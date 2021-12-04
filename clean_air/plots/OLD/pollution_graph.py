import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/pollution_us_2000_2016.csv')

# Removing empty spaces from State column to avoid errors
filtered_df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by State Column
new_df = filtered_df.groupby(['State'])['NO2 Mean'].sum().reset_index()

# Preparing data
data = [go.Bar(x=new_df['State'], y=new_df['NO2 Mean'])]

# Preparing layout
layout = go.Layout(title='NO2 Air Quality Index by State', xaxis_title="States",
                   yaxis_title="NO2 Mean")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='no2_mean_barchart.html')



#Original Code
# Filtering US Cases
#filtered_df = df[df['Country'] == 'US']

# Sorting values and select first 20 states
#new_df = new_df.sort_values(by=['Confirmed'], ascending=[False]).head(20)