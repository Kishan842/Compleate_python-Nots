'''Inheritance is a way of creating a new class from on existing class'''
def cal_sum(a, b):
    sum = a + b
    print(sum)
    return sum

cal_sum(5, 10)

# ------------------------------------------------------- #

# Function Definatipm
def cal_Sum(a, b): # --> parameters
    return a + b

sum = cal_Sum(10, 5) # --> function call arguments
print(sum)

# ------------------------------------------------------- #

def print_hello():
    print("Hello World")

print_hello()

# ------------------------------------------------------- #

def print_hello():
    print("Hello World")

output = print_hello()
print(output)

# ------------------------------------------------------- #

# avrage of three numbers
def cal_Sum(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

cal_Sum(1, 2, 3)

# ------------------------------------------------------- #

print("Hello kishan", end=" ") # sep = " "
print("Hello kishan", end="s") # sep = " "
print("Kishan", end=" ") # end = "\n"

# ------------------------------------------------------- #

def calsum(a = 4, b = 6):
    print(a * b)
    return a * b

calsum()

# ------------------------------------------------------- #

citis = ["delhi", "gurgon", "noida", "mumbai", "channai"]
heros = ["thor", "ironman", "captan america", "krish"]

def print_len(list):
    print(len(list))


print_len(citis)
print_len(heros)

# ------------------------------------------------------- #

citis = ["delhi", "gurgon", "noida", "mumbai", "channai"]
heros = ["thor", "ironman", "captan america", "krish"]

print_len(heros[0], end=" ")
print_len(heros[1], end=" ")

def print_len(list):
    print(len(list))

print_len(citis)
print_len(heros)

# ------------------------------------------------------- #

citis = ["delhi", "gurgon", "noida", "mumbai", "channai"]
heros = ["thor", "ironman", "captan america", "krish"]

def print_len(list):
    print(len(list))

def print_len(list):
    for item in list:
        print(item, end="")

print_len(heros)
print()
print_len(citis)
print()

# ------------------------------------------------------- #

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= 1
    print(fact)

cal_fact(5)

# ------------------------------------------------------- #

def converter(used_val):
    inr_val = used_val * 85
    print(used_val, "USD =", inr_val, "INR")

converter(100) # Ex:- 74, 35, 46, 85, 59, 

# ------------------------------------------------------- #

class Employe:
    company = "Google"

    def showDetails(self):
        print("This is an employe")

class programmer(Employe):
    language = "Python"
    # company = "YouTube"

    def getLanguage(self):
        print(f"the language is {self.getLanguage}")

    def showDetails(self):
        print("This is an programmer")

e = Employe()
e.showDetails()
print(e.company)
p = programmer()
p.showDetails()
print(p.company)

# ------------------------------------------------------- #

'''Types of Inheritance'''
# ***** 1. Single Inheritance *****
class Employe:
    company = "Google"

    def showDetails(self):
        print("This is an employe")

class programmer(Employe):
    language = "Python"

    def getLanguage(self):
        print(f"the language is {self.getLanguage}")

    def showDetails(self):
        print("This is an programmer")

e = Employe()
e.showDetails()
print(e.company)
p = programmer()
p.showDetails()
print(p.company)

# ------------------------------------------------------- #

# ***** 2. Multipal Inheritance *****
class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgredLevel(self):
        self.level = self.level + 1

class Programmers(Employee, Freelancer):
    name = "Kishan"

p = Programmers()
p.upgredLevel()
print(p.level)
print(p.company)

# ------------------------------------------------------- #

# ***** 3. Multilevel Inheritance *****
class Person:
    country = "India"
    
    def takBreth(self):
        print("I am breathing...")

class Employe:
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takBreth(self):
        print("I am an employee, so I am breathing lucky...")

class Programmer(Employe, Person): 
    company = "Fiverr"

    def getSalary(self):
        print("No salary for a programmer")

    def takBreth(self):
        print("I am a programmer, so I am breathing even luckyear...")

p = Person()
p.takBreth()

e = Employe()
e.takBreth()
print(e.company)

pr = Programmer()
pr.takBreth()
print(pr.company)
print(pr.country)
pr.getSalary()

# ------------------------------------------------------- #

'''Super method'''
class Person:
    country = "India"
    
    def takBreth(self):
        print("I am breathing...")

class Employe:
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takBreth(self):
        print("I am an employee, so I am breathing lucky...")

class Programmer(Employe, Person):
    company = "Fiverr"

    def getSalary(self):
        print("No salary for a programmer")

    def takBreth(self):
        print("I am a programmer, so I am breathing even luckyear...")

p = Person()
p.takBreth()

e = Employe()
e.takBreth()
print(e.company)

pr = Programmer()
pr.takBreth()
print(pr.company)
print(pr.country)
pr.getSalary()

# ------------------------------------------------------- #

'''Class method'''
class Employe:
    compnay = "Camel"
    salary = 100
    location = "Mumbai"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod    # <--- its caled decorator
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employe()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employe.salary)

