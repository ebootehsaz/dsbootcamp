# Work on the Brooklyn Pedestrian Dataset: https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD

# 1)Filter the data to include only weekdays (Monday to Friday) and plot a line graph showing the pedestrian counts for each day of the week.

# 2) Track pedestrian counts on the Brooklyn Bridge for the year 2019 and analyze how different weather conditions influence pedestrian activity in that year. Sort the pedestrian count data by weather summary to identify any correlations( with a correlation matrix) between weather patterns and pedestrian counts for the selected year.

# 3) Implement a custom function to categorize time of day into morning, afternoon, evening, and night, and create a new column in the DataFrame to store these categories. Use this new column to analyze pedestrian activity patterns throughout the day.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def get_brooklyn_pedestrian_data():
    url = 'https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD'
    df = pd.read_csv(url)
    return df

def q1():
    df = get_brooklyn_pedestrian_data()
    # print(df.dtypes)
    # print(df['hour_beginning'])
    df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
    df['hour'] = df['hour_beginning'].dt.hour
    df['month'] = df['hour_beginning'].dt.month
    df['date'] = df['hour_beginning'].dt.date
    df['day_name'] = df['hour_beginning'].dt.day_name()
    # 1)Filter the data to include only weekdays (Monday to Friday) 
    df = df[(df['day_name'] != 'Saturday') & (df['day_name'] != 'Sunday')]
    # and plot a line graph showing the pedestrian counts for each day of the week.
    df = df.groupby('day_name')['Pedestrians'].sum()
    df.plot(kind='line')
    plt.show()

# ['hour_beginning', 'location', 'Pedestrians', 'Towards Manhattan', 'Towards Brooklyn', 
# 'weather_summary', 'temperature', 'precipitation', 'lat', 'long', 'events', 'Location1', 'hour', 'month', 'date', 'day_name'],
def q2():
    df = get_brooklyn_pedestrian_data()
    df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
    df['hour'] = df['hour_beginning'].dt.hour
    df['month'] = df['hour_beginning'].dt.month
    df['date'] = df['hour_beginning'].dt.date
    df['day_name'] = df['hour_beginning'].dt.day_name()
    
    # Filter data for the year 2019 and Brooklyn Bridge
    df = df[(df['hour_beginning'] >= pd.Timestamp('2019-01-01')) & (df['hour_beginning'] <= pd.Timestamp('2019-12-31'))]
    df = df[(df['location'] == 'Brooklyn Bridge')]

    # Select relevant columns
    df = df[['Pedestrians', 'temperature', 'precipitation']]

    # Compute and print the correlation matrix
    print(df.corr())

def q3():
    # Implement a custom function to categorize time of day into morning, afternoon, evening, and night, and create a new column in the DataFrame to store these categories. Use this new column to analyze pedestrian activity patterns throughout the day.
    df = get_brooklyn_pedestrian_data()
    df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
    df['hour'] = df['hour_beginning'].dt.hour
    df['month'] = df['hour_beginning'].dt.month
    df['date'] = df['hour_beginning'].dt.date
    df['day_name'] = df['hour_beginning'].dt.day_name()

    def categorize_time_of_day(hour):
        if hour < 12:
            return 'morning'
        elif hour < 17:
            return 'afternoon'
        elif hour < 21:
            return 'evening'
        else:
            return 'night'
        
    df['time_of_day'] = df['hour'].apply(categorize_time_of_day)
    pedestrian_activity = df.groupby('time_of_day')['Pedestrians'].sum()

    # Plotting the pedestrian activity
    pedestrian_activity.plot(kind='bar')
    plt.xlabel('Time of Day')
    plt.ylabel('Total Pedestrians')
    plt.title('Pedestrian Activity Patterns Throughout the Day')
    plt.show()

q1()
q2()
q3()

    