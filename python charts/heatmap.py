import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/CoronaTimeSeries.csv')

# Preparing data
#this creates a heat map sectioned by rectangles
#the x-axis represents the day of the week
#the y-axis represents the week of the month
#each square represents a day of the particular week
#the intensity of the colors represent the number of cases

data = [go.Heatmap(x=df['Day'],
                   y=df['WeekofMonth'],
                   z=df['Recovered'].values.tolist(),
                   colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='Corona Virus Recovered Cases', xaxis_title="Day of Week",
                   yaxis_title="Week of Month")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')