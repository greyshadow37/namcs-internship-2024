import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df=pd.read_excel('preprocessed_data.xlsx')

df.describe()

q1_t = df['Temperature'].quantile(0.25)
q3_t = df['Temperature'].quantile(0.75)
iqr_t = q3_t - q1_t

print("IQR for 'Temperature':", iqr_t)


q1_h = df['Humidity'].quantile(0.25)
q3_h = df['Humidity'].quantile(0.75)
iqr_h = q3_h - q1_h

print("IQR for 'Humidity':", iqr_h)


q1_p = df['Precipitation'].quantile(0.25)
q3_p = df['Precipitation'].quantile(0.75)
iqr_p = q3_p - q1_p

print("IQR for 'Prepicitation':", iqr_p)


quartile_dict = {'humidity': (q1_h, q3_h), 'precipitation': (q1_p, q3_p), 'temperature': (q1_t, q3_t)}
iqr_dict = {'humidity': iqr_h, 'precipitation': iqr_p, 'temperature': iqr_t}


def remove_outliers_iqr(df, iqr_h, iqr_t, iqr_p):
  q1_h = df['Humidity'].quantile(0.25)
  q3_h = df['Humidity'].quantile(0.75)
  lower_bound_humidity = q1_h - 1.5 * iqr_h
  upper_bound_humidity = q3_h + 1.5 * iqr_h

  q1_t = df['Temperature'].quantile(0.25)
  q3_t = df['Temperature'].quantile(0.75)
  lower_bound_temperature = q1_t - 1.5 * iqr_t
  upper_bound_temperature = q3_t + 1.5 * iqr_t

  q1_p = df['Precipitation'].quantile(0.25)
  q3_p = df['Precipitation'].quantile(0.75)
  lower_bound_precipitation = q1_p - 1.5 * iqr_p
  upper_bound_precipitation = q3_p + 1.5 * iqr_p

  filtered_data = df[
      (df['Humidity'] >= lower_bound_humidity) &
      (df['Humidity'] <= upper_bound_humidity) &
      (df['Temperature'] >= lower_bound_temperature) &
      (df['Temperature'] <= upper_bound_temperature) &
      (df['Precipitation'] >= lower_bound_precipitation) &
      (df['Precipitation'] <= upper_bound_precipitation)
  ]

  return filtered_data


filtered_data=remove_outliers_iqr(df, iqr_h, iqr_t, iqr_p)


filtered_data.to_excel('preprocessed_data.xlsx', index=False)