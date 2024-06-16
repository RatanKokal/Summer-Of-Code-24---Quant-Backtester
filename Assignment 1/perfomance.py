from matplotlib import pyplot as plt

def plot_performance(df, symbol, start_date, end_date, timeframe):
    plt.figure(figsize=(10, 7))
    df['Close'].plot(title=f'{symbol} Performance from {start_date} to {end_date} with interval {timeframe}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.savefig(f'{symbol}_performance.png')
    # plt.show()