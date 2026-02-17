import streamlit as st
import pandas as pd
import numpy as np
import snowflake.connector

@st.cache_resource
def get_snowflake_connection():
    return snowflake.connector.connect(
        account=st.secrets["snowflake"]["MWDVYOC-BS73011"],
        user=st.secrets["snowflake"]["hemanthosi"],
        password=st.secrets["snowflake"]["Osi@Digital!@34"],
        warehouse=st.secrets["snowflake"]["COMPUTE_WH"],
        database=st.secrets["snowflake"]["DEV_EDW"],
        schema=st.secrets["snowflake"]["BASE"],
        role=st.secrets["snowflake"]["ACCOUNT_ADMIN"]
    )

conn = get_snowflake_connection()

# Page config
st.set_page_config(page_title="Simple Demo Report", layout="wide")

st.title("📊 Simple Demo Report (No Database Required)")

# ---- Generate Dummy Data ----
np.random.seed(42)

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": np.random.randint(10000, 50000, 6),
    "Profit": np.random.randint(2000, 15000, 6)
})

# ---- KPIs ----
total_sales = data["Sales"].sum()
total_profit = data["Profit"].sum()
avg_profit = data["Profit"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Avg Profit", f"${avg_profit:,.0f}")

st.divider()

# ---- Table ----
st.subheader("Sales Data")
st.dataframe(data, use_container_width=True)

# ---- Charts ----
col4, col5 = st.columns(2)

with col4:
    st.subheader("Monthly Sales")
    st.bar_chart(data.set_index("Month")["Sales"])

with col5:
    st.subheader("Monthly Profit Trend")
    st.line_chart(data.set_index("Month")["Profit"])

st.success("Report generated successfully without using any Snowflake tables.")

