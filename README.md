# 10 Academy: Artificial Intelligence Mastery

### Week 1 Challenge Document
### Date: 26 August - 03 September 2024


# Financial News and Stock Price Integration Dataset (FNSPID)

## Overview

The Financial News and Stock Price Integration Dataset (FNSPID) project is designed to enhance stock market predictions by combining quantitative and qualitative data. This project integrates sentiment analysis of financial news headlines with stock price movements to provide insights into how news sentiment impacts stock performance.

### Key Features
- **Sentiment Analysis**: Quantify the tone and sentiment expressed in financial news headlines using Natural Language Processing (NLP) techniques.
- **Correlation Analysis**: Establish statistical correlations between sentiment derived from news articles and corresponding stock price movements.
- **Streamlit App**: An interactive dashboard for visualizing sentiment analysis and correlation results.

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
│   ├── sentiment_analysis.py  # Sentiment analysis functions
│   ├── correlation_analysis.py# Correlation analysis functions
│   └── data_processing.py     # Data loading and preprocessing functions
├── notebooks/
│   ├── __init__.py
│   ├── sentiment_analysis_notebook.ipynb  # Jupyter notebook for sentiment analysis
│   └── correlation_analysis_notebook.ipynb# Jupyter notebook for correlation analysis
├── tests/
│   ├── __init__.py
│   ├── test_sentiment_analysis.py   # Unit tests for sentiment analysis
│   ├── test_correlation_analysis.py # Unit tests for correlation analysis
│   └── test_data_processing.py      # Unit tests for data processing
└── scripts/
    ├── __init__.py
    ├── streamlit_app.py      # Streamlit app script
    └── README.md             # Documentation for the scripts directory

# Installation

>>> git clone https://github.com/epythonlab/aim10academy-week1-challenge.git
cd aim10academy-week1-challenge

### Create virtual environment

>>> python3 -m venv venv # on MacOs or Linux
>>> source venv/bin/activate  # On Windows: venv\Scripts\activate

### Install Dependencies

>>> pip install -r requirements.txt



