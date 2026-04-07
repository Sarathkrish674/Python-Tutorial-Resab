numbers = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]

# index    0    1   2    3   4   5   6   7    8     9

# Write a slicing statement to print the first 4 elements of the list.
print(f"First 4 elements in the list is:{numbers[:4]}")

# Write a slicing statement to print the last 3 elements of the list.
print(f"Last 3 elements in the list is:{numbers[7:]}")

# Extract the elements from index 2 to index 6 using slicing.
print(f"Slice the index from 2 to 6 is:{numbers[2:7]}")

# Print all elements except the first two using slicing.
print(f"Elements using slicing is:={numbers[2:]}")