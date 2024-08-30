# 10 Academy: Artificial Intelligence Mastery

### Week 1 Challenge Document
### Date: 26 August - 03 September 2024


# Financial News and Stock Price Integration Dataset (FNSPID)

## Overview

The Financial News and Stock Price Integration Dataset (FNSPID) project is designed to enhance stock market predictions by combining quantitative and qualitative data. This project integrates sentiment analysis of financial news headlines with stock price movements to provide insights into how news sentiment impacts stock performance.

### Key Features
- **Sentiment Analysis**: Quantify the tone and sentiment expressed in financial news headlines using Natural Language Processing (NLP) techniques.
- **Correlation Analysis**: Establish statistical correlations between sentiment derived from news articles and corresponding stock price movements.
- **Financial Quantitative Analysis**: comprehensive quantitative evaluation of stock market data and its correlation with financial news using technical analysis indicators and financial metrics.

## Directory Structure

```plaintext
├── .vscode/
│   └── settings.json          # VS Code project-specific settings
├── .github/
│   └── workflows/
│       └── unittests.yml      # GitHub Actions workflow for running unit tests
├── .gitignore                 # Specifies files and directories to be ignored by Git
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation (this file)
├── src/
│   ├── __init__.py
│   
├── notebooks/
│   ├── __init__.py
│   ├── stock_news.ipynb  # Jupyter notebook for stock news analysis
│   └── financial_analysis_notebook.ipynb# Jupyter notebook for financial analysis
├── tests/
│   ├── __init__.py
│   ├── test_sentiment_analysis.py   # Unit tests for sentiment analysis
│   ├── test_publication_analysis.py # Unit tests for publication analysis
│   └── test_data_processing.py      # Unit tests for data processing
    ├── test_descriptive_analysis.py # Unit tests for exploratory analysis 

└── scripts/
    ├── __init__.py
    ├── publication_analysis.py # Script for publication analysis
    ├── sentiment_analysis.py # script for sentiment analysis
    ├── data_processing.py # sript for data processing
    ├── descriptive_analysis.py # script for descriptive analysis
    ├── correlation_analysis.py # script for correlation analysis    
    └── README.md             # Documentation for the scripts directory

# Installation

>>> git clone https://github.com/epythonlab/aim10academy-week1-challenge.git
cd aim10academy-week1-challenge

### Create virtual environment

>>> python3 -m venv venv # on MacOs or Linux
>>> source venv/bin/activate  # On Windows: venv\Scripts\activate

### Install Dependencies

>>> pip install -r requirements.txt

## To run tests
navigate 
>>> cd tests/
>>pytest # all tests will be tested



