# 🌾 MandiPredict

> ⚠️ **Experimental Project** — This is an early-stage prototype and not a final production-ready product. The forecasts are for learning and research purposes only and should not be used for real financial or business decisions.

A time series forecasting web app that predicts **onion mandi prices** at Medinipur(West) APMC, West Bengal, India — built with Facebook Prophet and real government data from Agmarknet.

---

## 📌 Project Overview

MandiPredict is a crop price forecasting application built as part of a personal ML portfolio. It uses **5 years of real historical onion price data** (2021–2026) sourced directly from the Government of India's Agmarknet portal to forecast future weekly prices at the Medinipur(West) APMC market.

The project demonstrates the complete lifecycle of a time series ML project — from raw government data to a deployed interactive web application.

---

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-url-here)

> Replace the link above with your Streamlit Cloud deployment URL after deployment.

---

## 📊 Features

- 📈 **Interactive forecast chart** — visualize actual vs predicted onion prices
- 🎛️ **Adjustable forecast horizon** — forecast 4 to 52 weeks into the future using a slider
- 📋 **Forecast table** — weekly predicted prices with lower and upper confidence bounds
- 💡 **Key insight cards** — next week price, peak price, and lowest price at a glance
- 🌿 **Dark green farming theme** — clean and intuitive UI

---

## 🗂️ Dataset

| Property | Details |
|---|---|
| **Source** | [Agmarknet — Government of India](https://agmarknet.gov.in) |
| **Commodity** | Onion |
| **Market** | Medinipur(West) APMC, West Bengal |
| **Date Range** | March 2021 — March 2026 |
| **Frequency** | Weekly (resampled from daily) |
| **Price Unit** | Rs. per Quintal (Modal Price) |

---

## 🧠 Model Details

| Property | Details |
|---|---|
| **Algorithm** | Facebook Prophet |
| **Growth** | Flat (no long-term trend assumed) |
| **Yearly Seasonality** | Enabled |
| **Weekly Seasonality** | Disabled |
| **Daily Seasonality** | Disabled |
| **Preprocessing** | Log transform applied before training, inverse transform after prediction |
| **MAE** | ₹613 per quintal |
| **RMSE** | ₹778 per quintal |
| **MAPE** | ~26.7% |

### Why Log Transform?
Onion prices are highly volatile with occasional extreme spikes (₹5000+). Log transform ensures predictions always remain positive and handles price spikes more gracefully.

### Why Flat Trend?
Crop prices don't follow a consistent upward or downward trend — they are primarily driven by seasonal harvest cycles. Flat trend prevents the model from over-extrapolating recent low or high price periods.

---

## 🔍 Key Findings from EDA

- Onion prices at Medinipur(West) APMC consistently **spike every October–November** (weeks 40–50) due to post-monsoon supply shortage
- Prices are typically **lowest in April–June** during harvest season when supply is high
- The **2023 price spike** (₹5000+) coincided with India's onion export ban
- **2025 was unusually calm** with prices staying low around ₹1500 throughout the year

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Facebook Prophet** — time series forecasting
- **Pandas & NumPy** — data processing
- **Matplotlib** — data visualization
- **Streamlit** — web app framework

---

## 📁 Project Structure

```
MandiPredict/
├── app.py                        # Main Streamlit application
├── onion_medinipur.csv           # Cleaned weekly price data
├── crop_price_forecaster.ipynb   # EDA and model building notebook
├── Medinipur.xlsx                # Raw data from Agmarknet
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## ⚙️ Run Locally

1. Clone the repository:
```bash
git clone https://github.com/aviksarkar0204-stack/MandiPredict.git
cd MandiPredict
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

---

## ⚠️ Limitations & Disclaimer

This project is in an **experimental stage** and has the following known limitations:

- The model achieves a MAPE of ~26.7% which is acceptable for crop price forecasting but not suitable for precise financial decisions
- Sudden price spikes caused by **government policy changes** (export bans, MSP revisions) or **extreme weather events** cannot be predicted from price data alone
- The dataset currently covers only **one market** (Medinipur West APMC) and **one commodity** (Onion)
- Data is not automatically updated — manual CSV upload is required to incorporate new price data
- Forecasts beyond 3–4 months should be interpreted with caution due to widening confidence intervals

---

## 🔮 Future Improvements

- [ ] Add "Upload & Update" feature to append new Agmarknet data and retrain model automatically
- [ ] Add Tomato price forecasting
- [ ] Include more West Bengal markets (Kolkata, Ghatal, Garbeta)
- [ ] Incorporate rainfall and seasonal data as additional features
- [ ] Improve MAPE with XGBoost + lag features approach

---

## 👨‍💻 Author

**Avik Sarkar**
- GitHub: [@aviksarkar0204-stack](https://github.com/aviksarkar0204-stack)
- Data Source: [Agmarknet — Government of India](https://agmarknet.gov.in)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ using real government data from my hometown — Medinipur, West Bengal 🌾*
