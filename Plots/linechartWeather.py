import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')


# Preparing data
#this creates a line graph
#the y-axis corresponds to the max temperature of each month
#the x-axis corresponds to the month of the year
data = [go.Scatter(x=df['month'], y=df['actual_max_temp'], mode='lines', name='Max Temp')]

# Preparing layout
# create a line chart layout for the max temp for each month
layout = go.Layout(title='Max Temperature for each country for each month', xaxis_title="Month",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechartWeather.html')