# ------------------------------------------------------- #

'''@property decorator'''
class Employee:
    company = "Bharat Gas"
    salary = 5000
    salaryBonus = 1000

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary

e = Employee()
print(e.totalSalary)  
e.totalSalary = 10000
print(e.salary)       
print(e.salaryBonus)  

# ------------------------------------------------------- #

'''Operator Overloading'''
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("Lets Multiply")
        return self.num * num2.num

# n1 = int(input("Enter The First number: "))
# n2 = int(input("Enter The Second number: "))
n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)

# ------------------------------------------------------- #

'''Othe dunder/magic method'''
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("Lets Multiply")
        return self.num * num2.num
    
    def __str__(self):
        return f"Decimal Number: {self.num}"
    
    def __len__(self):
        return 1

n1 = Number(4)
print(n1)
print(len(n1))

# ------------------------------------------------------- #

# ---> PRECTICE SET✍🏻👩🏻‍💻
'''
Q.1 Create a class C2dVector and it to create another class representing
a 3-d Vector.
'''
class C2dvector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dvector(C2dvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dvector(1, 3)
v3d = C3dvector(1, 9, 7)
print(v2d)
print(v3d)

# ------------------------------------------------------- #

'''
Q.2 Creare a class pets from a class Animal And further create class Dog from
pets. Add a method brek to class dog.
'''
class Animals:
    animalType = "Mammal"

class pets:
    color = "White"

class Dog:
    @staticmethod
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()

# ------------------------------------------------------- #

'''
Q.3 Create aca class employee and add salary and increment properties to it.
write a method salaryAfterIncrement method with a @property decoretor with a setter
which changes the value of increment based on the salary.
'''
class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = new_salary / self.salary

e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 2000
print(e.increment)

# ------------------------------------------------------- #

'''
Q.4 Wite a class complex to represent comlex numbers, alnog with overlodedwith a setter 
witch changes the calue of increment based on the salary.
'''
# Formula --> (a + bi) (c + di) = (ac - bd) + (ab + bc)
class Complex:
    def __init_subclass__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, c):
        return Complex(self.real + self.real, self.imaginary + c.imaginary)
    
    def __mul__(self, c):
        muReal = self.real * c.real - self.imaginary * c.imaginary
        mulimg = self.real * c.imaginary + self.imaginary * c.real
        return Complex(muReal, mulimg)

    def __str__(self):
        return f"{self.real} + {self.imaginary}"
    
c1 = complex(1, 4)
c2 = complex(1, 4)
print(c1 + c2)
print(c1 * c2)

# ------------------------------------------------------- #

'''
Q.5 Write a class vector representing a vector of n dimention overload
the + and * operator which claculate the sum and dot product of them.
'''
class Vector:
    def __init__(self, *vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0

        for i in self.vec:
            str1 += f"{i}a{index} + "
            index += 1
        return str1[:-1]
    
    def __add__(self, vac2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vac2.vec[i])
        return Vector(newlist)
    
v1 = Vector([1, 4, 6])
v2 = Vector([1, 8, 9])
print(v1+v2)

# ------------------------------------------------------- #

'''
Q.6 Write __str__() method to print the vector as follows:
                    7i + 8j + 18k
Assume vector of dimention 3 for this problem.
'''
class Vector:
    def __init__(self, *vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

v1 = Vector(1, 4, 6)
v2 = Vector(1, 8, 9)
print(v1)
print(v2)  

# ------------------------------------------------------- #

'''
Q.7 Overide the_len__() method on vector of problem 5 to display
the dimention of the vector.
'''
class Vector:
    def __init__(self, *vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0

        for i in self.vec:
            str1 += f"{i}a{index} + "
            index += 1
        return str1[:-1]

    def __add__(self, v):
        new_list = [a + b for a, b in zip(self.vec, v.vec)]
        return Vector(*new_list)

    def __len__(self):
        return len(self.vec)

v1 = Vector(1, 4, 6, 5, 45)
v2 = Vector(1, 8, 9)

print(len(v1))
print(len(v2))

# ------------------------------------------------------- #

def cal_sum(a, b):
    sum = a + b
    print(sum)
    return sum

cal_sum(15, 20)

class Person:
    country = "India"
    
    def takBreth(self):
        print("I am breathing...")

class Employe:
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takBreth(self):
        print("I am an employee, so I am breathing lucky...")

class Programmer(Employe, Person):
    company = "Fiverr"

    def getSalary(self):
        print("No salary for a programmer")

    def takBreth(self):
        print("I am a programmer, so I am breathing even luckyear...")

p = Person()
p.takBreth()

e = Employe()
e.takBreth()
print(e.company)

pr = Programmer()
pr.takBreth()
print(pr.company)
print(pr.country)
pr.getSalary()