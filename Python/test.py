# for i in range(1,21):
#     if i % 3 == 0:
#         print("Three")
#     else:
#         print(i)


# for i in range(1,16):
#     if i % 4 == 0:
#         print("Four")
#     elif i % 5 ==0:
#         print("Five")
#     else:
#         print(i)


# print("Start")
# for i in range(1,11):
#     print(i)
# print("End")

# number = [10,20,30,40,50,60,70,80]
# print(f"THe index from 3:6 is:", number[3:6])

# number = [10,20,30,40,50,60,70,80]
# print(f"Thefirst five  is:", number[:5])
    

# number = [10,20,30,40,50,60,70,80]
# print(f"The index from numer", number[1:6:2])

            #  OR

# number = [10,20,30,40,50,60,70,80]
# print(number[1:6:2])


# def item_to_list(list, item):
#     list.append(item)


# list = [1,2,3,4,5]

# item_to_list(list,10)

# print(f"Updated List:{list}")


# def check_number(a):
#     if a > 0:
#         print("positive")
#     elif a < 0:
#         print("negative")
#     else:
#         print("Zero")


# num = int(input("Enter the number: "))
# check_number(num)
    

# def divisible(a):
#     if a % 5 == 0:
#         print("The number is divisible by 5:")
#     else:
#         print("THis number is not divisible by 5:")

# num =int(input("Enter the number: "))
# divisible(num)    


# def even_num(a):
#     if a % 2 ==0 and a > 10 :
#         print("This is a Even number and Greater than 10: ")
#     elif a > 10:
#         print("The number is greater than 10:")
#     else:
#         print("Enter the number from 1 to 9")

# num =int(input("Enter the number: "))
# even_num(num)  



        #    or


# def even_num(a):
#     if a > 10 and a % 2 == 0:
#         print("Even and greater than 10")
#     elif a > 10:
#         print("Greater than 10 but odd")
#     else:
#         print("10 or below")

# num = int(input("Enter the number: "))
# even_num(num)



# def a_square(a):
#     """
#     Function Name: add_numbers
#     Parameters:
#     a -> first number

#     return sends the result back to the caller
#     """
#     return a * a


# result = a_square(5)

# print(f"Sum:{result}")



# def square(a):
#     """
#     Function Name: add_numbers
#     Parameters:
#     a -> first number

#     return sends the result back to the caller
#     """
#     return a * a

# user = int(input("Enter The Number :"))

# result = square(user)

# print(f"Sum:{result}")


# username = input("Enter the username:")
# password = input("Enter the password:")

# if username == "admin" and  password == "1234":
#     print("Login Successful")
# elif username == "admin" and password == "":
#     print("You have entered the wrong password ")
# else:
#     print("Invalid User")



# print("Menu")
# print("1.Balance")
# print("1.Withdraw")
# print("1.Deposit")
# print("1.Exit")

# choice = int(input ("Enter the number:"))
# # balance == 100 $
# if choice == 1:
    
#     Balance = int(input("Enther your Accout number: "))
#     print(f"Your current balance is :{Balance}")

