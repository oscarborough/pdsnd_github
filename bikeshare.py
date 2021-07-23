import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    """gets user input for city. The loop will stop the user when entering an invalid month until they enter a valid city"""

    cities = ['chicago', 'new york city', 'washington']
    while True:
        try:
            city = input("Specify city name (chicago, new york city, or washington): ").lower()
            if city in cities:
                break;
            else:
                print("Please enter a valid city")
        except:
            continue

    """gets user input for month. The loop will stop the user when entering an invalid month until they enter a valid month"""

    months = ['all', '1', '2', '3', '4', '5', '6']
    while True:
        try:
            month = input('Specify month (all, 1=january, 2=february, ... , 6=june): ').lower()
            if month in months:
                break;
            else:
                print("Please enter a valid month")
        except:
            continue

    """gets user input for day. The loop will stop the user when entering an invalid month until they enter a valid day"""

    days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while True:
        try:
            day = input('Specify day sunday, monday, ..., saturday: ').lower()
            if day in days:
                break;
            else:
                print("Please enter a valid day")
        except:
            continue

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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    """displays most common month (using mode)"""

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Common Start Month: ', popular_month)

    """displays most common day (using mode)"""

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.weekday_name
    popular_day = df['day'].mode()[0]
    print('Most Common Start Day: ', popular_day)

    """displays most common hour (using mode)"""

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    """displays most common start station (using mode)"""

    start_station = df['Start Station'].mode()[0]
    print('Most common start station: ', start_station)

    """displays most common end station (using mode)"""

    end_station = df['End Station'].mode()[0]
    print('Most common end station: ', end_station)

    """displays most common combination of stations"""

    combined_station = df['Start Station'] + df['End Station']
    print('most frequent combination of stations: {}'.format(combined_station.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    """displays total travel time (using sum)"""

    total_trip_time = df['Trip Duration'].sum()
    print('total trip duration (in seconds): ', total_trip_time)

    """displays average travel time"""

    average_trip_time = df['Trip Duration'].mean()
    print('average trip duration (in seconds): ', average_trip_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    """displays totals by each user type"""

    user_types = df['User Type'].value_counts()
    print('user type count: ', user_types)

    """displays totals by each gender. If the city is Washington, then the user will be notified that the data is not available"""

    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('Gender count: ', gender)
    else:
        print('Gender count: gender data not available')

    """displays earliest, most recent, and most common birth dates. If the city is Washington, then the user will be notified that the data is not available"""

    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print('earliest birth year: ', earliest_birth_year)
    else:
        print('earliest birth year: birth year data not available')

    if 'Birth Year' in df.columns:
        latest_birth_year = df['Birth Year'].max()
        print('most recent birth year: ', latest_birth_year)
    else:
        print('most recent birth year: birth year data not available')

    if 'Birth Year' in df.columns:
        common_birth_year = df['Birth Year'].mode()[0]
        print('most common birth year: ', common_birth_year)
    else:
        print('most common birth year: birth year data not available')

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

    """prompts the user to see raw data if wanted. It will add 5 more rows until the user says "no""""

        first_row = 0
        last_row = 5
        while True:
            viewData = input('Would you like to see 5 (more) rows of raw data? Yes/No: ')
            if viewData.lower() == 'yes':
                print(df[df.columns[0:]].iloc[first_row:last_row])
                last_row += 5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
