import pandas as pd

# Симуляція прогнозу на 30 днів
data = {
    'ds': pd.date_range(start='2025-04-02', periods=30),
    'yhat': [120 + i*0.5 for i in range(30)],
    'yhat_lower': [115 + i*0.4 for i in range(30)],
    'yhat_upper': [125 + i*0.6 for i in range(30)]
}

forecast = pd.DataFrame(data)
forecast.to_csv("forecast.csv", index=False)
forecast.head()
