# %% [markdown]
# # 0. Import packages

# %% [code]
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# %% [markdown]
# # 1. Loading data

# %% [code]
df = pd.read_csv("../../Datasets/pollution_us_2000_2016.csv")

# %% [markdown]
# # 2. Peek through the dataset

# %% [markdown]
# **About the data**: This dataset contains information on the four major pollutants (Nitrogen Dioxide, Sulphur Dioxide, Carbon Monoxide, and Ozone) for every day from 2000 to 2016 in the United States.

# %% [code]
df.head()

# %% [code]
# Deleting first column
df.drop('Unnamed: 0', axis = 1, inplace = True)

# %% [code]
df.shape

# %% [markdown]
# 28 columns and 1.7 milion of records.

# %% [code]
df.isna().sum()

# %% [markdown]
# Two columns have missing values. However, the percentage of data missing for each of these columns is small (around 0.5%). So there is no need to fix this.

# %% [markdown]
# Let's look at the categorical data.

# %% [code]
df.describe(include = ['object'])

# %% [markdown]
# There are 47 States, 133 Counties and 144 cities in the dataset. The NO2 Units and SO2 Units are expressed in parts per billion and O3 Units and CO Units in parts per million. 

# %% [markdown]
# Let's see the types of data.

# %% [code]
df.dtypes

# %% [markdown]
# Date Local column is an object (string). We will change the type of this column to datetime.

# %% [code]
df['Date Local']  = pd.to_datetime(df['Date Local'])

# %% [markdown]
# # 3. Visualizations

# %% [markdown]
# **a) The biggest polluters**

# %% [code]
# TOP 10 biggest polluters by mean value of AQI for Nitrogen Dioxide (NO2), Ozone (O3), Sulfur Dioxide (SO2) and Carbon Monoxide (CO) for 2000-2016

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
df_AQI_State.sort_values(by = 'NO2 AQI', ascending = False, inplace = True)
barplot1 = axs[0].bar(x, 'NO2 AQI', data=df_AQI_State[:10], label = 'NO2')
xlabels = df_AQI_State.loc[:10, 'State']
plt.sca(axs[0])
plt.xticks(x, xlabels) # x axis marks

# Plot for O3
df_AQI_State.sort_values(by = 'O3 AQI', ascending = False, inplace = True)
barplot2 = axs[1].bar(x, 'O3 AQI', data=df_AQI_State[:10], label = 'O3', color = 'red')
xlabels = df_AQI_State.loc[:10, 'State']
plt.sca(axs[1])
plt.xticks(x, xlabels) # x axis marks

# Plot for SO2
df_AQI_State.sort_values(by = 'SO2 AQI', ascending = False, inplace = True)
barplot3 = axs[2].bar(x, 'SO2 AQI', data=df_AQI_State[:10], label = 'SO2', color = 'green')
xlabels = df_AQI_State.loc[:10, 'State']
plt.sca(axs[2])
plt.xticks(x, xlabels) # x axis marks

# Plot for CO
df_AQI_State.sort_values(by = 'CO AQI', ascending = False, inplace = True)
barplot4 = axs[3].bar(x, 'CO AQI', data=df_AQI_State[:10], label = 'CO', color = 'purple')
xlabels = df_AQI_State.loc[:10, 'State']
plt.sca(axs[3])
plt.xticks(x, xlabels) # x axis marks

# change of font size on both axes
axs[0].tick_params(axis='both', which='major', labelsize=12) 
axs[1].tick_params(axis='both', which='major', labelsize=12)
axs[2].tick_params(axis='both', which='major', labelsize=12)
axs[3].tick_params(axis='both', which='major', labelsize=12)

# Adding value for each bar
i = 0
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    global i
    for rect in rects:
        height = rect.get_height()
        axs[i].annotate('{:.2f}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', size = 12)
    i = i + 1

autolabel(barplot1)
autolabel(barplot2)
autolabel(barplot3)
autolabel(barplot4)

