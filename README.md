# Time series model

This project forecasts the number of accidents that occurred in 2021 using time series analysis. The model used in this project is SARIMA, and it was trained on data from 2000 to 2018. The testing was done using data from 2019 to 2020 to evaluate the model's performance.

The project also includes a web app built using Streamlit. The app allows users to input the required parameters and generate a prediction for the number of accidents that could occur in 2021. The web app has been deployed on Heroku and can be accessed using the following link: https://accident-prediction-webapp.herokuapp.com/

The model.ipynb file contains the code for building and saving the SARIMA model.

To run the application locally, you can directly execute the main.py file using the command streamlit run main.py. 

Alternate method: The app2.py file accepts inputs in JSON format and writes the predictions to an output JSON file. 

This project is intended to provide insights into predicting the number of accidents that could occur in 2021 and to demonstrate the use of time series analysis for forecasting.
