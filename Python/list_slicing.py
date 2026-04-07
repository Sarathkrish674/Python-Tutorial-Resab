numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# index    0   1   2    3   4   5   6   7   8    9

# list[start:end:step]

# Slicing examples
print("Original list:", numbers)

# 1. Slice from index 2 to 5 (excluding 5)
print("Slice from index 2 to 5:", numbers[2:5])  # Output: [30, 40, 50]

# 2. Slice from the beginning to index 4 (excluding 4)
print("Slice from start to index 4:", numbers[:4])  # Output: [10, 20, 30, 40]
# left to the number given inside the [] bracket -1

# 3. Slice from index 5 to the end
print("Slice from index 5 to end:", numbers[5:])  # Output: [60, 70, 80, 90, 100]
# Right to the number till the end

# 4. Slice the entire list
print("Entire list :", numbers[:])  # Output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]




numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# index    0   1   2    3   4   5   6   7   8    9

# list[start:end:step]

# 5. Slice with a step (every 2nd element)
print("Every 2nd element:", numbers[::2])  # Output: [10, 30, 50, 70, 90]

# 6. Reverse the list using slicing
print("Reversed list:", numbers[::-1])  # Output: [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]


# Define the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slicing to pick every second element from the start to the end
print(numbers[::2])  # [start:end:step]
# Explanation:
# - start: not provided, so it starts from index 0 (beginning of the list).
# - end: not provided, so it goes until the end of the list.
# - step: 2, so it skips one element and picks every second element.
# Steps:
#   numbers[0] = 1
#   numbers[2] = 3
#   numbers[4] = 5
#   numbers[6] = 7
#   numbers[8] = 9
# Output: [1, 3, 5, 7, 9]

# Slicing to pick every second element, but in reverse order
print(numbers[::-2])  # [start:end:step]
# Explanation:
# - start: not provided, so it starts from the last element of the list.
# - end: not provided, so it goes until the first element of the list.
# - step: -2, so it moves backward and picks every second element.
# Steps:
#   numbers[9] = 10
#   numbers[7] = 8
#   numbers[5] = 6
#   numbers[3] = 4
#   numbers[1] = 2
# Output: [10, 8, 6, 4, 2]