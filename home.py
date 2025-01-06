import streamlit as st
import pandas as pd
import plotly.express as px
from snowflake.snowpark import Session
from snowflake.snowpark.context import get_active_session

# 페이지 제목 설정
st.title("Snowflake Data Analysis")

session = get_active_session()

# DEP_PAX 데이터 조회
st.subheader("DEP_PAX Data")
dep_pax_sql = "SELECT * FROM CIRIUMSKY.PUBLIC.FLIGHTS_EXTENDED LIMIT 20"
dep_pax_data = session.sql(dep_pax_sql).collect()
st.dataframe(dep_pax_data)
