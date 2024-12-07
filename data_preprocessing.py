import os
import pandas as pd


def process_stock_data(stock_file):
    """
    Process stock data to extract the necessary columns and format time.

    Parameters:
        stock_file (str): Path to the stock CSV file.

    Returns:
        pd.DataFrame: Processed stock data with columns ['time', 'close'].
    """
    stock_data = pd.read_csv(stock_file)
    stock_data = stock_data.loc[:, ['time', 'close']]
    stock_data['time'] = pd.to_datetime(stock_data['time'])
    return stock_data


def process_sentiment_data(sentiment_file, ticker):
    """
    Process sentiment data to calculate daily average sentiment scores.

    Parameters:
        sentiment_file (str): Path to the sentiment CSV file.
        ticker (str): Stock ticker symbol (e.g., 'AAPL').

    Returns:
        pd.DataFrame: Processed sentiment data with daily sentiment scores.
    """
    sentiment_data = pd.read_csv(sentiment_file)
    sentiment_data = sentiment_data[sentiment_data['ticker'] == ticker]
    sentiment_data = sentiment_data.loc[:, ['time', 'sentiment_score']]
    sentiment_data['time'] = pd.to_datetime(sentiment_data['time'])

    # Group by date and calculate mean sentiment score
    sentiment_data['date'] = sentiment_data['time'].dt.date
    grouped_data = sentiment_data.groupby('date').apply(
        lambda x: pd.Series({
            'time': pd.Timestamp(f"{x['date'].iloc[0]} 04:00:00"),
            'sentiment_score': x['sentiment_score'].mean()
        })
    ).reset_index(drop=True)

    return grouped_data


def merge_data(stock_data, sentiment_data):
    """
    Merge stock and sentiment data on time.

    Parameters:
        stock_data (pd.DataFrame): Processed stock data.
        sentiment_data (pd.DataFrame): Processed sentiment data.

    Returns:
        pd.DataFrame: Final merged dataset.
    """
    final_data = pd.merge(stock_data, sentiment_data, on='time')
    final_data.columns = ["DateTime", 'Price', 'Sentiment_score']
    final_data = final_data[['DateTime', 'Sentiment_score', 'Price']]
    return final_data


def process_ticker(ticker, stock_dir, sentiment_dir, output_dir):
    """
    Process data for a specific ticker and save the output.

    Parameters:
        ticker (str): Stock ticker symbol (e.g., 'AAPL').
        stock_dir (str): Directory containing stock files.
        sentiment_dir (str): Directory containing sentiment files.
        output_dir (str): Directory to save processed files.
    """
    stock_file = os.path.join(stock_dir, f"{ticker}.csv")
    sentiment_file = os.path.join(sentiment_dir, f"{ticker}_title_sentiments.csv")
    output_file = os.path.join(output_dir, f"{ticker}_processed_data.csv")

    stock_data = process_stock_data(stock_file)
    sentiment_data = process_sentiment_data(sentiment_file, ticker)
    final_data = merge_data(stock_data, sentiment_data)

    final_data.to_csv(output_file, index=False)
    print(f"Processed data for {ticker} saved to {output_file}")


def main():
    tickers = ['AAPL', 'GOOGL', 'MSFT', 'META', 'AMZN']
    stock_dir = "./dataset/stocks"
    sentiment_dir = "./dataset/polygon_title_sentiment_3"
    output_dir = "./processed_data"

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for ticker in tickers:
        process_ticker(ticker, stock_dir, sentiment_dir, output_dir)


if __name__ == "__main__":
    main()
