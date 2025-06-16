import pandas as pd
import numpy as np

def add_simple_features(df):
    """Add basic technical indicators without TA-Lib."""
    
    # Simple Moving Averages
    df['SMA_5'] = df['Close'].rolling(window=5).mean()
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    
    # Price changes
    df['Price_Change'] = df['Close'].pct_change()
    df['Price_Change_5d'] = df['Close'].pct_change(5)
    
    # Volume indicators
    df['Volume_SMA'] = df['Volume'].rolling(window=20).mean()
    df['Volume_Ratio'] = df['Volume'] / df['Volume_SMA']
    
    # Volatility
    df['Volatility'] = df['Price_Change'].rolling(window=20).std()
    
    # High-Low spread
    df['HL_Spread'] = (df['High'] - df['Low']) / df['Close']
    
    return df

def create_targets(df):
    """Create prediction targets."""
    # Next day direction (1 if price goes up, 0 if down)
    df['Target_1d'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    
    # 5-day direction
    df['Target_5d'] = (df['Close'].shift(-5) > df['Close']).astype(int)
    
    return df
