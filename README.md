# Attrition-prediction-App
This project aims to create an attrition prediction application using Streamlit
 
The Attrition Prediction App is an interactive Streamlit application designed to predict customer churn based on provided data. This README provides comprehensive instructions on creating, deploying, and using the app.
 
### Table of Contents
1. [Setup](#setup)
2. [Running the App](#running-the-app)
3. [Usage](#usage)
    - [Home Page](#home-page)
    - [Login Page](#login-page)
    - [Data Page](#data-page)
    - [Predictor Page](#predictor-page)
    - [Dashboard Page](#dashboard-page)
    - [History Page](#history-page)
4. [Models Used](#models-used)
5. [Deployment](#deployment)
6. [Further Development](#further-development)
7. [Contributing](#contributing)
8. [License](#license)
 
### Setup <a name="setup"></a>
 
1. **Clone Repository**: Clone the repository containing the Streamlit app code.
2. **Install Dependencies**: Install the required dependencies using pip.
3. **Data Setup**: Ensure you have a CSV dataset named `streamlitdata.csv` placed inside a folder named `data` in the project directory.
4. **Configuration**: Update the `login.py` file with necessary credentials and configuration details.
 
### Running the App <a name="running-the-app"></a>
 
To run the app locally, execute the following command in the project directory:
 
```bash
streamlit run main.py
```
 
The app will start running locally and can be accessed through a web browser.
 
### Usage <a name="usage"></a>
 
#### Home Page <a name="home-page"></a>
- Provides an overview of the app and its purpose.
 
#### Login Page <a name="login-page"></a>
- Existing and new Users: Enter a default username and password to log in, which is 'admin' for both.
- 
 
#### Data Page <a name="data-page"></a>
- Displays basic information about the dataset.
- Shows the All features(Categorical and Numerical Features).
- Shows Numerical Features only.
- Displays Categorical Features only.
 
#### Predictor Page <a name="predictor-page"></a>
- Batch Prediction: Upload a CSV dataset containing customer information to predict churn.
- Online Prediction: Input customer details interactively to predict churn.
 
#### Dashboard Page <a name="dashboard-page"></a>
- Provides visualizations and analytics related to customer churn.
- Includes research questions and key performance indicators.
- Offers insights through various charts and plots.
 
#### History Page <a name="history-page"></a>
- Tracks user interactions with the app.
- Displays a history log of actions performed by the user.
- Allows navigating back to previous points in history.
 
### Models Used <a name="models-used"></a>
 
#### Supported Models
1. Logistic Regression 
2. Random Forest
 
#### Description
- Logistic Regression:  logistic regression is used for binary classification tasks, where the output variable is categorical and has only two possible outcomes. It estimates the probability that a given input belongs to a certain class. It works by fitting a logistic curve to the data, which allows it to model the relationship between the input variables and the probability of the output being in a particular class.
- Random Forest: is an ensemble learning method that uses multiple decision trees to improve the accuracy of the model. It creates a "forest" of decision trees during training and makes predictions by averaging the predictions of each individual tree.
 
#### Model Training
- Data Preprocessing
- Pipeline Creation
- Model Training
- Evaluation
 
#### Model Selection
- User Choice
- Performance Comparison
 
### Deployment <a name="deployment"></a>
 
- Model Serialization
- Model Loading
 
### Further Development <a name="further-development"></a>
 
- Model Tuning
- Model Expansion
- Model Monitoring
 
### Contributing <a name="contributing"></a>
 
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or create a pull request.
 
### License <a name="license"></a>
 
This project is licensed under the [Apache 2.0](LICENSE). Feel free to use, modify, and distribute the code for personal and commercial purposes.