"""
Spencer Lefever
COSC311 Lab 2
"""

import pandas as pd # our main priority here
import numpy as np  # just in case, but also comes along with pandas
from matplotlib import pyplot as plt # for plotting

bejaia_data = pd.read_csv('Bejaia_Region.csv')
sidi_data = pd.read_csv('Sidi-Bel_Abbes_Region.csv')

#Task 1
print('Bejaia Region Info\n',bejaia_data.info())
print('\nSidi-Bel Abbes Region Info\n', sidi_data.info())
print('\nBejaia Region Data\n', bejaia_data.describe())
print('\nSidi-Bel Abbes Region Data\n', sidi_data.describe())
print('\nBejaia Unique Windspeed\n', bejaia_data['Ws'].unique())
print('\nSidi-Bel Abbes Unique Windspeed\n', sidi_data['Ws'].unique())
print('\nBejaia Count\n', bejaia_data.count())
print('\nSidi-Bel Abbes Count\n', sidi_data.count())

#Task 2
plt.plot(bejaia_data['Temperature'], marker='o', linestyle='solid')
plt.title('Temperature Over Time in Bejaia')
plt.ylabel('Temperature')
plt.xlabel('Day')
plt.show()

#Task 3
plt.scatter(sidi_data['Temperature'], sidi_data['FWI'])
plt.title('Temperature vs. Fire Weather Index in Sidi-Bel Abbes')
plt.xlabel('Temperature')
plt.ylabel('Fire Weather Index')
plt.show()

#Task 4
rh = bejaia_data['RH'].groupby(bejaia_data['month']).apply(lambda x: x.values.tolist()).to_dict()
rh_avg = {key: sum(rh[key])/len(rh[key]) for key in rh.keys()}
plt.bar(rh_avg.keys(), rh_avg.values())
plt.xlabel('Month')
plt.ylabel('Avg Relative Humidity')
plt.axis([5.5,9.5,50,75])
plt.xticks([i for i in range(6,10)])
plt.title('Avg Relative Humidity by Month in Bajaia')
plt.show()

#Task 5
rain = bejaia_data['Rain'].groupby(bejaia_data['month']).apply(lambda x: x.values.tolist()).to_dict()
max_rain = {key: max(rain[key]) for key in rain.keys()}
plt.bar(max_rain.keys(), max_rain.values())
plt.xlabel('Month')
plt.ylabel('Max Rainfall')
plt.axis([5.5,9.5,0, 20])
plt.xticks([i for i in range(6,10)])
plt.title('Max Rainfall by Month in Bejaia')
plt.show()

#Task 6
sidi_june = sidi_data[(sidi_data['month'] == 6)]
plt.hist(sidi_june['Ws'], bins=5, edgecolor=(0,0,0))
plt.xlabel('Wind Speed')
plt.ylabel('Frequency')
plt.title('Wind Speed Frequency in Sidi-Bel Abbes for June')
plt.show()

#Task 7
sidi_july = sidi_data[(sidi_data['month'] == 7)]
plt.plot(sidi_july['day'], sidi_july['Temperature'], marker='o', label='Temperature')
plt.plot(sidi_july['day'], sidi_july['RH'], marker='o', label='Relative Humidity')
plt.legend()
plt.xlabel('Time')
plt.title('Temperature and Relative Humidity Over Time in Sidi-Bel Abbes in July 2012')
plt.show()

#Task 8
plt.hist(bejaia_data['RH'], edgecolor=(0,0,0))
plt.axis([40,100, 0, 30])
plt.xlabel('Relative Humidity')
plt.ylabel('Number of Days')
plt.title('Frequency of Relative Humidity is Bejaia Region')
plt.show()

#Task 9
temp = bejaia_data[['Temperature', 'month', 'Classes']]
temp_fire = temp[temp['Classes'] == 'fire   '].groupby(['month'], as_index=False).mean()
temp_no_fire = temp[temp['Classes'] == 'not fire   '].groupby(['month'], as_index=False).mean()
plt.bar(temp_fire['month']-0.125, temp_fire['Temperature'], 0.25, label='Fire')
plt.bar(temp_no_fire['month']+0.125, temp_no_fire['Temperature'], 0.25, label='No Fire')
plt.axis([5, 10, 25, 35])
plt.legend()
plt.xlabel('Month')
plt.ylabel('Avg Temp')
plt.title('Average Temperature by Month for Fires and No Fires')
plt.show()