import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/CoronaTimeSeries.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Preparing data
#this creates a multi line graph
#each line corresponds to a different type of statistic (death, recovered, or unrecovered)
#the x-axis represents the data from Jan 1, 2020, to Mar 15, 2020
#the y-axis represents the number of cases, each interval separated by 10,000

trace1 = go.Scatter(x=df['Date'], y=df['Death'], mode='lines', name='Death')
trace2 = go.Scatter(x=df['Date'], y=df['Recovered'], mode='lines', name='Recovered')
trace3 = go.Scatter(x=df['Date'], y=df['Unrecovered'], mode='lines', name='Unrecovered')
data = [trace1,trace2,trace3]


# Preparing layout
layout = go.Layout(title='Corona Virus Death and Recovered Cases From 2020-01-22 to 2020-03-17', xaxis_title="Date",
                   yaxis_title="Number of cases")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart.html')