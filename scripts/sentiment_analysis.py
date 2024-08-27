import pandas as pd
from textblob import TextBlob

def sentiment_analysis(data: pd.DataFrame) -> pd.DataFrame:
    """
    Perform sentiment analysis on headlines.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing the data.
    
    Returns:
        pd.DataFrame: DataFrame with an added 'sentiment' column.
    """
    data['sentiment'] = data['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    
    return data[['headline', 'sentiment']]
