import pandas as pd
import datetime as dt

# Read dataset
ride_sharing = pd.read_csv('../datasets/cleaning_datasets/ride_sharing_new.csv')

# --------------------------------------------------------------------------------------------------------------------
# The number of rides taken has increased by 20% overnight,
# leading you to think there might be both complete and incomplete duplicates in the ride_sharing DataFrame.
# --------------------------------------------------------------------------------------------------------------------

# Find duplicates
duplicates = ride_sharing.duplicated('ride_id', keep=False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values(by = 'ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])

# ------------------------------------------------------------------------------------------------------
# Dropping Duplicates by merging the datasets
# by first dropping complete duplicates, and then merging the incomplete duplicate rows into
# one while keeping the average
# ------------------------------------------------------------------------------------------------------
# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates()

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby(by = 'ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset = 'ride_id', keep = False)
duplicated_rides = ride_unique[duplicates == True]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0