import streamlit as st
import pandas as pd






st.set_page_config(
    page_title='DATAPAGE',
    page_icon='',
    layout='wide')

df = pd.read_csv('LP2_Telco-churn-last-2000 (1).csv')
st.dataframe(df)
st.map(df)