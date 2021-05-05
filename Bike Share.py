# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:50:47 2021

@author: Compu Tech
"""


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'E:\\chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'E:\\washington.csv' }
city='chicago'
month = 'all'
day = 'all'
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while(True):
        city = input('please enter the city: ').lower()
        if(city=='chicago' or city=='new york city' or city=='washington'):
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    
    while(True):
        month = input('please enter the month: ')
        if(month=='all' or month=='january' or month=='february' or month=='march' or month=='april' or month=='may' or month=='june'):
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while(True):
        day = input('please enter the day: ')
        if(day=='all' or day=='saturday' or day=='sunday' or day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday'):
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    print("load data function")
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    #df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('the most common month is: ',common_month)
    # TO DO: display the most common day of week
    #df['day'] = df['Start Time'].dt.day_name()
    common_day = df['day'].mode()[0]
    print('the most common day is: ',common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('the most common hour is: ', common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('the most common used start station: ', common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('the most common used end station: ', common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    common_combination_stations = df.groupby(['Start Station', 'End Station'])
    print('the most frequent combination of start and end stations: ', common_combination_stations)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time: ', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print('the counts of user types: ', counts_user_types)
    # TO DO: Display counts of gender
    if city=="washington":
        print("washington csv file does not have gender coulmn")
    else:
        counts_of_gender = df['Gender'].value_counts()
        print('counts of gender: ', counts_of_gender)
    # TO DO: Display earliest, most recent, and most common year of birth
    if city=="washington":
        print("washington csv file does not have birth day coulmn")
    else:
        earliest_year = df['Birth Year'].min()
        print('the earliest year of birth: ', earliest_year)
        most_recent = df['Birth Year'].max()
        print('the most recent year of birth: ', most_recent)
        most_common_year = df['Birth Year'].mode()[0]
        print('the most common year of birth', most_common_year)
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data=='yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


