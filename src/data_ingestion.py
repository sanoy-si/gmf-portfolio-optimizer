import yfinance as yf
import pandas as pd
import os

def fetch_and_save_data(tickers, start_date, end_date, file_path):
    """
    Fetches historical financial data for a list of tickers from Yahoo Finance
    and saves it to a CSV file. If the file already exists, it loads the data
    from the file instead of re-fetching.

    Args:
        tickers (list): A list of stock tickers (e.g., ['TSLA', 'SPY']).
        start_date (str): The start date for the data in 'YYYY-MM-DD' format.
        end_date (str): The end date for the data in 'YYYY-MM-DD' format.
        file_path (str): The path to save or load the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the historical data.
    """
    # Check if the data file already exists
    if os.path.exists(file_path):
        print(f"Loading data from {file_path}...")
        data = pd.read_csv(file_path, header=[0, 1], index_col=0, parse_dates=True)
    else:
        print(f"Downloading data for {tickers} from {start_date} to {end_date}...")
        data = yf.download(tickers, start=start_date, end=end_date)
        
        # Ensure the directory exists before saving
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        data.to_csv(file_path)
        print(f"Data saved to {file_path}")
        
    return data

if __name__ == '__main__':
    TICKERS = ['TSLA', 'BND', 'SPY']
    START_DATE = '2015-07-01'
    END_DATE = '2025-07-31'
    RAW_DATA_PATH = 'data/raw/financial_data.csv'
    
    # Run the data fetching function
    financial_data = fetch_and_save_data(TICKERS, START_DATE, END_DATE, RAW_DATA_PATH)
    
    print("\nData Head:")
    print(financial_data.head())
    
    print("\nData Info:")
    financial_data.info()