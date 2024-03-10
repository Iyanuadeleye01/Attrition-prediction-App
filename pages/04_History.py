import streamlit as st
import pandas as pd
from login import authenticate_user, entered_cred


st.set_page_config(
    page_title='HISTORY',
    page_icon='',
    layout='wide'
)

def history_page_content():
    entered_cred()
    if authenticate_user():
        st.title('History Page')

        def create_prediction_history():
            df = pd.read_csv('./data/history.csv')
            st.dataframe(df)
            return df
        df = create_prediction_history()
    else:
        st.error("Please enter 'admin' as username and password")
if __name__ == '__main__':
    history_page_content()
    
    #st.dataframe(df)
