import streamlit as st
import sys
sys.path.append('..')  # Adds the parent directory to the Python path
from scripts.stock_analysis import load_data, plot_stock_data, plot_rsi, plot_macd

# Streamlit UI
def main():
    st.title('Stock Data Visualization')

    # Load data
    df = load_data('../Data/stock_data.csv')
    stocks = df['stock'].unique()

    selected_stock = st.sidebar.selectbox('Select Stock', stocks)
    indicator = st.sidebar.selectbox('Select Indicator', ['Moving Averages', 'RSI', 'MACD'])

    if indicator == 'Moving Averages':
        fig = plot_stock_data(selected_stock, df)
    elif indicator == 'RSI':
        fig = plot_rsi(selected_stock, df)
    elif indicator == 'MACD':
        fig = plot_macd(selected_stock, df)

    st.pyplot(fig)

if __name__ == "__main__":
    main()
