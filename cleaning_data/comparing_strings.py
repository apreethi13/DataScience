import pandas as pd
import recordlinkage

# Import Process from fuzzywuzzy
from fuzzywuzzy import process


def main():

    restaurants_df = pd.read_csv('../datasets/cleaning_datasets/restaurants_L2.csv')
    restaurants_new_df = pd.read_csv('../datasets/cleaning_datasets/restaurants_L2_dirty.csv')

    # rename columns
    restaurants_df.rename(columns={'type': 'cuisine_type'}, inplace=True)
    restaurants_new_df.rename(columns={'type': 'cuisine_type'}, inplace=True)

    # Find similarity score for 'asian', 'american', and 'italian'
    get_matching_cuisine_scores(restaurants_df)

    # Find matches with similarity score > 80
    find_matching_cuisine_score_80(restaurants_df)

    # Create Rrecord Linkage
    create_record_linkage(restaurants_df, restaurants_new_df)

def get_matching_cuisine_scores(restaurants):

    # Store the unique values of cuisine_type in unique_types
    unique_types = restaurants['cuisine_type'].unique()

    # Calculate similarity of 'asian' to all values of unique_types
    print(process.extract('asian', unique_types, limit=len(unique_types)))

    # Calculate similarity of 'american' to all values of unique_types
    print(process.extract('american', unique_types, limit=len(unique_types)))

    # Calculate similarity of 'italian' to all values of unique_types
    print(process.extract('italian', unique_types, limit=len(unique_types)))


def find_matching_cuisine_score_80(restaurants):
    categories = ['asian', 'american', 'italian']

    # For each correct cuisine_type in categories
    for cuisine in categories:
        # Find matches in cuisine_type of restaurants
        matches = process.extract(cuisine, restaurants['cuisine_type'],
                                  limit=restaurants.shape[0])

        # For each possible_match with similarity score >= 80
        for possible_match in matches:
            if possible_match[1] >= 80:
                # Find matching cuisine type
                matching_cuisine = restaurants['cuisine_type'] == possible_match[0]
                restaurants.loc[matching_cuisine, 'cuisine_type'] = cuisine

    # Print unique values to confirm mapping
    print(restaurants['cuisine_type'].unique())


def create_record_linkage(restaurants, restaurants_new):
    # Create an indexer and object and find possible pairs
    indexer =  recordlinkage.Index()

    # Block pairing on cuisine_type
    indexer.block('cuisine_type')

    # Generate pairs
    pairs = indexer.index(restaurants, restaurants_new)

    # Create a comparison object
    comp_cl = recordlinkage.Compare()

    # Find exact matches on city, cuisine_types
    comp_cl.exact('city', 'city', label='city')
    comp_cl.exact('cuisine_type', 'cuisine_type', label='cuisine_type')

    # Find similar matches of rest_name
    comp_cl.string('name', 'name', label='name', threshold=0.8)

    # Get potential matches and print
    potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
    print(potential_matches)

    # Isolate potential matches with row sum >=3
    matches = potential_matches[potential_matches.sum(axis=1) >= 3]

    # Get values of second column index of matches
    matching_indices = matches.index.get_level_values(1)

    # Subset restaurants_new based on non-duplicate values
    non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]

    # Append non_dup to restaurants
    full_restaurants = restaurants.append(non_dup)
    print(full_restaurants)

if __name__ == "__main__":
    main()