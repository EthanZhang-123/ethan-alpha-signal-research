import yfinance as yf
import pandas as pd

hsi_ticker_file = pd.read_csv("AASTOCKS_Export_2025-6-6.csv")

hsi_tickers = hsi_ticker_file['Symbol'].tolist()

def download_stock_price(tickers):
    for ticker in tickers:
        ticker = ticker.strip()
        stock = yf.Ticker(ticker)
        price = stock.history(start="2020-01-01", end=None)
        price.to_csv(f"HSI_Tickers/{ticker}.csv")

download_stock_price(hsi_tickers)