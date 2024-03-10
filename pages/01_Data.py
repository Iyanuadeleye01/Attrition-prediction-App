
import streamlit as st
import pandas as pd
from login import authenticate_user, entered_cred

#from function import all_feature_selection

st.set_page_config(
    page_title='Datapage',
    page_icon='',
    layout='wide')

st.markdown( """ <style>
            section[data-testid="stSidebar"]
            { width: 200px !important;
            }
            </style> """,
            unsafe_allow_html=True,
)


def data_page_content():
    entered_cred()
    if authenticate_user():
        st.title('The proprietary Data from Vodafone')
        df = pd.read_csv('./data/streamlitdata.csv')

        col1, col2 = st.columns(2)
        with col1:
            selected_feature = st.selectbox('Select Feature Type', options=['All Features', 'Numeric Features', 'Categorical Features'], key='select_feature')

        if selected_feature == 'Numeric Features':
            df = df.select_dtypes(include='number')
        elif selected_feature == 'Categorical Features':
            df = df.select_dtypes(include='object')

        st.dataframe(df)
    else:
        st.error("Please enter 'admin' as username and password to login")

if __name__ == '__main__':
    data_page_content()
        

