import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# this sorts the top 20 countries based on gold medals won
df = df.sort_values(by=['Gold'], ascending=[False]).head(20).reset_index()

# Preparing data
#this sorts each country with how many gold medals they have won
#prepares a stacked bar chart with gold, silver, and bronze
trace1 = go.Bar(x=df['NOC'], y=df['Gold'], name='Gold', marker={'color': '#CD7F32'})
trace2 = go.Bar(x=df['NOC'], y=df['Silver'], name='Silver', marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=df['NOC'], y=df['Bronze'], name='Bronze', marker={'color': '#FFD700'})
data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title='Number of medals won by each country', xaxis_title="Country",
                   yaxis_title="Number of Medals", barmode='stack')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')