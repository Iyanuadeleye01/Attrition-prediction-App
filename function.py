import streamlit as st
import pandas as pd
import numpy as np
import pyodbc


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

@st.cache_data()
def all_feature_selection():
    query = "SELECT * FROM dbo.LP2_Telco_churn_first_3000"
    data = query_database(query)
    return data