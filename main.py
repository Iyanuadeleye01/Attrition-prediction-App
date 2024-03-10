
import streamlit as st
from login import authenticate_user, entered_cred

#Initialize session state if not already initialized
if 'user' not in st.session_state:
    st.session_state['user'] = ''
if 'pwd' not in st.session_state:
    st.session_state['pwd'] = ''

st.set_page_config(
    page_title='Home',
    page_icon='',
    layout='wide'
)

st.markdown("""<style>
            section[data-testid="stSidebar"]
            { width: 200px !important;
            }
            </style> """,
            unsafe_allow_html=True)

def main():
    entered_cred()
    if authenticate_user():
        st.title('Vodafone Customer Attrition Prediction')
        st.write('Harnessing Data Insights to Predict Customer Attrition')

        virtual_env = """
        # Activate virtual environment
        venv/scripts/activate
        streamlit run main.py
        """

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('### Attrition Meter')
            st.write("This app predicts customer churn based on demographic and service-related questions, determining whether a customer will stop using the company's services")
            
            st.markdown('### Key Features')
            st.write('- Data - Allows you access to the data in a remote database through connection')
            st.write('- Dashboard - Contains data visualization')
            st.write('- Prediction - Allows you to view prediction in real-time')
            st.write('- History - Provides you with the records of past predictions')

            st.markdown('### User Benefits')
            st.write('- Unveiling customer attrition patterns using a data-driven solution')
            st.write('- Harness the power of Machine Learning without its complexities')
            st.write('- Insightful predictions by anticipating customer churn with Precision')

        with col2:
            st.markdown('### How to run application')
            st.code(virtual_env, language='python')

            st.markdown('### Machine Learning Integration')
            st.write('- You have access to select between 2 models for prediction')
            st.write('- Simple integration and user-friendly interface')
            st.write('- Save data to a database for future use')
            st.write('- Get probability for predictions')

            st.markdown('### Need Help?')
            st.write("""
        <div>
            <p>Contact me at <a href="mailto:iyanu1106@gmail.com">iyanu1106@gmail.com</a> for collaborations &copy; 2024. All rights reserved</p>
        </div>
        """, unsafe_allow_html=True)
            
            st.markdown('<a style="color: #0366d6;" href="https://github.com/Iyanuadeleye01">Github</a>', unsafe_allow_html=True)
            
            st.markdown('<a style="color: #0366d6;" href="https://medium.com/@iyanu1106">Medium</a>', unsafe_allow_html=True)
    else:
        st.error("Please enter 'admin' as username and password to login")

if __name__ == '__main__':
    main()
 