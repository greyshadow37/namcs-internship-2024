import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df=pd.read_excel('preprocessed_data.xlsx')

df.head()

x=df['Temperature']
plt.figure(figsize=(10,6))
sns.histplot(x,bins=10,kde=False)
plt.xlabel('temperature')
plt.ylabel('frequency')
plt.title('temperature frequency')

sns.boxplot(x='WeatherCondition',y='Temperature',data=df)
plt.title("boxplot")
plt.show()

x=df['Temperature']
y=df['Precipitation']
plt.scatter(x,y,color='black',marker="x")
plt.xlabel("temperature")
plt.ylabel("precipitation")
plt.title("temerature vs precipitation")
plt.show()

x=df['Temperature']
y=df['Humidity']
plt.scatter(x,y,color='black',marker="x")
plt.xlabel("temperature")
plt.ylabel("humidity")
plt.title("temerature vs humidity")
plt.show()

x=df['Precipitation']
y=df['Humidity']
plt.scatter(x,y,color='black',marker="x")
plt.xlabel("precipitation")
plt.ylabel("humidity")
plt.title("precipitatin vs humidity")
plt.show()

