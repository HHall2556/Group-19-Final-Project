import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as pyo
import plotly.tools as tls
import plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot

df = pd.read_csv('../Datasets/pollution_us_2000_2016.csv')
df.head()

nodf = df[
    ['Address', 'State', 'County', 'City', 'Date Local', 'NO2 Units', 'NO2 Mean', 'NO2 1st Max Value', 'NO2 1st Max '
                                                                                                       'Hour',
     'NO2 AQI']]

nodf.head()

nodf = nodf.groupby(['Address', 'State', 'County', 'City', 'Date Local']).mean().reset_index()
nodf.head()

nodf['State'].unique()

nodf = nodf[nodf['State'] != 'Country Of Mexico']

totalTuples = nodf.count()['State']

# totalTuples
# add year and month columns
tempYear = []
tempMonth = []
for i in range(totalTuples):
    delement = (nodf['Date Local'].iloc[i]).split('-')
    tempYear.append(int(delement[0]))
    tempMonth.append(delement[0] + '-' + delement[1])
nodf['Year'] = tempYear
nodf['Month'] = tempMonth
nodf.head()

stateData = {}
addrlabel = []
acountlabel = []
for i in nodf['State'].unique():
    # create a dicionary of data frames for state-wise record
    stateData[i] = nodf[nodf['State'] == i]
    addrlabel.append(i)
    acountlabel.append(stateData[i]['Address'].nunique())
aCountdf = pd.DataFrame(addrlabel, columns=['State'])
aCountdf['Address Count'] = acountlabel
aCountdf.head

mapData = nodf[(nodf['Month'] >= '2014-12') & (nodf['Month'] <= '2015-11')]

# winterdf = pd.concat([mapData[mapData['Month'] == '2014-12'],mapData[mapData['Month'] == '2015-01'],mapData[mapData['Month'] == '2015-02']])[['State','CO Mean']].groupby('State').mean().reset_index().sort_values('State')
# springdf = pd.concat([mapData[mapData['Month'] == '2015-03'],mapData[mapData['Month'] == '2015-04'],mapData[mapData['Month'] == '2015-05']])[['State','CO Mean']].groupby('State').mean().reset_index().sort_values('State')
# summerdf = pd.concat([mapData[mapData['Month'] == '2015-06'],mapData[mapData['Month'] == '2015-07'],mapData[mapData['Month'] == '2015-08']])[['State','CO Mean']].groupby('State').mean().reset_index().sort_values('State')
# autumndf = pd.concat([mapData[mapData['Month'] == '2015-09'],mapData[mapData['Month'] == '2015-10'],mapData[mapData['Month'] == '2015-11']])[['State','CO Mean']].groupby('State').mean().reset_index().sort_values('State')


fullyeardf = mapData[mapData['Month'].isin(['2015-01', '2015-02', '2015-03', '2015-04', '2015-05', '2015-06',
                                            '2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12'])].groupby(
    'State').mean().reset_index().sort_values('State')
winterdf = mapData[mapData['Month'].isin(['2014-12', '2015-01', '2015-02'])].groupby(
    'State').mean().reset_index().sort_values('State')
springdf = mapData[mapData['Month'].isin(['2015-03', '2015-04', '2015-05'])].groupby(
    'State').mean().reset_index().sort_values('State')
summerdf = mapData[mapData['Month'].isin(['2015-06', '2015-07', '2015-08'])].groupby(
    'State').mean().reset_index().sort_values('State')
autumndf = mapData[mapData['Month'].isin(['2015-09', '2015-10', '2015-11'])].groupby(
    'State').mean().reset_index().sort_values('State')

# abbDF = pd.read_html('https://www.50states.com/abbreviations.htm')[0]
# above line gives URLError. However, works on local notebook.
# extracted values by
# adict = abbDF.to_dict()
# abbState = list(adict[0].values())
# abbAB = list(adict[1].values())

abbState = ['US State:', 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
            'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
            'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
            'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',
            'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
            'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',
            'Wisconsin', 'Wyoming', 'Commonwealth/Territory:', 'American Samoa', 'District Of Columbia',
            'Federated States of Micronesia', 'Guam', 'Marshall Islands', 'Northern Mariana Islands', 'Palau',
            'Puerto Rico', 'Virgin Islands', 'Military "State":', 'Armed Forces Africa', 'Armed Forces Americas',
            'Armed Forces Canada', 'Armed Forces Europe', 'Armed Forces Middle East', 'Armed Forces Pacific']
abbAB = ['Abbreviation:', 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA',
         'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
         'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY',
         'Abbreviation:', 'AS', 'DC', 'FM', 'GU', 'MH', 'MP', 'PW', 'PR', 'VI', 'Abbreviation:', 'AE', 'AA', 'AE', 'AE',
         'AE', 'AP']
abbDF = pd.DataFrame([abbState, abbAB]).transpose()

# small correction, so things go smooth ahead
abbDF.iloc[53][0] = 'District Of Columbia'

mapA = []
mapS = []
for i in fullyeardf.index:
    mapA.append(str(fullyeardf['NO2 Mean'].iloc[i])[:5] + ' ppm')
    mapS.append(abbDF[abbDF[0] == fullyeardf['State'].iloc[i]][1].values[0])
fullyeardf['text'] = mapA
fullyeardf['code'] = mapS

mapA = []
mapS = []
for i in winterdf.index:
    mapA.append(str(winterdf['NO2 Mean'].iloc[i])[:5] + ' ppm')
    mapS.append(abbDF[abbDF[0] == winterdf['State'].iloc[i]][1].values[0])
winterdf['text'] = mapA
winterdf['code'] = mapS


mapA = []
mapS = []
for i in springdf.index:
    mapA.append(str(springdf['NO2 Mean'].iloc[i])[:5] + ' ppm')
    mapS.append(abbDF[abbDF[0] == springdf['State'].iloc[i]][1].values[0])
springdf['text'] = mapA
springdf['code'] = mapS

mapA = []
mapS = []
for i in summerdf.index:
    mapA.append(str(summerdf['NO2 Mean'].iloc[i])[:5] + ' ppm')
    mapS.append(abbDF[abbDF[0] == summerdf['State'].iloc[i]][1].values[0])
summerdf['text'] = mapA
summerdf['code'] = mapS

mapA = []
mapS = []
for i in autumndf.index:
    mapA.append(str(autumndf['NO2 Mean'].iloc[i])[:5] + ' ppm')
    mapS.append(abbDF[abbDF[0] == autumndf['State'].iloc[i]][1].values[0])
autumndf['text'] = mapA
autumndf['code'] = mapS

data = dict(type='choropleth',
            colorscale='reds',
            locations=fullyeardf['code'],
            z=fullyeardf['NO2 Mean'],
            locationmode='USA-states',
            text=fullyeardf['text'],
            marker=dict(line=dict(color='rgb(255,255,255)', width=2)),
            colorbar={'title': "NO2 Mean in ppm"}
            )
layout = dict(title='NO2 Mean Value in 2015 by State',
              geo=dict(scope='usa',
                       showlakes=True,
                       lakecolor='rgb(85,173,240)')
              )
choromap = go.Figure(data=[data], layout=layout)
pyo.plot(choromap, filename='NO2_Map.html')
