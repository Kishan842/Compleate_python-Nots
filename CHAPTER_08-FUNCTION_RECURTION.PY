'''function and recurtion'''

def percentage(marks):
    return (sum(marks)/400 )*100

marks1 = [45, 78, 86, 77]
percentage1 = percentage(marks1)

marks2 = [48, 76, 86, 70]
percentage2 = percentage(marks2)
print(percentage1, percentage2)

'''
Quick Quize: Write a program to greet a user with "good day" using function
'''
def greet(name):
    print("Good day " + name)
greet("Kishan")

# ------------------------------------------------------- #

'''Function with argument'''
def great(name):
    print("good day " + name)

def muSum(num1, num2):
    return num1 + num2

great("Kishan")
s = muSum(6, 30)
print(s)

# ------------------------------------------------------- #

'''default parameter value'''
def great(name="stranger"):
    print("good day " + name)

great("kishan")
great()

# ------------------------------------------------------- #

'''Recursion'''
# n! = 1 * 2 * 3 * 4
# n! = [1 * 2 * 3 * 4..... n-1] *n
# n! = n * (n-1)!

# First Ex:- # n! = 1 * 2 * 3 * 4
n = 4
product = 1
for i in range(n):
    product = product * (i+1)
print(product)

# second Ex:- # n! = [1 * 2 * 3 * 4..... n-1] *n
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
print(factorial_iter(5))

# thirs Ex:- # n! = n * (n-1)!
def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)
print(factorial_recursive(5))


# ------------------------------------------------------- #

# ---> PRECTICE SET✍🏻👩🏻‍💻
'''
Q.1 Write a program using function to find greatest of three number
'''
def maximum(num1, num2, num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m = maximum(3, 5, 234)
print("The value of the maximum is " + str(m))

# ------------------------------------------------------- #

'''
Q.2 Write a python program using function to convert celsius to fahrenite
'''
def faranite(celsius):
    return (celsius *(9/5)) + 32

c = 35
f = faranite(c)
print("Fahrenhite tempreture is " + str(f))

# ------------------------------------------------------- #

'''
Q3. How do you present a python print() function to print a new time at the end
'''
print("Hello", end=" ")
print("how", end=" ")
print("are", end=" ")
print("you", end=" ")

# ------------------------------------------------------- #

'''
Q.4 Write a python function to first a line of the following pattern
*****
****
***         n = 5
**
*
'''
n = 5
for i in range(n):
    print("*" * (n-i)) # prints * n-i times

# ------------------------------------------------------- #

'''
Q.5 Write a python function to remove a given words from a string and strip it at the same time

Ex of stripe:- this = "     kishan is a good boy       "
print(this)
print(this.strip())
'''
def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Kishan is a good boy       "
n = remove_and_split(this, "Kishan")
print(n)

# ------------------------------------------------------- #

'''
Q.6 Write a python function to print nultiplication table of a given number
'''
def multiplication_table(number, upto):
    for i in range(1, upto + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

multiplication_table(5, 10)
