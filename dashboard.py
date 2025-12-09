import streamlit as st
import sqlite3
import pandas as pd

# 1. SETUP PAGE
st.set_page_config(page_title="Amazon Price Tracker", page_icon="📉")
st.title("📉 Amazon Price History Tracker")
st.markdown("This dashboard reads directly from the **SQLite Database** updated daily by **GitHub Actions**.")

# 2. CONNECT TO DATABASE
# The database file is in the same folder
DB_NAME = 'amazon_prices.db'

def load_data():
    try:
        conn = sqlite3.connect(DB_NAME)
        # Read SQL into a Pandas DataFrame
        df = pd.read_sql_query("SELECT * FROM prices", conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Error loading database: {e}")
        return pd.DataFrame()

df = load_data()

# 3. DISPLAY METRICS
if not df.empty:
    # Get the latest price
    latest_price = df.iloc[-1]['price']
    latest_date = df.iloc[-1]['timestamp']
    
    # Get the lowest price ever recorded
    min_price = df['price'].min()
    max_price = df['price'].max()

    col1, col2, col3 = st.columns(3)
    col1.metric("Latest Price", f"₹{latest_price:,.2f}")
    col2.metric("Lowest Price Ever", f"₹{min_price:,.2f}")
    col3.metric("Last Updated", latest_date.split(" ")[0])

    # 4. PLOT HISTORY
    st.subheader("Price Trend Over Time")
    
    # Convert timestamp to datetime object for better plotting
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Create a line chart
    st.line_chart(df.set_index('timestamp')['price'])

    # 5. SHOW RAW DATA (Optional)
    with st.expander("See Raw Data"):
        st.dataframe(df.sort_values(by='timestamp', ascending=False))

else:
    st.warning("No data found yet. The scraper needs to run at least once!")