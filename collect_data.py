import yfinance as yf
import pandas as pd
from datetime import datetime
import os

def download_reliance_data():
    print("Downloading RELIANCE.NS data...")
    
    # Download 2 years of data
    ticker = yf.Ticker("RELIANCE.NS")
    data = ticker.history(period="2y")
    
    if data.empty:
        print("No data downloaded!")
        return
    
    # Create data directory
    os.makedirs("data", exist_ok=True)
    
    # Save data
    filename = f"data/RELIANCE_NS_{datetime.now().strftime('%Y%m%d')}.csv"
    data.to_csv(filename)
    
    # Also save as latest
    data.to_csv("data/RELIANCE_NS_latest.csv")
    
    print(f"Saved {len(data)} records to {filename}")
    print(f"Date range: {data.index[0]} to {data.index[-1]}")

if __name__ == "__main__":
    download_reliance_data()
