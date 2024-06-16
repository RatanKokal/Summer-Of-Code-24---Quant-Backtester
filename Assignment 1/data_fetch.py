import yfinance
import pandas

def download_historical_data(symbol, start_date, end_date, timeframe):
    data = yfinance.download(symbol, start=start_date, end=end_date, interval=timeframe)
    df = pandas.DataFrame(data)
    return df
    