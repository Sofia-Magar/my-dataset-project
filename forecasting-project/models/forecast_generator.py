import pandas as pd
from prophet import Prophet

# Load dataset
df = pd.read_csv("../datasets/dataset_pcs.csv")

# Prepare data for Prophet
df_prophet = df[['period', 'qty_total']].copy()
df_prophet = df_prophet.rename(columns={'period': 'ds', 'qty_total': 'y'})
df_prophet['ds'] = pd.to_datetime(df_prophet['ds'], errors='coerce')
df_prophet = df_prophet.dropna()

# Create and fit the model
model = Prophet()
model.fit(df_prophet)

# Generate forecast for 30 days
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Save results to CSV
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv("../results/forecast.csv", index=False)
print("✅ Forecast saved to forecast.csv")