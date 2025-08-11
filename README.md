# GMF Investments: AI-Powered Portfolio Optimization

A data-driven strategy to optimize a financial portfolio (TSLA, SPY, BND) by forecasting returns with ARIMA/LSTM models and applying Modern Portfolio Theory. This project serves as a comprehensive demonstration of quantitative analysis, from data ingestion to strategy backtesting.

## Business Objective
This project was developed for Guide Me in Finance (GMF) Investments, a firm specializing in personalized portfolio management. The goal is to leverage data-driven insights to enhance portfolio performance, minimize risks, and capitalize on market opportunities by building and validating a quantitative investment strategy.

---

## Tech Stack
- **Data Analysis & ML:** `pandas`, `numpy`, `scikit-learn`, `statsmodels`
- **Time Series Forecasting:** `pmdarima` (for AutoARIMA), `tensorflow` (for LSTM)
- **Data Fetching:** `yfinance`
- **Portfolio Optimization:** `PyPortfolioOpt`
- **Visualization:** `matplotlib`, `seaborn`

---

## Project Structure
The repository is organized to separate concerns, making it modular and easy to navigate.

```
gmf-portfolio-optimizer/
├── .gitignore
├── data/ # Raw and processed data
├── models/ # Saved ARIMA and LSTM models
├── notebooks/ # Jupyter notebooks for analysis (run in order)
├── src/ # Reusable Python source code
├── requirements.txt # Project dependencies
└── README.md
```

---

## Setup and Installation

**1. Clone the repository:**
```bash
git clone https://github.com/sanoy-si/gmf-portfolio-optimizer.git
cd gmf-portfolio-optimizer
```

**2. Create and activate a virtual environment:**
```bash
# Create the environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

**3. Install the required packages:**
```bash
pip install -r requirements.txt
```

---

## Analysis Workflow
The analysis is structured across several Jupyter Notebooks in the `/notebooks` directory.  
They should be run in the following sequence:

1. **`1.0-data-exploration.ipynb`** – Fetches data, cleans it, performs EDA, and conducts stationarity tests.  
2. **`2.0-arima-modeling.ipynb` & `3.0-lstm-modeling.ipynb`** – Builds, trains, and evaluates the forecasting models (ARIMA and LSTM) for TSLA's stock price.  
3. **`4.0-portfolio-optimization.ipynb`** – Uses the best forecast to calculate expected returns and runs Modern Portfolio Theory optimization to find the optimal portfolio.  
4. **`5.0-backtesting.ipynb`** – Simulates the performance of the recommended portfolio against a 60/40 benchmark over a historical period.

---