# Space between charts
plt.subplots_adjust(hspace=0.3) 

# Adding plot titles and axis titles
axs[0].set_title('TOP 10 biggest polluters by mean value of AQI for Nitrogen Dioxide (NO2) for 2000-2016', fontsize = 14)
axs[1].set_title('TOP 10 biggest polluters by mean value of AQI for Ozone (O3) for 2000-2016', fontsize = 14)
axs[2].set_title('TOP 10 biggest polluters by mean value of AQI for Sulfur Dioxide (SO2) for 2000-2016', fontsize = 14)
axs[3].set_title('TOP 10 biggest polluters by mean value of AQI for Carbon Monoxide (CO) for 2000-2016', fontsize = 14)
fig.text(0.1, 0.5, 'Mean value of AQI', ha='center', va='center', rotation='vertical', fontsize = 14)

# %% [markdown]
# The highest average pollution level for the years 2000-2016 is for ozone and it is between 40.51 AQI and 45.36. Next is for NO2 (from 28.38 AQI to 37.99 AQI) and then for SO2 (from 12.89 AQI to 18.55 AQI). The lowest level is for CO and it is between 6.44 AQI to 17.70 AQI.
# 
# By the mean value of Ozone the biggest polluters are respectively Tennessee (45.36 AQI), North Carolina (44.38 AQI) and Kentucky (43.01 AQI). Kentucky is also one of the biggest polluters for SO2 (18.55 AQI). For NO2 the record holders are respectively: Country of Mexico (37.99 AQI), Arizona (36.11 AQI) and Colorado (35.96 AQI). Country of Mexico and Arizona are also one of the biggest polluters for CO (17.70 AQI and 9.19 AQI respectively).

# %% [markdown]
# **b) Changes in the level of pollution over time** 

# %% [code]
# Mean value of pollutants for USA in 2000-2016

# Data
df_AQI_Year = df_AQI[['Date Local', 'NO2 AQI', 'O3 AQI', 'SO2 AQI', 'CO AQI']].resample('Y', on = 'Date Local').mean()
df_AQI_Year.reset_index(inplace=True)

# Plot size
plt.rcParams["figure.figsize"] = (12, 8) 

# Adding plots
fig, ax = plt.subplots()
ax.plot('Date Local', 'NO2 AQI', data=df_AQI_Year, color = "red", label = "NO2 AQI")
ax.plot('Date Local', 'O3 AQI', data=df_AQI_Year, color = "blue", label = "O3 AQI")
ax.plot('Date Local', 'SO2 AQI', data=df_AQI_Year, color = "green", label = "SO2 AQI")
ax.plot('Date Local', 'CO AQI', data=df_AQI_Year, color = "purple", label = "CO AQI")

# Adding plot title and axis titles
plt.title('Mean value of pollutants for USA in 2000-2016', fontsize = 16)
plt.xlabel("Year", fontsize = 13)
plt.ylabel("Mean value of AQI", fontsize = 13)

# change of font size on both axes
ax.tick_params(axis='both', which='major', labelsize=11) 

# Adding legend
ax.legend()
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -.15), ncol = 6, shadow = True, fontsize = 13)

# %% [markdown]
# For all pollutants except ozone, AQI has decreased from 2000 to 2016. For ozone the level of AQI for 2016 is practically the same as in 2000.

# %% [markdown]
# **c) Choropleth maps**

# %% [markdown]
# We will create choropleth maps to show geographically the level of pollution over time.

# %% [code]
## To use plotly choropleth maps, states names must be encoded.
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# %% [markdown]
# Because Country Of Mexico and District Of Columbia are not used in choropleth maps, we will delete them.

# %% [code]
df = df[df['State']!='Country Of Mexico'] # deleting Mexico
df = df[df['State']!='District Of Columbia'] # deleting Columbia
df['State_abbrev'] = df.State.apply(lambda x: us_state_abbrev[x])

