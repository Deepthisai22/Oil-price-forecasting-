# app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load your historical oil price data (replace with your actual data)
df3 = pd.read_csv(r'C:\Users\Admin\Desktop\Dataset Oil price daily1.csv')

# Assuming p=1, d=1, q=1 (replace with your chosen order)
model = ARIMA(df3['Price'], order=(1, 1, 1))
model_fit = model.fit()

# Forecast the next 30 days
forecast_steps = 30
forecast = model_fit.forecast(steps=forecast_steps)

# Streamlit app
st.title("Oil Price Forecasting")
st.write("Using ARIMA model")

# Plot the forecast
plt.figure(figsize=(10, 6))
plt.plot(df3.index, df3['Price'], label='Historical Prices', color='blue')
plt.plot(pd.date_range(start=df3.index[-1], periods=forecast_steps + 1, closed='right'), forecast, label='Forecast', color='red')
#plt.fill_between(pd.date_range(start=df3.index[-1], periods=forecast_steps + 1, closed='right'), forecast - stderr, forecast + stderr, color='gray', alpha=0.3)
plt.xlabel('Date')
plt.ylabel('Oil Price')
plt.title('Oil Price Forecast')
plt.legend()
st.pyplot(plt)

# Display forecast values
st.write("Forecasted Prices:")
st.write(forecast)
