import streamlit as st
import pandas as pd
import plotly.express as px
import pyodbc
import altair as alt
from login import authenticate_user, entered_cred


st.set_page_config(
    page_title='Dashboard',
    page_icon='',
    layout='wide'
)

st.markdown( """ <style>
            section[data-testid="stSidebar"]
            { width: 200px !important;
            }
            </style> """,
            unsafe_allow_html=True,
)

def dashboard_page_content():
    entered_cred()
    if authenticate_user():

        st.title('VODAFONE ATTRITION DASHBOARD')


        #df = all_feature_selection()

        #st.write(df)

        df = pd.read_csv('./data/streamlitdata.csv')

        # Creaate a select box for the user
        select_col, vis_col = st.columns([1,3])
        display_vis = select_col.selectbox(
            " Select Chart",
            ["KPI", "EDA"])

        # Seniorcitizen churn rate
        senior_citizen = df[df.SeniorCitizen == True]
        churn_by_seniorcitizen = senior_citizen['Churn'].value_counts(normalize=True)*100
        churn_by_seniorcitizen = churn_by_seniorcitizen.reset_index()

        # How payment method affects churn rate
        churn_by_payment = df.groupby('PaymentMethod').value_counts(normalize=True).unstack()
        churned_by_payment = churn_by_payment[True]
        churn_by_payment.reset_index(inplace=True)

        # Effect of Internet Service on customer churn
        # internet_service = df.groupby('InternetService')['Churn'].value_counts(normalize=True)
        # fibre_optic_effect = round(internet_service.loc['Fibre optic','No'] *100,2)
        # dsl_effect =  round(internet_service.loc['DSL', True] *100,2)

        # Effect of contract payment on customer churn
        contract_effect = df.groupby('Contract')['Churn'].value_counts().unstack()

        # Convert monthlycharges and totalcharges to numeric
        df.MonthlyCharges = pd.to_numeric(df['MonthlyCharges'], errors='coerce')
        df.TotalCharges = pd.to_numeric(df['TotalCharges'], errors='coerce')

        numerical_col = ['TotalCharges','MonthlyCharges','tenure']
        numerical_data = df[numerical_col]


        # Create columns on the dashboard page
        col1,col2 = st.columns(2)
        if display_vis == 'KPI':
            with col1:
                fig1 = px.bar(churn_by_seniorcitizen, x='Churn', y='proportion', color='Churn',
                            labels={'proportion': 'percentage(%)', 'Churn': 'Churn'},
                            title='Customer Churn Rate by SeniorCitizen')
                st.plotly_chart(fig1, use_container_width=True)

                fig2 = px.bar(churn_by_payment.reset_index(), x='PaymentMethod', y=True, color='PaymentMethod',
                    title='Churn Percentage by Payment Method', barmode='group')
                fig2.update_layout(xaxis_title='Payment Method', yaxis_title='Churn Percentage', showlegend=False)

                st.plotly_chart(fig2, use_container_width=True)

            with col2:
                container = st.container()
            with container:
                average_tenure = df['tenure'].mean()
                st.markdown('###### Average Tenure')
                st.markdown(f'#### {"{:,.2f}".format(average_tenure)}')

                average_Monthlycharges = df['MonthlyCharges'].mean()
                st.markdown('###### Average MonthlyCharges')
                st.markdown(f'#### {"{:,.2f}".format(average_Monthlycharges)}')

                total_charges = df.groupby(['TotalCharges'])['Churn'].mean()

                fig3 = px.bar(contract_effect, x=contract_effect.index, y=True,
                        labels={'x': 'Contract Duration', 'y': 'Churn Rate'},
                        title='Churn Rate by Contract Duration')
                st.plotly_chart(fig3, use_container_width=True)


        elif  display_vis == 'EDA':
            with col1:
                fig4 = px.histogram(df, x='TotalCharges', nbins=20, title='TotalCharges Distribution') 
                st.plotly_chart(fig4, use_container_width=True)  

                numeric_df = df.apply(pd.to_numeric, errors='coerce')

                # Calculate the correlation matrix
                corr_matrix = numeric_df.corr()

                # Create the heatmap
                fig5 = px.imshow(corr_matrix, labels=dict(x="Variables", y="Variables", color="Correlation"),
                                x=corr_matrix.columns, y=corr_matrix.columns, color_continuous_scale='Viridis')

                # Update layout
                fig5.update_layout(
                    title='Correlation Heatmap',
                    width=800,
                    height=700
                )

                # Display the heatmap in the Streamlit app
                st.plotly_chart(fig5, use_container_width=True)


                    # Using Altair
                gender_chart = alt.Chart(df).mark_bar().encode(
                    x=alt.X('gender', title='Gender'),
                    y=alt.Y('count()', title='Count'),
                    color='Churn:N'
                ).properties(
                    title="Churn Distribution by Gender (Altair)"
                )
                st.altair_chart(gender_chart, use_container_width=True)



            with col2:

                #  Relationship between total charges and churn
               
                charges_churn_scatter = alt.Chart(df).mark_circle(size=60).encode(
                    x='TotalCharges',
                    y='Churn',
                    color='Churn:N',
                    tooltip=['TotalCharges', 'Churn']
                ).properties(
                    title="Relationship between TotalCharges and Churn"
                ).interactive()
                st.altair_chart(charges_churn_scatter, use_container_width=True)

                # Create a boxplot to show the distribution of customer tenure in the company
                fig = px.histogram(df, x='tenure', nbins=20)
                fig.update_layout(title='Customer Tenure Distribution')
                st.plotly_chart(fig, use_container_width=True)

                # Create a scstter_matrix to shhow the relationship among the numerical features

                data = df[['Churn', 'MonthlyCharges', 'TotalCharges', 'tenure']]

                # Define custom colors for 'True' and 'False' in 'Churn' column
                colors = {True: 'blue', False: 'orange'}

                # Create a scatter matrix plot
                fig6 = px.scatter_matrix(data, dimensions=['MonthlyCharges', 'TotalCharges', 'tenure'], 
                                        color='Churn', color_discrete_map=colors)

                # Update layout
                fig6.update_layout(
                    height=800,
                    width=1200,
                    title='Pairwise Relationships'
                )

                # Display the plot in the Streamlit app
                st.plotly_chart(fig6, use_container_width=True)
    else:
        st.error("Please enter 'admin' as username and password to login")
if __name__ == '__main__':
    dashboard_page_content()

