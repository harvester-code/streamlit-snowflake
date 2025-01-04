import streamlit as st
import pandas as pd
import plotly.express as px
from snowflake.snowpark import Session
from snowflake.snowpark.context import get_active_session

# 페이지 제목 설정
st.title("Snowflake Data Analysis")

session = get_active_session()

# TPCH 샘플 데이터 조회
st.subheader("TPCH Sample Data")
tpch_sql = "SELECT * FROM snowflake_sample_data.tpch_sf1.lineitem LIMIT 20"
tpch_data = session.sql(tpch_sql).collect()
st.dataframe(tpch_data)

# DEP_PAX 데이터 조회
st.subheader("DEP_PAX Data")
dep_pax_sql = 'SELECT * FROM dev_flexa_dwh_db.public."2402_DEP_PAX" LIMIT 20'
dep_pax_data = session.sql(dep_pax_sql).collect()
st.dataframe(dep_pax_data)
