import streamlit as st
import pandas as pd
import plotly.express as px
from snowflake.snowpark import Session
from snowflake.snowpark.context import get_active_session
import psycopg2
from psycopg2.extras import RealDictCursor
import json

# 페이지 제목 설정
st.title("Snowflake Data Analysis")

session = get_active_session()

# DEP_PAX 데이터 조회
st.subheader("DEP_PAX Data")
dep_pax_sql = 'SELECT * FROM dev_flexa_dwh_db.public."2402_DEP_PAX" LIMIT 20'
dep_pax_data = session.sql(dep_pax_sql).collect()
st.dataframe(dep_pax_data)


def get_snowflake_secret():
    session = get_active_session()
    secret = session.sql("SELECT GET_SECRET('redshift_secret')").collect()[0][0]
    return json.loads(secret)


# Secret 값 가져오기
redshift_config = get_snowflake_secret()

# 각 값 사용하기
host = redshift_config["host"]
port = redshift_config["port"]
database = redshift_config["database"]

# # Redshift secret 가져오기
# redshift_secret = session.sql("SELECT SYSTEM$GET_SECRET('redshift_secret')").collect()[
#     0
# ]["SYSTEM$GET_SECRET('redshift_secret')"]

# redshift_config = json.loads(redshift_secret)

# # Redshift 연결
# redshift_conn = psycopg2.connect(
#     host=redshift_config["host"],
#     port=redshift_config["port"],
#     database=redshift_config["database"],
#     cursor_factory=RealDictCursor,
# )
