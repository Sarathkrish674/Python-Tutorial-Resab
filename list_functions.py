# Add 50 to the list.

# lst = [10, 20, 30, 40]
# lst.append(50)

# print(f"The Output Is {lst}")  The Output Is [10, 20, 30, 40, 50]


# lst = [1, 2]
# lst.insert(2, 3)
# print(f"The Output Is {lst}")    The Output Is [1, 2, 3]


# Add 100 in to the list

# li=[20,40,60,80]

# li.append(100)
# print(li)  [20, 40, 60, 80, 100]


# Add extend to the list

# li =[1,2]
# li.extend([3,4])
# print(li)  [1, 2, 3, 4]


# Add a number to the list 

# li=[1,2,3]
# li.insert(3,15)
# print(li)    [1, 2, 3, 15]                    String is always in the square bracket[]


# li=[1,3,4]
# li.extend("SA")
# print(li)   [1, 3, 4, 'S', 'A']



# me=["Sarath","Sumith"]
# me.append("Mrudun")
# print(me)   ['Sarath', 'Sumith', 'Mrudun']



# me=["Sarath","Sumith"]
# me.extend("Midhun")
# print(me)     ['Sarath', 'Sumith', 'M', 'i', 'd', 'h', 'u', 'n']


# Add a number 6 in the tuple

# a=(1,2,3,4,5)
# print(f"this is tuple ,{a}")
# b=list(a)
# print(f"this is list ,{b}")
# b.append(6)
# print(f"this is list ,{b}")
# c=tuple(b)
# print(f"final tuple ouput,{c}")

# this is tuple ,(1, 2, 3, 4, 5)
# this is list ,[1, 2, 3, 4, 5]
# this is list ,[1, 2, 3, 4, 5, 6]
# final tuple ouput,(1, 2, 3, 4, 5, 6)


# Add a number 45 in the 3rd index in the tuple

# a=(1,2,3,4,5,6,7)
# b=list(a)
# print(b)
# b.insert(3,45)
# print(b)
# c=tuple(b)
# print(c)

# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 45, 4, 5, 6, 7]
# (1, 2, 3, 45, 4, 5, 6, 7)



# Me = [1,2,3,4,4]
# Me.remove(4)
# print(Me)

# [1, 2, 3, 4]



# M=[10,30,50]
# M.pop()
# print(M)

# [10, 30]



# S=[20,40,50]
# S.pop(1)
# print(S)

# [20, 50]


# cart = ["Laptop", "Mouse", "Keyboard", "USB Cable"]

# print(cart)

# cart.clear()

# print(cart)

# ['Laptop', 'Mouse', 'Keyboard', 'USB Cable']
# []



# actions = ["Login", "Open File", "Edit Text", "Save File"]

# last_action = actions.pop()

# print("Removed Action:", last_action)
# print("Remaining Actions:", actions)


# Removed Action: Save File
# Remaining Actions: ['Login', 'Open File', 'Edit Text']




# attendance = ["Arun", "Meena", "John", "Divya", "Kiran"]
# print("These are the present studnts:",attendance)

# list.clear(attendance)
# print(attendance)

# attendance.append("Rahul")
# print(attendance)


 
employee = {
    "id": 101,
    "name": "Arjun",
    "salary": 25000,
    "department": "IT"
}

employee.keys()
print(employee.keys())

employee.values()
print(employee.values())

employee.get("name")
print(employee.get("name"))

employee.update({"salary": 30000})
print(employee)

employee.update({"city": "Chennai"})
print(employee)

employee.pop("department")
print(employee)