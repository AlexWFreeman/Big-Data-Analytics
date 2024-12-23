## Overview

AI trader is an automated trading system that uses artificial intelligence (AI) techniques to analyze financial markets and execute trades.
This repo implements the components of our system as described in the paper. Our system consists of gathering financial data, labeling the
sentiments of financial news, predicting price movements with machine learning models, simulating trading on each stock, and optimizing portfolio
performance as a whole. The picture below illustrates the pipeline of our system from data sources to trade execution.

The introduction video of our project is available at: https://www.youtube.com/watch?v=RLRWkY7VKfg&t=1s

<img width="409" alt="image" src="https://github.com/user-attachments/assets/fe3812a7-1da2-4f22-aa28-fff4ba4b368c" />

## Components

**Data Gathering:** We gather data mainly from polygon.io. website. `data_paser.ipynb` extracts stock price and news data from polygon and save
them into csv files under `dataset/stocks` and `dataset/news`, respectively. We also explored news data with sentiment and relation scores from
marketaux and alpha vatange (although we didn't use them in our final design). We extract and analyze these data in `data_pulling.ipynb` and
`mt-alpha_data_relevance.ipynb` and store the csv files in `dataset/news_maux` and `dataset/news_alpha`, respectively.
We use utilities under `data_combine` to preprocess the raw data in `news_maux` and `news_alpha`.

**Sentiment Analysis:** We use finBert to generate sentiment labels and scores from news titles, keywords, and descriptions (summaries).
Our scripts to run finBERT and analyze the sentiments are stored under `sentiment`. Our sentiment dataset is `dataset/polygon_title_sentiment_3`.

**Price Prediction:** We predicted the next day's price based on historical prices and news sentiment scores. We did basic analysis for
our dataset in `model/analysis.ipynb`. Our prediction model is `model/price_prediction.ipynb` which preprocess the raw data, train the LSTM
model, and generate predicted prices in a 20-fold pattern. Our predicted prices are stored under `price_sim`, which is used in trading steps.
We also explored other machine learning models and approaches (although not used in our final design), some of which are stored in `alternative_model`.

**Trading Strategy and Portfolio Optimization:** The scripts for the last two steps are in `model/do_trade.ipynb` which takes in predicted prices and
generate the percentages of each stock to hold in the portfolio (or position for single stocks) and evaluate the yield rate and Sharpe ratios.
The trading results including portfolio ratios, yield trends, etc. are stored under `results`. `single_stock` are the results of trading single stocks.
`portfolio_short.csv` and `portfolio.csv` are the results of trading the portfolio, enabling or disabling short selling.

**Visualization:** We've developed a website under `webpages` containing three pages for visualization. We described the use of it in
our videos. You can start a local server and open index.html to browse it.
