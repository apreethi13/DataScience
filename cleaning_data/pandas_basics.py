import pandas as pd

# Read dataset
ride_sharing = pd.read_csv('../datasets/cleaning_datasets/ride_sharing_new.csv')

# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing.dtypes)

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())

# Print Value counts
print(ride_sharing['user_type'].value_counts())
"""
Name: user_type, dtype: float64
2    12972
3     6502
1     6286
"""

# Print Count of missimg values
print(ride_sharing.isna().sum())
# --------------
# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip("minutes")

# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration
print(ride_sharing[['duration','duration_trim','duration_time']])
print(ride_sharing['duration_time'].mean())
# -------------