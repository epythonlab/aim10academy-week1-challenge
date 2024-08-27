import pandas as pd

def headline_length_stats(data: pd.DataFrame) -> pd.Series:
    """
    Calculate and return descriptive statistics for the length of headlines.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing the data.
    
    Returns:
        pd.Series: Descriptive statistics for headline lengths.
    """
    data['headline_length'] = data['headline'].apply(len)
    
    return data['headline_length'].describe()

def articles_per_publisher(data: pd.DataFrame) -> pd.Series:
    """
    Count the number of articles per publisher.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing the data.
    
    Returns:
        pd.Series: Counts of articles per publisher.
    """
    return data['publisher'].value_counts()

def articles_by_day_of_week(data: pd.DataFrame) -> pd.Series:
    """
    Analyze the distribution of articles by day of the week.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing the data.
    
    Returns:
        pd.Series: Counts of articles by day of the week.
    """
    if not pd.api.types.is_datetime64_any_dtype(data['date']):
        raise ValueError("The 'date' column must be in datetime format.")
    
    data['day_of_week'] = data['date'].dt.day_name()
    
    return data['day_of_week'].value_counts()
