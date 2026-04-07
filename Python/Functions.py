# ================================
# PYTHON FUNCTIONS - EXAMPLES FILE
# ================================

# A function is a reusable block of code that performs a specific task.
# Syntax:
# def function_name(parameters):
#     code
#     return value
# function function_name(parameters):
#     code 
#     return value

# A parameter is the variable written in the function definition.

# An argument is the actual value passed to the function when calling it.
# -------------------------------------------------
# 1. Adding an item to a list (Mutable object)
# -------------------------------------------------

def item_to_list(my_list, item):
    my_list.append(item)


# List creation
my_list = [1,2,3,4,5,6,7]

# Function call
item_to_list(my_list,8)

print(f"Updated List:{my_list}")


 

# -------------------------------------------------
# 2. Function returning a value
# -------------------------------------------------

def add_numbers(a, b):
    """
    Function Name: add_numbers
    Parameters:
    a -> first number
    b -> second number

    return sends the result back to the caller
    """
    return a + b


result = add_numbers(5, 10)

print(f"Sum:{result}")




def a_square(a):
    """
    Function Name: add_numbers
    Parameters:
    a -> first number

    return sends the result back to the caller
    """
    return a * a


result = a_square(5)

print(f"Sum:{result}")






# -------------------------------------------------
# 3. Check Even or Odd
# -------------------------------------------------

def check_even_odd(num):
    """
    Function Name: check_even_odd
    Parameter:
    num -> number to check

    % operator gives the remainder.
    """
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


result = check_even_odd(7)

print(f"Number is:{result}")


# -------------------------------------------------
# 4. Find Largest Number
# -------------------------------------------------

def find_largest(a, b, c):
    """
    Function Name: find_largest
    Parameters:
    a, b, c -> three numbers

    max() returns the largest value
    """
    return max(a, b, c)


largest = find_largest(10, 20, 15)

print("Largest number:", largest)


# -------------------------------------------------
# 5. Reverse a String
# -------------------------------------------------

def reverse_string(s):
    """
    Function Name: reverse_string
    Parameter:
    s -> string to reverse

    [::-1] is Python slicing used to reverse a string
    """
    return s[::-1]

a = reverse_string("hello")

print(f"Reversed string:{a}" )


# -------------------------------------------------
# 6. Sum of List
# -------------------------------------------------

def sum_list(numbers):
    """
    Function Name: sum_list
    Parameter:
    numbers -> list of numbers

    sum() adds all elements in the list
    """
    return sum(numbers)


my_numbers = [1, 2, 3, 4, 5]

a = sum_list(my_numbers)

print("Sum of list:", a)







# -------------------------------------------------
# 7. Palindrome Check
# -------------------------------------------------

def is_palindrome(s):
    """
    Function Name: is_palindrome
    Parameter:
    s -> string

    A palindrome reads the same forward and backward
    """
    return s == s[::-1]


print("Is 'madam' palindrome?", is_palindrome("madam"))
print("Is 'hello' palindrome?", is_palindrome("hello"))



#    OR


def is_palindrome(s):
    """
    Function Name: is_palindrome
    Parameter:
    s -> string

    A palindrome reads the same forward and backward
    """
    return s == s[::-1]

a = is_palindrome("madam")

b = is_palindrome("hello")



print("Is 'madam' palindrome?",a )
print("Is 'hello' palindrome?",b)



# s == s[::-1]    madam  == madam 

# s == s[::-1]   hello   == olleh


# -------------------------------------------------
# 8. Anagram Check
# -------------------------------------------------

def is_anagram(str1, str2):
    """
    Function Name: is_anagram
    Parameters:
    str1 -> first word
    str2 -> second word

    Anagram means same letters in different order.
    sorted() arranges characters alphabetically.
    lower() makes comparison case-insensitive.
    """
    return sorted(str1.lower()) == sorted(str2.lower())

# ==	Compares the two sorted lists.
# sorted()	Converts the string into a list of characters sorted alphabetically
# .lower()	Normalizes the strings.

print("listen & silent:", is_anagram("listen", "silent"))
print("hello & world:", is_anagram("hello", "world"))



            # OR

def is_anagram(str1, str2):
    """
    Function Name: is_anagram
    Parameters:
    str1 -> first word
    str2 -> second word

    Anagram means same letters in different order.
    sorted() arranges characters alphabetically.
    lower() makes comparison case-insensitive.
    """
    return sorted(str1.lower()) == sorted(str2.lower())

a = is_anagram("listen", "silent")

b = is_anagram("hello", "world")

print("listen & silent:", a)
print("hello & world:", b)


# -------------------------------------------------
# 9. Anagram Check with User Input
# -------------------------------------------------

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if is_anagram(str1, str2):
    print(f'"{str1}" and "{str2}" are anagrams!')
else:
    print(f'"{str1}" and "{str2}" are not anagrams.')


# -------------------------------------------------
# 10. Print vs Return
# -------------------------------------------------

def add_and_print(a, b):
    """
    This function prints the result but does not return it.
    """
    print("Printed sum:", a + b)


add_and_print(3, 5)


def add(a, b):
    """
    This function returns the result so it can be stored or reused.
    """
    return a + b


result = add(3, 5)

print("Returned sum:", result)


# =========================================
# PYTHON FUNCTION - PARAMETER & ARGUMENT
# =========================================

# Question:
# Write a Python function that adds two numbers
# and returns the result.


# -----------------------------------------
# Step 1: Define the function
# -----------------------------------------

def add_numbers(a, b):
    """
    Function Name: add_numbers

    Parameters:
    a -> first number
    b -> second number

    Parameter Meaning:
    A parameter is a variable defined in the function
    that receives a value when the function is called.
    """

    # Step 2: Perform the calculation
    result = a + b

    # Step 3: Return the result
    return result


# -----------------------------------------
# Step 4: Call the function
# -----------------------------------------

# Here we pass values to the function.
# These values are called ARGUMENTS.

result = add_numbers(5, 10)

"""
Argument Meaning:
An argument is the actual value passed to the function
when calling it.

Example here:
5  -> argument for parameter 'a'
10 -> argument for parameter 'b'
"""


# -----------------------------------------
# Step 5: Print the result
# -----------------------------------------

print("The sum is:", result)


# -----------------------------------------
# Final Explanation Summary
# -----------------------------------------

"""
Function:
A reusable block of code that performs a task.

Parameter:
Variable inside the function definition.

Example:
def add_numbers(a, b)
                ↑  ↑
           parameters

Argument:
Actual value passed to the function.

Example:
def add_numbers(5, 10)
            ↑  ↑
         arguments
"""

# The sum is: 15

# -------------------------------------------------
# END OF FILE
# -------------------------------------------------