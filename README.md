## Overview
AI trader is an automated trading system that uses artificial intelligence (AI) techniques to analyze financial markets and execute trades. 
This repo implements the components of our system as described in the paper. Our system consists of gathering financial data, labeling the 
sentiments of financial news, predicting price movements with machine learning models, simulating trading on each stock, and optimizing portfolio 
performance as a whole. The picture below illustrates the pipeline of our system from data sources to trade execution.

<img width="409" alt="image" src="https://github.com/user-attachments/assets/fe3812a7-1da2-4f22-aa28-fff4ba4b368c" />

## Components
**Data Gathering:** We gather data mainly from polygon.io. website. `data_paser.ipynb` extracts stock price and news data from polygon and save 
them into csv files under `dataset/stocks` and `dataset/news`, respectively. We also explored news data with sentiment and relation scores from 
marketaux and alpha vatange (although we didn't use them in our final design). We extract and analyze these data in `data_pulling.ipynb` and 
`mt-alpha_data_relevance.ipynb` and store the csv files in `dataset/news_maux` and `dataset/news_alpha`, respectively.
