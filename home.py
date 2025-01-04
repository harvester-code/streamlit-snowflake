import streamlit as st
import pandas
import plotly.express as px
from snowflake.snowpark import Session
from snowflake.snowpark.context import get_active_session

st.write("aaa")

# # Snowflake 연결 생성 (Native App 환경에서 자동으로 연결)
# conn = st.connection("snowflake")

# # 데이터 쿼리
# df = conn.query("SELECT * FROM sim_df_dict LIMIT 1")
# st.dataframe(df)

# # 현재 활성화된 세션 가져오기
session = Session.get_active_session()

# # 데이터 쿼리
# df = session.sql("SELECT * FROM sim_df_dict LIMIT 1").to_pandas()

# # Streamlit 앱 구성
# st.title("Snowflake Data Analysis")

# # 데이터 미리보기
# st.dataframe(df)
