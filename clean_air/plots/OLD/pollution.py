import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/pollution_us_2000_2016.csv')

# Remove duplicate date entries
filtered_df = filtered_df.groupby(['Address', 'State', 'County', 'City', 'Date Local']).mean().reset_index()
filtered_df.head()

# Creating sum of number of cases group by State Column
new_df = filtered_df.groupby(['State'])['O3 Mean'].sum().reset_index()

# Preparing data
data = [go.Bar(x=new_df['State'], y=new_df['O3 Mean'])]

# Preparing layout
layout = go.Layout(title='O3 by State', xaxis_title="States",
                   yaxis_title="O3")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='O3_barchart.html')
