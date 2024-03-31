'''create a list using []'''
a = [1,2,3,6,9,56]
# print the list using print() function
print(a)
'''Access using index using a[0], a[1], a[2]'''
print(a[2])

# ---------------------------------------------------------------------------------------------------------------------------- #

'''change the value of using list'''

a= [1,2,6,7]
a[0] = 98
print(a)

# ---------------------------------------------------------------------------------------------------------------------------- #

'''We can create a lost items of difrent types'''
c = [45, "Kishan", False, 6.9]
print(c)

# ---------------------------------------------------------------------------------------------------------------------------- #

'''List slicing'''
friends = ["Kishan", "Kajal", "Sir ji", "Bharat", "SUgandhim", 45]
print(friends[0:4])
a = 45
b = 65
print("The value is", a + b)

# ---------------------------------------------------------------------------------------------------------------------------- #

'''List methods'''
l1 = [1, 8, 7, 2, 21, 15]
print(l1)
# ---sorts the list---
l1.sort()
# ---reverses the list---
l1.reverse()
print(l1)
# ---.append the list --> append of the end of the list---
l1.append(54)
print(l1)

# ---------------------------------------------------------------------------------------------------------------------------- #

'''Tuples'''
t = (1, 2, 4, 5)
print(t[0])

t1 = () # ---Empty tuple---
t1 = (1) # ---Wrong way to declear a Tuple with single element---
t1 = (1,) # ---Tuple with single element---
print(t1)

# ---------------------------------------------------------------------------------------------------------------------------- #

'''tuple method'''
t = (1, 2, 4, 5, 1, 1, 6, 8, 3, 1, 1,)
print(t.count(1))
print(t.index(5))

# ---------------------------------------------------------------------------------------------------------------------------- #

# ---> PRECTICE SET✍🏻👩🏻‍💻
'''
Q.1> Write a programm to store fruites in a list entred by user.
'''
f1 = input("Enter Fruit Number 1 : ")
f2 = input("Enter Fruit Number 2 : ")
f3 = input("Enter Fruit Number 3 : ")
f4 = input("Enter Fruit Number 4 : ")
f5 = input("Enter Fruit Number 5 : ")
f6 = input("Enter Fruit Number 6 : ")
f7 = input("Enter Fruit Number 7 : "); print("\n")
list = [f1, f2, f3, f4, f5, f6, f7]
print(list)

# ---------------------------------------------------------------------------------------------------------------------------- #

'''
Q.2> Write a program to input of 6 student and display
them in a sourted manner
'''
m1 = int(input("Enter Marks for student Number 1 : "))
m2 = int(input("Enter Marks for student Number 2 : "))
m3 = int(input("Enter Marks for student Number 3 : "))
m4 = int(input("Enter Marks for student Number 4 : "))
m5 = int(input("Enter Marks for student Number 5 : "))
m6 = int(input("Enter Marks for student Number 6 : "))

myList = [m1, m2, m3, m4, m5, m6]
myList.sort()
print(myList)

# ---------------------------------------------------------------------------------------------------------------------------- #

'''
Q.3> Check that a Tuple can no be a changed
'''
a = (2, 4, 6, 9, 12)
a[0] = 45

# ---------------------------------------------------------------------------------------------------------------------------- #

'''
Write a program to sum a list with 4 numbers.
'''
a = [2, 4, 56, 3]
print("The sum is",a[0] + a[1] + a[2] + a[3])

# ---------------------------------------------------------------------------------------------------------------------------- #

'''
Write a program to find the numbers of zeros to find
the following tuple. ex:-> (7, 0, 8, 0, 0, 9)
'''
number = (7, 0, 8, 0, 0, 9)
print(number.count(0))