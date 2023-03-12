import streamlit as st
import pandas as pd
from pandas.tseries.offsets import DateOffset
import statsmodels.api as sm
import pickle

# Load pre-trained model
# model = sm.load('sarima_model.h5')
model = pickle.load(open('sarima_model.pkl','rb'))


def predict_accidents(year, month):
    # Create input array for model prediction
    future_dates1 = [pd.Timestamp(year=year, month=month, day=1) + DateOffset(months=x) for x in range(0,12)]
    future_dates1=pd.DataFrame(future_dates1)
    future_dates1.set_index(0,inplace=True)

    pred_future_start_date=future_dates1.index[-12]
    pred_future_end_date=future_dates1.index[-1]
    future_dates1['forecast'] = model.predict(start = pred_future_start_date , end = pred_future_end_date)  

    return future_dates1.loc[pd.Timestamp(year=year, month=month, day=1), 'forecast']

# Create Streamlit app
st.title('Alcohol-Related Accidents Prediction for 2021')

# Add input fields for year and month
year = st.number_input('Year', value=2021, step=1)
month = st.selectbox('Month', range(1, 13))

# Call predict_accidents function with user inputs
prediction = predict_accidents(year, month)

# Display prediction result
st.write('Prediction for {}-{}: {}'.format(month, year, round(prediction)))
