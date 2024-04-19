'''1. if-elif-else ladder'''
Number = 3 # More Example:- Number = 15,56,2,4,53,78,100, take any number
if (Number>3):
    print("The Value of Number is greter than 3")
elif(Number>13):
    print("The Value of Number is greter than 13")
elif(Number>7):
    print("The Value of Number is greter than 7")
elif(Number>17):
    print("The Value of Number is greter than 17")
else:
    print("The value is not greter than of any number")

# ---------------------------------------------------------------------------------------------------------------------------- #

'''2. Multiple if statment'''
num = 85
if(num<3):
    print("The Value of num is greter than 3")

if(num<13):
    print("The Value of num is greter than 13")

if(num<7):
    print("The Value of num is greter than 7")

if(num>17):
    print("The Value of num is greter than 17")

else:
    print("The value is not greter than of any number")

# ---------------------------------------------------------------------------------------------------------------------------- #

'''Quick quize: Write a program to print yes when the age enterd
by the user is greter then or equal to 18'''
age = int(input("Enter your age: "))
if age>18:
    print("Yes")
else:
    print("No")

# ---------------------------------------------------------------------------------------------------------------------------- #

'''Logical Operators'''
age = int(input("Enter your age: "))
if(age>18 and age<60):
    print("You can work with us")
else:
    print("You can not work with us")

# ---------------------------------------------------------------------------------------------------------------------------- #

'''in or is Operator'''
# Use of is
a = None
if (a is None):
    print("Yes")
else:
    print("No")
    
# Use of in
a = [45, 56, 36]
print(456 in a)

# ---------------------------------------------------------------------------------------------------------------------------- #

'''if else optional'''
a = 66 #Ex:- 63, 4, 86, 2, 3,. 
if(a==7):
    print("Yes")
elif(a>56):
    print("No and yes")
else:
    print("I am optional")

# ---------------------------------------------------------------------------------------------------------------------------- #

p = 1234
c = 0
while(c!=3):
    c = c + 1
    pin = int(input("Enter a pin: "))
    if pin==p:
        print("Tranjection sucsesfull")
        break
    else:
        print("Encorexct pin")
else:
    print("\n\t\tCard block")

# ---------------------------------------------------------------------------------------------------------------------------- #
