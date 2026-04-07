set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

c=set1.union(set2)
print(c)

# Out Put => {1, 2, 3, 4, 5, 6}   
# Union means combine all elements from both sets without duplicates.

d=set1.intersection(set2)
print(d)

# Out Put => {3, 4}

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}


e=set1.difference(set2)
print(e)

# Out Put => {1, 2}

f=set2.difference(set1)
print(f)

# Out Put => {5,6}


a = {1,2,3,4,5}
b={5,6,7,8,9,10}

c=a.difference(b)
print(c)

# {1, 2, 3, 4} 

d=b.difference(a)
print(d)

# {6, 7, 8, 9, 10}