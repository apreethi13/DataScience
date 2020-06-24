import pandas as pd
import numpy as np

# Read the csv file
airlines = pd.read_csv('../datasets/cleaning_datasets/airlines_final.csv')
categories = pd.read_csv('../datasets/cleaning_datasets/airline_categories.csv')

print(airlines.columns.tolist())
# --------------------------------------------------------------------------------------------------------------------
# Print unique values of the survey columns
# --------------------------------------------------------------------------------------------------------------------
print(categories)

# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")
print('Safety: ', airlines['safety'].unique(), "\n")
print('Satisfaction: ', airlines['satisfaction'].unique(), "\n")

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Print rows with consistent categories only
print(airlines[~cat_clean_rows])

# --------------------------------------------------------------------------------------------------------------------
# Print unique values and categorize in bins
# --------------------------------------------------------------------------------------------------------------------
# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges,
                                labels = label_names)

# Create mappings and replace
mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday',
            'Thursday': 'weekday', 'Friday': 'weekday',
            'Saturday': 'weekend', 'Sunday': 'weekend'}

airlines['day_week'] = airlines['day'].replace(mappings)
print(airlines.head())

# --------------------------------------------------------------------------------------------------------------------
# Cleaning Text Data by removing "Dr.", "Mr.", "Miss" and "Ms."
# --------------------------------------------------------------------------------------------------------------------
# Replace "Dr." with empty string ""
# airlines['full_name'] = airlines['full_name'].str.replace("Dr.","")
#
# # Replace "Mr." with empty string ""
# airlines['full_name'] = airlines['full_name'].str.replace("Mr.","")
#
# # Replace "Miss" with empty string ""
# airlines['full_name'] = airlines['full_name'].str.replace("Miss","")
#
# # Replace "Ms." with empty string ""
# airlines['full_name'] = airlines['full_name'].str.replace("Ms.","")
#
# # Assert that full_name has no honorifics
# assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False

# --------------------------------------------------------------------------------------------------------------------
# Isolate the responses with a character count higher than 40 ,
# and make sure your new DataFrame contains responses with 40 characters or more using an assert statement.
# --------------------------------------------------------------------------------------------------------------------

# Store length of each row in survey_response column
# resp_length = airlines['survey_response'].str.len()
#
# # Find rows in airlines where resp_length > 40
# airlines_survey = airlines[resp_length > 40]
#
# # Assert minimum survey_response length is > 40
# assert airlines_survey['survey_response'].str.len().min() > 40
#
# # Print new survey_response column
# print(airlines_survey['survey_response'])