'''1. While Loop'''
i = 1
while i<10:
    print("Yes: " + str(i))
    i = i + 1

# ------------------------------------------------------- #

'''2. Quick Quize: Write a program to print 1 to 50 using a while with loop'''
i = 1
while i<=50:
    print("yes: " + str(i))
    i = i + 1

# ------------------------------------------------------- #

'''3. Quick Quize: Write a program to print the contest of a list using while loop'''
fruites = [
    "Banana", "Watermallon",
    "greps", "Mango"
]
i = 0
while i<len(fruites):
    print(fruites[i])
    i = i + 1

# ------------------------------------------------------- #

'''3. For loop'''
fruites = [
    "Watermallon", "Banana",
    "greps", "Mango"
]
for item in fruites:
    print(item)
# ------------------------------------------------------- #

'''4. Range function'''
for i in range(1,8):
   print(i)

'''5. Step size Rnage function'''
for i in range(1, 8, 2):
    print(i)

# ------------------------------------------------------- #

'''6. For loop with else'''
for i in range(10):
    print(i)
else:
    print("This is inside else of for")

# ------------------------------------------------------- #

'''7. Break statment in loop'''
for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("This is inside else of for")

# ------------------------------------------------------- #

'''8. continew statment in loop'''
for i in range(10):
    if i == 5:
        continue
    print(i)

# ------------------------------------------------------- #

'''9. Pass statment in loop'''
i = 4
if i>0:
    pass
while i>6:
    pass
print("Kishan is a good boy")

# ------------------------------------------------------- #

# ---> PRECTICE SET✍🏻👩🏻‍💻
'''
Q.1 Wite a program to print multiplication table of a given number using for loop.
'''
num = int(input("Enter the number: "))
for i in range(1, 11):
    print(str(num) + " X " + str(i) + " = " + str(i*num)) # Short form --> print(f"{num}X{i}={num*i}")

# ------------------------------------------------------- #

'''
Q.2 Write a program to gretatst the person names stord in a list that l1 abd which start with 5

l1 = ["Kishan", "Code", "Full", "Night"]
'''
l1 = [
    "Kishan", "Code", "Kajal", "Full", "Night"
]
for name in l1:
    if name.startswith("K"):
        print("Hello " + name)

# ------------------------------------------------------- #

'''
Q.3 Write a program to find whether a given number is prime or not.
'''
num = int(input("Enter the number: "))
Perime = True
for i in range(2, num):
    if(num%i == 0):
        Perime = False
        break
if Perime:
    print("This numbe is prime")
else:
    print("This number is not a prime")

# ------------------------------------------------------- #

'''
Q.4 Write a program to find the sum of first n natural numbers using while loop.
'''
# n! = 1 X 2 X 3 X 4....... X-n
# 5! = X 2 X 3 X 4 X 5.

num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")

# ------------------------------------------------------- #

'''
Q. 5 Write a program to input following star pointter
*
**
***  
****     fot n = 3
'''

n = 4
for i in range(4):
    print("*" * (i+1))

# ------------------------------------------------------- #

'''
Q. 6 Write a program to input following star pointter
  *  
 *** 
*****
'''
n = 3
for i in range(3):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
