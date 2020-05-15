# Imports
import pandas as pd
import matplotlib.pyplot as plt

# Data Preprocessing
data = pd.read_csv('data/covid19-global-forecasting-week-1/train.csv', parse_dates=['Date']) # Contains case and fatality data up to 18th March
predictions = pd.read_csv('data/covid19-global-forecasting-week-1/test.csv', parse_dates=['Date']) # Just contains dates for future prediction, no data actually present in the file
data.rename(columns = {'Country/Region':'Region', 'Province/State':'State', 'ConfirmedCases':'Cases'}, inplace = True)
predictions.rename(columns = {'Country/Region':'Region', 'Province/State':'State', 'ConfirmedCases':'Cases'}, inplace = True)

# Define specific region or state, set to False if desire all regions/states
region = 'Italy'
state = False

if region:
    data = data[data['Region'] == region]
if state:
    data = data[data['State'] == state]


# Remove initial tails
tail_case_cut = 5
data = data[data['Cases'] >= tail_case_cut]

# Create figure and plot space
fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(data['Date'], data['Cases'])
# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)
plt.show()
