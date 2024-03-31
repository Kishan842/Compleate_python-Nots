'''Opps'''
'''
a = 12
b = 34
print("This sum of a and b is ", a+b)

----> Write to this program using OBJECT_ORIENTED_PROGRAM
'''
class Number:
    def sum_Number(self_counting):
        return self_counting.integir_Number_1 + self_counting.integir_Number_2
Variable = Number(); Variable.integir_Number_1 = 12
Variable.integir_Number_2 = 34
user_End = Variable.sum_Number()
print(user_End)

# ------------------------------------------------------- #

class Jojo:
    def math(a):
        return a.int1 + a.int2
val = Jojo()
val.int1 = 55
val.int2 = 5
b = val.math()
print(b)

# ------------------------------------------------------- #

'''
defrence between camel_case or pascal_case
1. pascalCase
EmployeeName --> pascalCase
2. camalCase
isNumeric, isFloat --> camalCase
'''

# ------------------------------------------------------- #

'''Example of Railway form_filling'''
class RailwayForm:
    formtype = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"train is {self.train}")

kishanAplication = RailwayForm(); kishanAplication.name = "Kishan"
kishanAplication.train = "Rajdhani Express"
kishanAplication.printData()

# ------------------------------------------------------- #

'''Explample of game using opps'''

# ----------------------------
# class Remote():            |
#     pass                   |
#                            |
# class player:              |
#     def moveRight(self):   |
#         pass               |
#                            |   <------ THIS PART CALL IS INCAPSULATION ------>
#     def moveLeft(self):    |           <------ SIMPLE CAPSULE ------>
#         pass               |
#                            |
#     def moveTop(self):     |
#         pass               |
# ----------------------------
# remote1 = Remote()
# player1 = player()

# if(remote1.isLeftPressed()):
#     player1.moveLeft()

# ------------------------------------------------------- #

'''class Atribute'''
class Employee:
    compny = "Google"

kishan = Employee()
kajal = Employee()
print(kishan.compny)
print(kajal.compny)
Employee.compny = "YouTube"
print(kishan.compny)
print(kajal.compny)

# ------------------------------------------------------- #

'''instant Atribute'''
class Employee:
    compny = "Goole"
    salary = 100

kishan = Employee()
kajal = Employee()

# creating instance attribute sallary for both the object
# kishan.salary = 500
# kajal.salary = 400
kishan.salary = 450
print(kishan.salary)
print(kajal.salary)

# print(kajal.adress) ----> below line throws an error as adress is not present in instane/class <----

# ------------------------------------------------------- #

'''self parameter'''

class Employee:
    compnay = "Amazone"
    def getSallary(self):
        print(f"Sallary for this employe working in {self.compnay} is {self.Sallary}")

kishan = Employee()
kishan.Sallary = 100000
kishan.getSallary() # Employee.getSallary(kishan)

# ------------------------------------------------------- #

'''static method'''
class Employee:
    company = "Amazon"

    def get_salary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.Salary}")
        print(signature)

    @staticmethod
    def great():
        print("Good Morning Sir")

    @staticmethod
    def time():
        print("The time is 4:AM in the morning")

kishan = Employee()
kishan.Salary = 100000
kishan.get_salary("Thanks!")  # Employee.get_salary(kishan, "Thanks!")
kishan.great()  # Employee.great()
kishan.time()

# ------------------------------------------------------- #

'''__init__() constroctor'''
'''
# __init__() is a special method which is first as soon as the object is creating
__init__() method is also rename as construction
'''
class Employee:
    company = "Amazon"

    def __init__(self, name, salary, subunit):    # <---- This is caled consttact ---->
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employe is created")
        
    def get_Details(self):
        print(f"The Name of the employe is {self.name}")
        print(f"Or Salary of the employe is {self.salary}")
        print(f"And Subunit of the employe is {self.subunit}")

    def get_salary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.Salary}")
        print(signature)

    @staticmethod
    def great():
        print("Good Morning Sir")

    @staticmethod
    def time():
        print("The time is 4:AM in the morning")

kishan = Employee("Kishan", 100, "Microsoft")
kishan.get_Details()

# ------------------------------------------------------- #

# ---> PRECTICE SET✍🏻👩🏻‍💻
'''
Q.1 Create a class programmer for storing information of few programmers working
at microsoft.
'''
class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of {self.company} programmer is {self.name} and the product is {self.product}")

kishan = Programmer("Kishan", "Skype")
alka = Programmer("Alka", "GitHub")

kishan.getInfo()
alka.getInfo()

# ------------------------------------------------------- #

'''
Q.2 Write a class calculator capable of finding square, cube and square
root of a number.
'''
class Calculator:
    def __init__(self, num):
        self.number = num
    
    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"The value of {self.number} square root is {self.number **0.5}")


    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")

a = Calculator(9)
a.square()
a.squareRoot()
a.cube()

# ------------------------------------------------------- #

'''
Q.3 Create a class with a class attribute a; create an object from it and set a
directly using object.a = 0. Dose this change the calss attribute>
'''
class Sample:
    a = "kishan"

obj = Sample()
obj.a = "Kajal"
# Sample.a = "Kajal"

print(Sample.a)
print(obj.a)

# ------------------------------------------------------- #

'''
Q.4 Add a static method in python 2 to greet the user with hello.
'''
class Calculator:
    def __init__(self, num):
        self.number = num
    
    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"The value of {self.number} square root is {self.number **0.5}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")

    @staticmethod
    def grate():
        print("***** Hello welcome to the calculator of the world *****")

a = Calculator(9)
a.grate()
a.square()
a.squareRoot()
a.cube()

# ------------------------------------------------------- #

'''
Q.5 Write a class Train witch has method to book a ticket, get status(non of seat)
and get fare information of train humming under indian Railways.
'''
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("**********")
        print(f"The train of the name is {self.name}")
        print(f"The seats available in the train is {self.seats}")
        print("**********")

    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats -= 1
        else:
            print("Sorry, this train is full. Kindly try in tatkal")

    def fareInfo(self):
        print(f"The price of the ticket is Rs. {self.fare}")

    def cancelTicket(self, seatNo):
        self.seats += 1
        print(f"Your ticket with seat number {seatNo} has been canceled.")

intercity = Train("Intercity Express: 14015", 90, 300)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket(1)
intercity.getStatus()

# ------------------------------------------------------- #

'''
Q.6 Write you change the self parameter inside a class to something else, (say, 'Kishan')
try changing self to 'self' or 'Kishan' and see the effects.
'''
class Sample:
    a = "Kishan"
    def __init__(slf, name):
        slf.name = name

obj = Sample("Kishan")
print(obj.name)
