a = []  # List for zeros
b = []  # List for even numbers
c = []  # List for odd numbers

# Taking 5 inputs one by one
num1 = int(input("Enter the first number: "))
if num1 == 0:
    a.append(num1)
elif num1 % 2 == 0:
    b.append(num1)
else:
    c.append(num1)


print("List of zeros (a):", a)
print("List of even numbers (b):", b)
print("List of odd numbers (c):", c)