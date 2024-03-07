import streamlit as st
import joblib
import pandas as pd
import sklearn
import os

st.set_page_config(
    page_title='PREDICTION',
    page_icon='',
    layout='wide'
)

# Create functions to load the machine learning models
st.cache_resource(show_spinner='loading')
def load_reg_model():
    pipeline = joblib.load("./pages/models/logistic_regression_model.joblib")
    return pipeline

st.cache_resource(show_spinner='loading')
def load_random_model():
    pipeline = joblib.load("./pages/models/random_forest_model.joblib")
    return pipeline

# Create a function to select the Machine Learning algorithm to be used

@st.cache_resource(experimental_allow_widgets=True)
def model_selection():
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_model = st.selectbox('Selected Model', options=['Logistic Regression', 'Random Forest'], key='selected_model')
    with col2:
        pass
    with col3:
        pass

    # Create a condition to load the selected model
    if st.session_state['selected_model'] == 'Logistic Regression':
        pipeline = load_reg_model()
    else:
        pipeline = load_random_model()

    encoder = joblib.load("./pages/models/encoder.joblib")

    return pipeline, encoder

# if not os.path.exists('./data/history.csv'):
#         os.makedirs('./data')

# Create a function to make prediction with the pipeline and encoder as parameters
def get_prediction(pipeline, encoder):

    
    gender = st.session_state['gender']
    seniorcitizen = st.session_state['seniorcitizen']
    partner = st.session_state['partner']
    dependents = st.session_state['dependents']
    tenure = st.session_state['tenure']
    phoneservice = st.session_state['phoneservice']
    multiplelines = st.session_state['multiplelines']
    internetservice = st.session_state['internetservice']
    onlinesecurity = st.session_state['onlinesecurity']
    onlinebackup = st.session_state['onlinebackup']
    deviceprotection = st.session_state['deviceprotection']
    techsupport = st.session_state['techsupport']
    streamingtv = st.session_state['streamingtv']
    streamingmovies = st.session_state['streamingmovies']
    contract = st.session_state['contract']
    paperlessbilling = st.session_state['paperlessbilling']
    paymentmethod = st.session_state['paymentmethod']
    monthlycharges = st.session_state['monthlycharges']
    totalcharges = st.session_state['totalcharges']

    # Create a dataframe from the variables

    columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
               'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
               'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
               'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
               'PaymentMethod', 'MonthlyCharges', 'TotalCharges']

    data = [[gender, seniorcitizen, partner, dependents, tenure, phoneservice,
             multiplelines, internetservice, onlinesecurity, onlinebackup, deviceprotection,
             techsupport, streamingtv, streamingmovies, contract, paperlessbilling,
             paymentmethod, monthlycharges, totalcharges]]

    df = pd.DataFrame(data, columns=columns)

    # if not os.path.exists('./data/history.csv'):
    #     os.makedirs('./data')

    df.to_csv('./data/history.csv',mode='a',header=not os.path.exists('./data/history.csv'), index=False)

    # To predict with the dataframe created

    pred = pipeline.predict(df)

    prediction = int(pred[0])

    prediction = encoder.inverse_transform([prediction])

   # Create prediction probabilities

    prob = pipeline.predict_proba(df)

    #Update session state
    st.session_state['prediction'] = prediction
    st.session_state['prob'] = prob
    


    return prediction, prob

if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None
if 'prob' not in st.session_state:
    st.session_state['prob'] = None


# Create a function for the user information in a form
def user_information():
    pipeline, encoder = model_selection()  # Call this function here, so the form could have knowledge of it

    with st.form('input features'):
        col1, col3 = st.columns([1, 1])

        with col1:
            st.write('### Personal Information')
            st.selectbox('Gender', options=['Male', 'Female'], key='gender')
            st.selectbox('Partner', options=['Yes', 'No'], key='partner')
            st.number_input('Senior Citizen', min_value=0, max_value=1, step=1, key='seniorcitizen')
            st.number_input('Tenure', min_value=0, max_value=71, step=1, key='tenure')
            st.selectbox('Dependents', options=['Yes', 'No'], key='dependents')

        with col3:
            st.write('### Subscriptions')
            st.selectbox('Payment Methods', options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], key='paymentmethod')
            st.selectbox('Contract', options=['Month-to-month', 'One year', 'Two year'], key='contract')
            st.selectbox('PaperlessBilling', options=['Yes', 'No'], key='paperlessbilling')
            st.number_input('MonthlyCharges', min_value=18, max_value=118,step=5, key='monthlycharges')
            st.number_input('TotalCharges', min_value=19, max_value=8670,step=50, key='totalcharges')

        col2_1, col2_2 = st.columns(2)
        with col2_1:
            st.write('### Services')
            st.selectbox('Internet Services', options=['DSL', 'Fiber optic', 'No'], key='internetservice')
            st.selectbox('Phone Services', options=['Yes', 'No'], key='phoneservice')
            st.selectbox('MultipleLines', options=['Yes', 'No','No phone service'], key='multiplelines')
            st.selectbox('OnlineSecurity', options=['Yes', 'No','No internet service'], key='onlinesecurity')
        with col2_2:
            st.write('### Services')
            st.selectbox('OnlineBackup', options=['Yes', 'No','No internet service'], key='onlinebackup')
            st.selectbox('DeviceProtection', options=['Yes', 'No','No internet service'], key='deviceprotection')
            st.selectbox('TechSupport', options=['Yes', 'No','No internet service'], key='techsupport')
            st.selectbox('StreamingTV', options=['Yes', 'No','No internet service'], key='streamingtv')
            st.selectbox('StreamingMovies', options=['Yes', 'No','No internet service'], key='streamingmovies')

        if st.form_submit_button('Predict', on_click=get_prediction, kwargs=dict(pipeline=pipeline, encoder=encoder)):
            pass

if __name__ == "__main__":
    st.title('Get a Prediction')


    user_information()


    # Retrieve prediction and prob from the session_state
    prediction = st.session_state['prediction'] 
    prob = st.session_state['prob'] 

    if not prediction:
        st.write('### Display Prediction here')
    elif prediction =='Yes':
        prob_of_customer_churn = prob[0][1] * 100
        st.write(f'### Probability that the Customer will churn is {round(prob_of_customer_churn,2)}%')
    else:
        proba_of_customer_will_not_churn = prob[0][0] * 100
        st.write(f'### Probability that the Customer will not churn is {round(proba_of_customer_will_not_churn,2)}%')
    

    st.balloons()
    #st.markdown(f"### {final_prediction}")


    #st.write(st.session_state)



    