# %% [code]
# Calculating annual mean value of pollutants for every State
df_AQI = df[['State_abbrev', 'Date Local', 'NO2 AQI', 'O3 AQI', 'SO2 AQI', 'CO AQI']]
df_AQI_State_Year = df_AQI.groupby('State_abbrev').resample('Y', on = 'Date Local').mean()
df_AQI_State_Year.reset_index(inplace = True)
df_AQI_State_Year

# %% [code]
# Adding column coresponding to the year of Date Local column
df_AQI_State_Year['Year'] = df_AQI_State_Year['Date Local'].dt.year
# Sorting values by Date Local (for animated choropleth presented below)
df_AQI_State_Year.sort_values(by = 'Date Local', inplace = True)

# %% [code]
# Plotly choropleth showing AQI for Nitrogen Dioxide changes from 2000 to 2016
fig_NO2 = px.choropleth(df_AQI_State_Year,
              locations = 'State_abbrev',
              animation_frame="Year", # showing changes through the years
              color='NO2 AQI',
              # Creating fixed scale (the same as defined by EPA)
              color_continuous_scale = [(0.00, "green"),   (0.1, "green"),
                                        (0.1, "yellow"), (0.2, "yellow"),
                                        (0.2, "orange"),  (0.3, "orange"),
                                        (0.3, "red"),  (0.4, "red"),
                                        (0.4, "purple"),  (0.6, "purple"),
                                        (0.6, "maroon"),  (1.00, "maroon"),
                                        ],
              range_color = (0, 500),
              locationmode='USA-states',
              scope="usa",
              title='Mean values of Air Quality Index (AQI) per year for Nitrogen Dioxide (NO2)',
              height=600,
             )

# Modifying legend 
fig_NO2.update_layout(coloraxis_colorbar=dict(
    title="Air Quality Index (AQI)",
    ticks="outside", 
    dtick=50
))

# %% [code]
# Plotly choropleth showing AQI for Ozone changes from 2000 to 2016
fig_O3 = px.choropleth(df_AQI_State_Year,
              locations = 'State_abbrev',
              animation_frame="Year", # showing changes through the years
              color='O3 AQI',
              # Creating fixed scale (the same as defined by EPA)
              color_continuous_scale = [(0.00, "green"),   (0.1, "green"),
                                        (0.1, "yellow"), (0.2, "yellow"),
                                        (0.2, "orange"),  (0.3, "orange"),
                                        (0.3, "red"),  (0.4, "red"),
                                        (0.4, "purple"),  (0.6, "purple"),
                                        (0.6, "maroon"),  (1.00, "maroon"),
                                        ],
              range_color = (0, 500),
              locationmode='USA-states',
              scope="usa",
              title='Mean values of Air Quality Index (AQI) per year for Ozone (O3)',
              height=600,
             )

# Modifying legend 
fig_O3.update_layout(coloraxis_colorbar=dict(
    title="Air Quality Index (AQI)",
    ticks="outside", 
    dtick=50
))

# %% [code]
# Plotly choropleth showing AQI for Sulfur Dioxide changes from 2000 to 2016
fig_SO2 = px.choropleth(df_AQI_State_Year,
              locations = 'State_abbrev',
              animation_frame="Year", # showing changes through the years
              color='SO2 AQI',
              # Creating fixed scale (the same as defined by EPA)
              color_continuous_scale = [(0.00, "green"),   (0.1, "green"),
                                        (0.1, "yellow"), (0.2, "yellow"),
                                        (0.2, "orange"),  (0.3, "orange"),
                                        (0.3, "red"),  (0.4, "red"),
                                        (0.4, "purple"),  (0.6, "purple"),
                                        (0.6, "maroon"),  (1.00, "maroon"),
                                        ],
              range_color = (0, 500),
              locationmode='USA-states',
              scope="usa",
              title='Mean values of Air Quality Index (AQI) per year for Sulfur Dioxide (SO2)',
              height=600,
             )

# Modifying legend 
fig_SO2.update_layout(coloraxis_colorbar=dict(
    title="Air Quality Index (AQI)",
    ticks="outside", 
    dtick=50
))

