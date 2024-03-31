a = "kishan" # string type
b = 562 # int type
c = 45.23 # float type
d = True # Booleans Variable
e = None # None Type bariable

# ------------------------------------------------------- #

'''Printing the variables'''
print(a)
print(b)
print(c)
print(d)
print(e)

# ------------------------------------------------------- #

'''
identifires datas and for us
'''
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# ------------------------------------------------------- #

'''
operators
'''
# Arithemetic operators
'''
+, -, *, /, ect.
'''
a = 65
b = 45
print("The value 64 + 45 is ", 64 + 45)
print("The value 64 - 45 is ", 64 - 45)
print("The value 64 * 45 is ", 64 * 45)
print("The value 64 / 45 is ", 64 / 45)

# ------------------------------------------------------- #

'''Assigment Operators.'''

'''
=, +=, -=, ect.
'''
a = 23
a += 2
print(a)

# ------------------------------------------------------- #

'''Comparition operators.'''

'''
==, >, >=, <, !=, ect.
'''
b = (14>7)
print(b)
b = (14>=7)
print(b)
b = (14<7)
print(b)
b = (14==7)
print(b)
b = (14!=7)
print(b)

# ------------------------------------------------------- #

'''Logical operatrs'''

'''
and, or, not ect.
'''
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 and bool2 is", (bool1 or bool2))
print("The value of not bool2 is", (not bool2))

# ------------------------------------------------------- #

'''Typecasting variables'''

# string type       # int type
# a = "3534"        | a = 9594
# a = int(a)        | a = (a)
# print(a + 5)      | print(a + 5)

# ------------------------------------------------------- #

'''Input function'''
a = int(input("Enter a name: "))
print(a); print(type(a))

a = input("Enter your name: ")
print(a); print(type(a))

# ------------------------------------------------------- #

# ---> PRECTICE SET✍🏻👩🏻‍💻
'''
Q.1> Write a program to add two number
'''
a = 56
b = 12
print("The sum is a and b is ", a + b)

# ------------------------------------------------------- #

'''
Q.2> Write a program to find remainder when a number is divided by 2
'''
a = 659
b = 53
print("The remainder when a is divided by b is", a%b)

# ------------------------------------------------------- #

'''
Q.3> use comparition operator to find out whether a given
variable a is genrated then "b" or not
Take a = 34 and b = 80
'''
a = 34
b = 80
print(a>b); print(a<b)

# ------------------------------------------------------- #

'''
Q.4> Write a program to find a average of two numbers entered by the user
'''
a = float(input("enter first number: "))
b = float(input("enter second number: "))
avg = (a + b)/2
print("The value if a and b is", avg)

# ------------------------------------------------------- #

'''
Q.5> Write a program to calculate square of a number enter by user
'''
a = int(input("enter first number: "))
b = int(input("enter second number: "))
avg = (a * b)
print(avg)
