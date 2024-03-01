import streamlit as st
import pandas as pd
import numpy as np
import pyodbc
from dotenv import dotenv_values






st.set_page_config(
    page_title='Datapage',
    page_icon='',
    layout='wide')

# Create an instance of the environment variable 
environment_variable = dotenv_values('.env')


server_name = environment_variable.get('server')
username = environment_variable.get('user')
password = environment_variable.get('password')
database_name = environment_variable.get('database')

connection_string = f"DRIVER={{SQL Server}};SERVER={server_name};PWD={password};DATABASE={database_name};UID={username}"

connection = pyodbc.connect(connection_string)

# Load the  dataset from the database
query = 'SELECT * FROM dbo.LP2_Telco_churn_first_3000'
df = pd.read_sql(query, connection)
st.dataframe(df)
