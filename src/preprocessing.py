import pandas as pd
from statsmodels.tsa.stattools import adfuller

def preprocess_data(df):
    """
    Performs basic preprocessing on the financial data.

    Args:
        df (pd.DataFrame): The raw financial data.

    Returns:
        pd.DataFrame: The preprocessed data.
    """
    # Use Adjusted Close for analysis as it accounts for dividends and splits
    adj_close_df = df['Adj Close'].copy()
    
    # Check for missing values
    if adj_close_df.isnull().sum().any():
        print("Missing values found. Interpolating...")
        # Use time-based interpolation for financial series
        adj_close_df = adj_close_df.interpolate(method='time')
        adj_close_df = adj_close_df.fillna(method='bfill') # Backfill any remaining NaNs
    
    print("Preprocessing complete. No missing values.")
    return adj_close_df

def calculate_daily_returns(df):
    """
    Calculates the daily percentage change in price.
    
    Args:
        df (pd.DataFrame): DataFrame with asset prices.
        
    Returns:
        pd.DataFrame: DataFrame with daily returns.
    """
    daily_returns = df.pct_change().dropna()
    return daily_returns

def check_stationarity(series, series_name=''):
    """
    Performs the Augmented Dickey-Fuller test to check for stationarity.

    Args:
        series (pd.Series): The time series data to test.
        series_name (str): The name of the series for printing.
    """
    print(f'--- Stationarity Test for {series_name} ---')
    result = adfuller(series.dropna())
    
    print(f'ADF Statistic: {result[0]:.4f}')
    print(f'p-value: {result[1]:.4f}')
    print('Critical Values:')
    for key, value in result[4].items():
        print(f'\t{key}: {value:.4f}')
        
    if result[1] <= 0.05:
        print(f"Conclusion: p-value is less than 0.05. The series '{series_name}' is likely stationary.")
    else:
        print(f"Conclusion: p-value is greater than 0.05. The series '{series_name}' is likely non-stationary.")
    print('--- End of Test ---\n')