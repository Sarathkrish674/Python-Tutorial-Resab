# Write a Python program for a simple food ordering system. 
# The program should display a menu with the following options:

# Pizza
# Burger
# Pasta
# Exit
# The user should enter the number corresponding to their choice.
# If the user selects Pizza, prompt them to enter the number of pieces they want and display a confirmation message.
# If the user selects Burger, prompt them to specify the size of the burger (Small/Medium/Large) and display a confirmation message.
# If the user selects Pasta, prompt them to specify the type of sauce they want and display a confirmation message.
# If the user selects Exit, display a message and terminate the program.
# If the user enters an invalid choice, display an error message.


a=("Food Ordering System")
print(a)

print(1,"pizza")
print(2,'Burger')
print(3,'Pasta')
print(4,'Exit')

b=int(input("Enter a number of piceses :"))

if b == 1:
    print("Conformation Message")
elif b == 2:
    print("The Booking is Completed")
elif b == 3:
    print("The Booking is Completed")
elif b == 4:
    print("Terminimate the program")
else:
    print("Error Message")