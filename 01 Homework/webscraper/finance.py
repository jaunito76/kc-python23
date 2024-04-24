import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(ticker: str, start_date: str, end_date: str):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def main():
    stock_tickers = [
        'AAPL',  # Apple
        'MSFT',  # Microsoft
        'AMZN',  # Amazon
        'GOOGL',  # Google
        'FB',  # Facebook
        'TSLA',  # Tesla
        'BRK-B',  # Berkshire Hathaway
        'JPM',  # JPMorgan Chase
        'JNJ',  # Johnson & Johnson
        'V',  # Visa
    ]
    start_date = '2020-01-01'
    end_date = '2020-12-31'
    stock_data = []
    for ticker in stock_tickers:
        stock_data.append(fetch_stock_data(ticker, start_date, end_date))
    print(stock_data)
    for data in stock_data:
        data['Close'].plot()
    plt.show()
    
if __name__ == '__main__':
    main()