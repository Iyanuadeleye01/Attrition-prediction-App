import streamlit as st
import pandas as pd
import numpy as np
import pyodbc
from dotenv import dotenv_values






st.set_page_config(
    page_title='Datapage',
    page_icon='',
    layout='wide')

st.title('The proprietary Data from Vodafone')



# Function to create a database connection
@st.cache_resource(show_spinner="Connecting to database...")
def create_connection():
    connection = pyodbc.connect(
        DRIVER="{SQL Server};"
        + "SERVER=" + st.secrets["server"]
        + ";PWD=" + st.secrets["password"]
        + ";DATABASE=" + st.secrets["database"]
        + ";UID=" + st.secrets["user"]
    )
    return connection

# Connect to the database
conn = create_connection()

# Function to query the database
def query_database(query):
    with conn.cursor() as curs:
        curs.execute(query)
        rows = curs.fetchall()
        data = pd.DataFrame.from_records(data=rows, columns=[col[0] for col in curs.description])
    return data

# Function to select all features
@st.cache_data()
def all_feature_selection():
    query = "SELECT * FROM dbo.LP2_Telco_churn_first_3000"
    data = query_database(query)
    return data





# Main code block to display features based on user selection
if __name__ == "__main__":
    col1, col2 = st.columns(2)
    with col1:
        selected_feature = st.selectbox('Select Feature Type', options=['All Features', 'Numeric Features', 'Categorical Features'], key='select_feature')

    if selected_feature == 'All Features':
        df = all_feature_selection()
    else: 
        df = all_feature_selection()
        if selected_feature == 'Numeric Features':
            df = df.select_dtypes(include='number')
        else:
            df = df.select_dtypes(include='object')

        

    st.dataframe(df)
    #st.write(st.session_state)

