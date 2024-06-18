from argparse import ArgumentParser
from data_fetch import download_historical_data
from perfomance import plot_performance
from datetime import date
import pandas as pd

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

try:
    yf.Ticker(args.symbol)
    df = download_historical_data(args.symbol, args.start_date, args.end_date, args.timeframe)
    plot_performance(df, args.symbol, args.start_date, args.end_date, args.timeframe)
except Exception as e:
    print(f'No data found for {args.symbol} from {args.start_date} to {args.end_date} with interval {args.timeframe}')

