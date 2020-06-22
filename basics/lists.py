# Example 1
# Create the areas list1
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])
# ans: 11.25

# Print out last element from areas
print(areas[-1])
# ans: 9.5

# Print out the area of the living room
print(areas[5])
# ans : 20.0

# my_list[start:end] - start index will be included, while the end index is not
downstairs = areas[0:6]
# ans = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0]

# Use slicing to create upstairs
upstairs = areas[-4:]
# ans = ["bedroom", 10.75, "bathroom", 9.50]

# Copying a list
area_copy1 = areas[:]
area_copy2 = list(areas)
# ans = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Example 2
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)
# ans = [20.0, 18.0, 11.25, 10.75, 9.5]