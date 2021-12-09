import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import mpld3

df = pd.read_csv("../Datasets/pollution_us_2000_2016.csv")
df.head()
# Deleting first column
df.drop('Unnamed: 0', axis=1, inplace=True)
df.shape
df.isna().sum()
df.describe(include=['object'])
df.dtypes
df['Date Local'] = pd.to_datetime(df['Date Local'])
df = df[df['State'] != 'Country Of Mexico']

# TOP 10 biggest polluters by mean value of AQI for Nitrogen Dioxide (NO2), Ozone (O3), Sulfur Dioxide (SO2) and
# Carbon Monoxide (CO) for 2000-2016

# Calculating mean value of pollutants for every State
df_AQI = df[['State', 'Date Local', 'NO2 AQI', 'O3 AQI', 'SO2 AQI', 'CO AQI']]
df_AQI_State = df_AQI.groupby('State').mean()
df_AQI_State.reset_index(inplace=True)

# Charts size
plt.rcParams["figure.figsize"] = (20, 15)

# Creating x variable for 10 biggest polluters
x = np.arange(10)

# Adding four charts
fig, axs = plt.subplots(4, 1)

# Plot for NO2
df_AQI_State.sort_values(by='NO2 AQI', ascending=False, inplace=True)
barplot1 = axs[0].bar(x, 'NO2 AQI', data=df_AQI_State[:10], label='NO2')
xlabels = df_AQI_State.loc[:10, 'State']
plt.sca(axs[0])
plt.xticks(x, xlabels)  # x axis marks

# Plot for O3
df_AQI_State.sort_values(by='O3 AQI', ascending=False, inplace=True)
barplot2 = axs[1].bar(x, 'O3 AQI', data=df_AQI_State[:10], label='O3', color='red')
xlabels = df_AQI_State.loc[:10, 'State']
plt.sca(axs[1])
plt.xticks(x, xlabels)  # x axis marks

# Plot for SO2
df_AQI_State.sort_values(by='SO2 AQI', ascending=False, inplace=True)
barplot3 = axs[2].bar(x, 'SO2 AQI', data=df_AQI_State[:10], label='SO2', color='green')
xlabels = df_AQI_State.loc[:10, 'State']
plt.sca(axs[2])
plt.xticks(x, xlabels)  # x axis marks

# Plot for CO
df_AQI_State.sort_values(by='CO AQI', ascending=False, inplace=True)
barplot4 = axs[3].bar(x, 'CO AQI', data=df_AQI_State[:10], label='CO', color='purple')
xlabels = df_AQI_State.loc[:10, 'State']
plt.sca(axs[3])
plt.xticks(x, xlabels)  # x axis marks

# change of font size on both axes
axs[0].tick_params(axis='both', which='major', labelsize=12)
axs[1].tick_params(axis='both', which='major', labelsize=12)
axs[2].tick_params(axis='both', which='major', labelsize=12)
axs[3].tick_params(axis='both', which='major', labelsize=12)

# Adding value for each bar
i = 0


# Space between charts
plt.subplots_adjust(hspace=0.3)

# Adding plot titles and axis titles
axs[0].set_title('TOP 10 biggest polluters by mean value of AQI for Nitrogen Dioxide (NO2) for 2000-2016', fontsize=14)
axs[1].set_title('TOP 10 biggest polluters by mean value of AQI for Ozone (O3) for 2000-2016', fontsize=14)
axs[2].set_title('TOP 10 biggest polluters by mean value of AQI for Sulfur Dioxide (SO2) for 2000-2016', fontsize=14)
axs[3].set_title('TOP 10 biggest polluters by mean value of AQI for Carbon Monoxide (CO) for 2000-2016', fontsize=14)
fig.text(0.1, 0.5, 'Mean value of AQI', ha='center', va='center', rotation='vertical', fontsize=14)

mpld3.show()