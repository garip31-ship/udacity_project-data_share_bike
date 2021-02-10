#! /usr/bin/python
#from datetime import timedelta
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter"""

    print('\nHello! Let\'s explore some US bikeshare data!') # TO DO: get user input for city(chicago, new york city, washington).HINT:Use a while loop to handle invalid inputs


    while True:
      city = input("\nWhich city would you like to filter? Washington, New York City, or Chicago?\n")
      if city not in ('New York City', 'Chicago', 'Washington'):
        print("Sorry, I didn't get this. Could You Please Try Again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nWhich month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n")
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("Sorry, I didn't catch that. Try again.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nAre you looking for a particular day? If so, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n")
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("Sorry, I didn't catch that. Try again.")
        continue
      else:
        break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        
        # use index of month list to get corresponding int
        MONTH_DATA = ['January', 'February', 'March', 'April', 'May', 'June']
        month = MONTH_DATA.index(month)+1

        # filter by month to create new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

# look_up dictionary 
    look_up = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
        '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}

    # display the most common month
    popular_month = df['month'].mode()[0]
    month_in_string = look_up[str(popular_month)]
    print("1. The most common month was: ", month_in_string)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("2. The most common day of the week was: {}".format(popular_day))

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('3. The most common start hour was:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    Start_Station = df['Start Station'].mode()[0]
    print("Most Commonly used start station : " + Start_Station)

    #display most commonly used end station
    End_Station = df['End Station'].mode()[0]
    print("Most Commonly used end station : " + End_Station)

    #display most frequent combination of start station and end station trip
    Combination_Station = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("Most Commonly used combination of start station and end station trip : " + str( Combination_Station.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    #display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print("Total travel time : " + str(Total_Travel_Time))

    #display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print("Mean travel time : " + str(Mean_Travel_Time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    ###################### TO DO: Display counts of user types ############################

    user_types = df['User Type'].value_counts()

    print('User Types:\n', user_types) #print(user_types)

    ####################### TO DO: Display counts of gender ###############################

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    ####################### TO DO: Display earliest, most recent, and most common year of birth ########################

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds to calculate." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
    """Displays raw data on user request."""
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nDo you want to view next 5 row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

        #MAIN FUNCTION
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