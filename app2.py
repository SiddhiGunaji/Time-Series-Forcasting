import pandas as pd
from pandas.tseries.offsets import DateOffset
import statsmodels.api as sm

# Load pre-trained model
model = sm.load('sarima_model.h5')


def predict_accidents(year, month):
    # Create input array for model prediction
    future_dates1 = [pd.Timestamp(year=year, month=month, day=1) + DateOffset(months=x) for x in range(0,12)]
    future_dates1=pd.DataFrame(future_dates1)
    future_dates1.set_index(0,inplace=True)

    pred_future_start_date=future_dates1.index[-12]
    pred_future_end_date=future_dates1.index[-1]
    future_dates1['forecast'] = model.predict(start = pred_future_start_date , end = pred_future_end_date)  

    return future_dates1.loc[pd.Timestamp(year=year, month=month, day=1), 'forecast']


import json

# Read input from input.json
with open('input.json', 'r') as f:
    input_data = json.load(f)

# Make prediction
prediction = predict_accidents(input_data['year'], input_data['month'])

# Write output to output.json
with open('output.json', 'w') as f:
    json.dump({'prediction': prediction}, f)


