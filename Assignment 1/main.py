from argparse import ArgumentParser
from data_fetch import download_historical_data
from perfomance import plot_performance
from datetime import date, datetime
import pandas as pd
import yfinance as yf

today = date.today().strftime('%Y-%m-%d')

parser = ArgumentParser()

parser.add_argument('-tf', '--timeframe', 
                    help='The frequency of the data in days (Default: 1d). Allowed intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo',
                    type=str, 
                    default='1d')

parser.add_argument('-sd', '--start_date', 
                    help='The start date of the data in the format YYYY-MM-DD',
                    type=str, 
                    default='2024-06-01')

parser.add_argument('-ed', '--end_date', 
                    help='The end date of the data in the format YYYY-MM-DD',
                    type=str, 
                    default=today)

parser.add_argument('-s', '--symbol', 
                    help='The stock symbol to download data for',
                    type=str, 
                    default='RELIANCE.NS')

args = parser.parse_args()

# Check if the timeframe is valid
allowed_timeframes = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
try :
    assert(args.timeframe in allowed_timeframes)
except AssertionError:
    print(f'Invalid timeframe {args.timeframe}. Allowed timeframes are {allowed_timeframes}')
    exit(1)

# Check if data is available for the given symbol
try:
    assert(yf.Ticker(args.symbol).history(period='1d').empty == False)
    df = download_historical_data(args.symbol, args.start_date, args.end_date, args.timeframe)
    plot_performance(df, args.symbol, args.start_date, args.end_date, args.timeframe)
except Exception as e:
    print(f'No data found for {args.symbol} from {args.start_date} to {args.end_date} with interval {args.timeframe}')

