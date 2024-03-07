import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth


st.set_page_config(
    page_title='Home',
    page_icon='',
    layout ='wide'
)


# add styling to the page
st.markdown("<h1 style='text-align: center; color: #006699;'>Welcome to the Vodafone Customer Attrition Prediction Application</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: #006699;'>This application provides predictions on customer attrition tendencies, offering valuable insights for customer retention strategies</h3>", unsafe_allow_html=True)

st.divider()


# Subheading
st.markdown("<h4 style='text-align: centre;'> Harnessing Data Insights to Predict Customer Attrition</h4>", unsafe_allow_html=True)

# add bullet point to the home page
st.write('- Empowering Vodafone: Predicting Customer Attrition')
st.write('- Enhancing Customer Retention: A Predictive Approach')
st.write('- Unveiling Customer Attrition Patterns: A Data-Driven Solution')
st.write('- Predictive Analytics for Customer Retention: The Vodafone Advantage')
st.write('- Insightful Predictions: Anticipating Customer Churn with Precision')


