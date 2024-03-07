import streamlit as st
import pandas as pd


st.set_page_config(
    page_title='HISTORY',
    page_icon='',
    layout='wide'
)

st.title('History Page')

def create_prediction_history():
    df = pd.read_csv('./data/history.csv')

    return df

if __name__ == '__main__':
    df = create_prediction_history()
    st.dataframe(df)
