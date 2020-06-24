import pandas as pd
import datetime as dt

# Read dataset
ride_sharing = pd.read_csv('../datasets/cleaning_datasets/ride_sharing_new.csv')

#--
# ire_sizes column has the correct range by first converting it to an integer,
# then setting and testing the new upper limit of 27″ for tire sizes.

# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())

#--

#---
#A bug was discovered which was relaying rides taken today as taken next year.
# Convert ride_date to datetime
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date'])

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())
#---