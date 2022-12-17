import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

working_month = ['january', 'febuary', 'march', 'april', 'may','june']
months= ['january', 'febuary', 'march', 'april', 'may',                     'june','july','august','september','october','november','december']

day_of_week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
##### TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please enter the city you would like to analyze ! \n').lower()
    while (city != 'chicago' and city != 'new york city' and city !='washington'):
        print("we don't have data on {} yet !".format(city))
        city = input("Please choose one of the following cities: chicago,new york city,washington \n")
       
#####TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please enter the month that you would like to analyze ! \n').lower()

    if month != 'all':
      while True:
        try:
            temp=working_month.index(month) + 1
        except  ValueError as ve:
        # Not a valid value
            try:
                temp2=months.index(month) + 1
                print("We don't have any data to the selected month please choose another month :")
                month = input('Please enter a valid month to analyze ! \n')
            except  ValueError as ve2:
                print(f'You entered {month},not a valid month .')
                month = input('Please enter a valid month to analyze ! \n')
        else:
        # No error; stop the loop
            break

#####TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter the day that you would like to analyze ! \n').lower()
    if day != 'all':

        while True:
            try:
                print(f'day {day} is {day_of_week.index(day) + 1}')
            except  ValueError as ve:
            # Not a valid value
                print(f'You entered {day},not a valid day .')
                day = input('Please enter a valid day to analyze ! \n')
            else:
            # No error; stop the loop
                break
    print("you entered the city: {} in month: {} and day: {}".format(city,month,day))
        
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
    # loads the file of the required city
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']== month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']== day.title()]
    return df
    
   
def time_stats(df):
    
    
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    ##### TO DO: display the most common month
    if(df['month'].nunique()>1):
        popular_month = df['month'].mode()[0]
        
        print('Most common Month:', months[popular_month])
        ##### TO DO: display the most common day of week
    if(df['day_of_week'].nunique()>1):
            popular_day_of_week = df['day_of_week'].mode()[0]
            print ('Most common day of the week :', popular_day_of_week) 

     ##### TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] =df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('Most common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
        
        
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

##### TO DO: display most commonly used start station

    Start_Station_count = df['Start Station'].value_counts()
    head_S_station = Start_Station_count.head(1)
    most_used_SS = head_S_station.index[0]
    print('The most commonly used start station is: {}'.format(most_used_SS))
        
##### TO DO: display most commonly used end station
    End_Station_count = df['End Station'].value_counts()
    head_E_station = End_Station_count.head(1)
    most_used_ES = head_E_station.index[0]
    print('The most commonly used End station is: {}'.format(most_used_ES))

##### TO DO: display most frequent combination of start station and end station trip

    Station_combo = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most frequent comination of start station and end station is {} as start station and {} as end station'.format(Station_combo[0],Station_combo[1]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

##### TO DO: display total travel time
    Trip_Duration_total = df['Trip Duration'].sum()
    print('Total trip duration is: {}'.format(Trip_Duration_total))

##### TO DO: display mean travel time
    Trip_Duration_avg = df['Trip Duration'].mean()
    print('average trip duration is: {}'.format(Trip_Duration_avg))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

##### TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

##### TO DO: Display counts of gender
    try:
        Gender= df['Gender'].value_counts()
        print(Gender)
    except KeyError as KE:
        print("washington doesn't save a gender column or birth year column in the data available")
        return
##### TO DO: Display earliest, most recent, and most common year of birth
       
    earliest_Birth_year= df['Birth Year'].min()
    print("The earliest birth year is: {}".format(earliest_Birth_year))
    # most recent year of birth 
    recent_Birth_year = df['Birth Year'].max()
    print("The most recent birth year is: {}".format(recent_Birth_year))
    #most common year of birth 
    common_Birth_Year= df['Birth Year'].value_counts()
    head_Common = common_Birth_Year.head(1)
    most_common = head_Common.index[0]
    
    print('the most common birth year is: {}'.format(head_Common.index[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_disp(city):
    counter=0
    prompt='yes'
    while(prompt=='yes'):
        df=pd.read_csv(CITY_DATA[city], skiprows = counter, nrows=5)
        print(df)
        counter+=6
        prompt=input('\nWould you like to display the next set of raw data ? Enter yes or no.\n') 
    
    print('-'*40)

    
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data = input('\nWould you like to display raw data ? Enter yes or no.\n') 
        if raw_data.lower() == 'yes':
            raw_data_disp(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
