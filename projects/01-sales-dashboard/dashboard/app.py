import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Superstore Sales Performance Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/superstore.csv')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
region = st.sidebar.multiselect("Region", df['Region'].unique(), default=df['Region'].unique())

filtered_df = df[df['Region'].isin(region)]

# Key Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.0f}")
col3.metric("Profit Margin", f"{(filtered_df['Profit'].sum()/filtered_df['Sales'].sum()*100):.1f}%")
col4.metric("Orders", f"{len(filtered_df):,}")

# Visualizations
tab1, tab2, tab3 = st.tabs(["Trends", "Category Analysis", "Forecast"])

with tab1:
    st.subheader("Sales Trend")
    daily_sales = filtered_df.groupby('Order Date')['Sales'].sum().reset_index()
    fig = px.line(daily_sales, x='Order Date', y='Sales')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Profit by Category")
    cat_profit = filtered_df.groupby('Category')['Profit'].sum().reset_index()
    fig2 = px.bar(cat_profit, x='Category', y='Profit')
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.subheader("Sales Forecast (Next 6 Months)")
    st.info("Forecasting model would go here with Prophet")