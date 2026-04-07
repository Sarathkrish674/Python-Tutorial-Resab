# for i in range(5, 0, -1):
#     print(i)
# 5
# 4
# 3
# 2
# 1

# The expression for i in range(5, 0, -1): means:

# 5 (start): The loop starts at the value 5.
# 0 (stop): The loop stops before reaching 0. It does not include 0.
# -1 (step): The loop decreases by 1 after each iteration.


# for i in range(1,6):
#     print("*" * i)
# *
# **
# ***
# ****
# *****  

# for i in range(5, 0, -1):
#     print("*" * i)

# *****
# ****
# ***
# **
# *



# for i in range(1, 6):
#     print(" " * (5 - i) + "*" * i)

#     *
#    **
#   ***
#  ****
# *****

# for i in range(5,0,-1):
#     print(" " * (5 - i) + "*" * i)

# *****
#  ****
#   ***
#    **
#     *



 


# for i in range(1, 6):
#     print(" " * (5 - i) + "*" * (2 * i - 1))

#     *
#    ***
#   *****
#  *******
# *********

# for i in range(5,0,-1):
#     print(" " * (5 - i) + "*" * (2 * i - 1))

# *********
#  *******
#   ***** 
#    ***
#     *


# word1 = input("enter the first word : ")
# word2 =  input("enter the second word : ")

# # Step 1: Remove spaces and convert both strings to lowercase
# word1 = word1.lower()
# word2 = word2.lower()

# # Step 2: Check if the sorted versions of the strings are the same
# if sorted(word1) == sorted(word2):
#     print(f'"{word1}" and "{word2}" are anagrams.')
# else:
#     print(f'"{word1}" and "{word2}" are not anagrams.')


# silent   listen    are anagram 

# def is_anagram(str1, str2):
#     # Remove spaces and convert to lowercase for normalization
#     return sorted(str1.lower()) == sorted(str2.lower())

# # Taking user input
# str1 = input("Enter the first string: ")
# str2 = input("Enter the second string: ")

# # Checking and printing the result
# if is_anagram(str1, str2):
#     print(f'"{str1}" and "{str2}" are anagrams!')
# else:
#     print(f'"{str1}" and "{str2}" are not anagrams.')



# Define the decorator function, which takes another function as its input (func).
def decorator_function(func):
    # Define the inner function `wrapper`. This is the function that will be executed
    # in place of the original function passed to the decorator.
    def wrapper():
        # Code to execute before the original function.
        print("Before the function call")
        # Call the original function (func) passed to the decorator.
        func()
        # Code to execute after the original function.
        print("After the function call")
    # Return the `wrapper` function. This is what will replace the original function.
    return wrapper

# Apply the decorator to the `say_hello` function.
# This is equivalent to:
# say_hello = decorator_function(say_hello)
@decorator_function
def say_hello():
    # This is the original function that gets wrapped by the decorator.
    print("Hello!")

# Call the decorated function.
say_hello()

# When `say_hello` is called, it now points to the `wrapper` function inside the decorator.
# The following steps occur in sequence:
# 1. The wrapper function is called.
# 2. The message "Before the function call" is printed.
# 3. The original `say_hello` function (which prints "Hello!") is executed.
# 4. The message "After the function call" is printed.

# Expected Output:
# Before the function call
# Hello!
# After the function call