numbers = [18, 24, 33, 40, 45, 54, 60, 72, 81, 90, 99, 108]
a =[]
b =[]
c =[]
for i in numbers:
    if (i % 3 == 0) & (i % 9 == 0):
        a.append(i)
    elif (i % 3 == 0):
        b.append(i)
    elif (i % 9 == 0):
       c.append(i)
print(f"The number both divisible by 3 & 5 is:{a}")
print(f"The number both divisible by 3 is:{b}")
print(f"The number both divisible by 9 is:{c}")

