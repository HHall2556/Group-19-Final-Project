import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of gold group by Country Column
df = df.sort_values(by=['Gold'], ascending=[False]).head(20).reset_index()

# Preparing data
#this sorts each country with how many gold medals they have won
trace1 = go.Bar(x=df['NOC'], y=df['Gold'], name='Gold', marker={'color': '#CD7F32'})
data = [trace1]

# Preparing layout
layout = go.Layout(title='Number of gold medals won by the top 20 countries', xaxis_title="Country",
                   yaxis_title="Gold medals", barmode='stack')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')