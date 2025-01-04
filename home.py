import streamlit as st
import pandas
import plotly.express as px
from snowflake.snowpark import Session

st.write('aaa')

# Snowflake 연결 생성 (Native App 환경에서 자동으로 연결)
conn = st.connection("snowflake")

# 데이터 쿼리
df = conn.query("SELECT * FROM sim_df_dict LIMIT 1")
st.dataframe(df)