import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet

st.set_page_config(page_title="MandiPredict", page_icon="🌾", layout="wide")

st.markdown("""
<style>
body { background-color: #0a1f0a; }
.stApp { background-color: #0a1f0a; color: #e0ffe0; }
h1, h2, h3 { color: #4caf50; }
.metric-card {
    background-color: #1a3a1a;
    border: 1px solid #4caf50;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
}
.metric-value { font-size: 28px; font-weight: bold; color: #4caf50; }
.metric-label { font-size: 14px; color: #a5d6a7; }
</style>
""", unsafe_allow_html=True)

st.title("🌾 MandiPredict")
st.markdown("#### Onion Price Forecaster — Medinipur(West) APMC, West Bengal")
st.markdown("---")

@st.cache_resource
def train_model():
    df = pd.read_csv('onion_medinipur.csv')
    df['ds'] = pd.to_datetime(df['ds'])
    df_log = df.copy()
    df_log['y'] = np.log(df['y'])
    model = Prophet(
        growth='flat',
        yearly_seasonality=True,
        weekly_seasonality=False,
        daily_seasonality=False
    )
    model.fit(df_log)
    return model, df

model, df_actual = train_model()

st.sidebar.title("⚙️ Settings")
weeks = st.sidebar.slider("Weeks to Forecast", min_value=4, max_value=52, value=26, step=4)
st.sidebar.markdown("---")
st.sidebar.markdown("📍 **Market:** Medinipur(West) APMC")
st.sidebar.markdown("🧅 **Commodity:** Onion")
st.sidebar.markdown("📅 **Data:** 2021 - 2026")

future = model.make_future_dataframe(periods=weeks, freq='W')
forecast = model.predict(future)

forecast['yhat'] = np.exp(forecast['yhat'])
forecast['yhat_lower'] = np.exp(forecast['yhat_lower'])
forecast['yhat_upper'] = np.exp(forecast['yhat_upper'])

future_only = forecast.tail(weeks)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">₹{future_only['yhat'].iloc[0]:.0f}</div>
        <div class="metric-label">Next Week Forecast</div>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">₹{future_only['yhat'].max():.0f}</div>
        <div class="metric-label">Peak Price (Next {weeks} Weeks)</div>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">₹{future_only['yhat'].min():.0f}</div>
        <div class="metric-label">Low Price (Next {weeks} Weeks)</div>
    </div>""", unsafe_allow_html=True)

st.markdown("---")
st.subheader("📈 Price Forecast Chart")

fig, ax = plt.subplots(figsize=(14, 5))
fig.patch.set_facecolor('#0a1f0a')
ax.set_facecolor('#0a1f0a')
ax.plot(df_actual['ds'], df_actual['y'], color='#4caf50', label='Actual Prices', linewidth=1.5)
ax.plot(forecast['ds'], forecast['yhat'], color='#ffeb3b', label='Predicted Prices', linewidth=1.5)
ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='#ffeb3b', alpha=0.15, label='Confidence Interval')
ax.axvline(pd.Timestamp(df_actual['ds'].max()), color='red', linestyle='--', linewidth=1, label='Forecast Start')
ax.set_xlabel('Date', color='#a5d6a7')
ax.set_ylabel('Price (Rs./Quintal)', color='#a5d6a7')
ax.tick_params(colors='#a5d6a7')
ax.legend(facecolor='#1a3a1a', labelcolor='#e0ffe0')
ax.grid(True, color='#1a3a1a')
for spine in ax.spines.values():
    spine.set_edgecolor('#4caf50')
st.pyplot(fig)

st.markdown("---")
st.subheader("📋 Forecast Table")

forecast_display = future_only[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
forecast_display.columns = ['Date', 'Predicted Price', 'Lower Bound', 'Upper Bound']
forecast_display['Date'] = forecast_display['Date'].dt.strftime('%d %b %Y')
forecast_display['Predicted Price'] = forecast_display['Predicted Price'].apply(lambda x: f"₹{x:.0f}")
forecast_display['Lower Bound'] = forecast_display['Lower Bound'].apply(lambda x: f"₹{x:.0f}")
forecast_display['Upper Bound'] = forecast_display['Upper Bound'].apply(lambda x: f"₹{x:.0f}")
st.dataframe(forecast_display, use_container_width=True, hide_index=True)

st.markdown("---")
st.caption("Data Source: Agmarknet — Government of India | Built with Prophet & Streamlit")