# %% [code]
# Plotly choropleth showing AQI for Carbon Monoxide changes from 2000 to 2016
fig_CO = px.choropleth(df_AQI_State_Year,
              locations = 'State_abbrev',
              animation_frame="Year", # showing changes through the years
              color='CO AQI',
              # Creating fixed scale (the same as defined by EPA)
              color_continuous_scale = [(0.00, "green"),   (0.1, "green"),
                                        (0.1, "yellow"), (0.2, "yellow"),
                                        (0.2, "orange"),  (0.3, "orange"),
                                        (0.3, "red"),  (0.4, "red"),
                                        (0.4, "purple"),  (0.6, "purple"),
                                        (0.6, "maroon"),  (1.00, "maroon"),
                                        ],
              range_color = (0, 500),
              locationmode='USA-states',
              scope="usa",
              title='Mean values of Air Quality Index (AQI) per year for Carbon Monoxide (CO)',
              height=600,
             )

# Modifying legend 
fig_CO.update_layout(coloraxis_colorbar=dict(
    title="Air Quality Index (AQI)",
    ticks="outside", 
    dtick=50
))

# %% [markdown]
# The annual average level of AQI for all pollutants exept ozone has never exceeded 50, which means that for NO2, SO2 and CO the air quality condidions are good (green color). For ozone AQI has been between 50 and 100 in years 2000-2006 (except 2004) and in 2012. The worst was 2002 and 2005 with 3 States above 50 AQI.
# 
# Let's look at the data for 2005 for July. It is expected that in the summer months the level of Ozone should be higher.

# %% [code]
# Calculating daily mean value of pollutants for every State
df_AQI_State_Month = df_AQI.groupby('State_abbrev').resample('D', on = 'Date Local').mean()
df_AQI_State_Month.reset_index(inplace = True)

# Adding columns coresponding to the day, month and year of Date Local column
df_AQI_State_Month['Day'] = df_AQI_State_Month['Date Local'].dt.day
df_AQI_State_Month['Month'] = df_AQI_State_Month['Date Local'].dt.month
df_AQI_State_Month['Year'] = df_AQI_State_Month['Date Local'].dt.year

# Data for July in 2005
df_AQI_State_2005_July = df_AQI_State_Month[(df_AQI_State_Month['Year'] == 2005) & (df_AQI_State_Month['Month'] == 7)]

# Sorting values by Date Local (for animated choropleth presented below)
df_AQI_State_2005_July.sort_values(by = 'Date Local', inplace = True)

# %% [code]
# Plotly choropleth showing AQI for Ozone changes for July 2005
fig_O3_v2 = px.choropleth(df_AQI_State_2005_July,
              locations = 'State_abbrev',
              animation_frame="Day", # showing changes through the days
              color='O3 AQI',
              # Creating fixed scale (the same as defined by EPA)
              color_continuous_scale = [(0.00, "green"),   (0.1, "green"),
                                        (0.1, "yellow"), (0.2, "yellow"),
                                        (0.2, "orange"),  (0.3, "orange"),
                                        (0.3, "red"),  (0.4, "red"),
                                        (0.4, "purple"),  (0.6, "purple"),
                                        (0.6, "maroon"),  (1.00, "maroon"),
                                        ],
              range_color = (0, 500),
              locationmode='USA-states',
              scope="usa",
              title='Mean values of Air Quality Index (AQI) per day for Ozone (O3) for July 2005',
              height=600,
             )

# Modifying legend 
fig_O3_v2.update_layout(coloraxis_colorbar=dict(
    title="Air Quality Index (AQI)",
    ticks="outside", 
    dtick=50
))

# %% [markdown] As expected the level of AQI for Ozone has reached good air quality conditions (green color). In some
# cases it has exceeded 100 AQI (air quality conditions are unhealthy for sensitive groups) and even 150 AQI (air
# quality conditions are unhealthy).