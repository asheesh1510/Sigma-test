import streamlit as st
import snowflake.connector

conn = snowflake.connector.connect(
    user="hemanthosi",
    password="Osi@Digital!@34",
    account="MWDVYOC-BS73011",
    warehouse="COMPUTE_WH",
    database="TST_EDW",
    schema="BASE"
)


cur = conn.cursor()
cur.execute("SELECT * FROM TST_EDW.BASE.USERS LIMIT 10")
data = cur.fetchall()

st.write(data)
