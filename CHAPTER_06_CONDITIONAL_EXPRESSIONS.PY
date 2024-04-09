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
if(age>18 and age<60): # 18> sika matlab 18 se jyada <60 se kam
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
    print("No and yos")
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

d1 = {45:"Amit", 81:"Ajay", "Age":18, "Weight":50}
for i in d1:
    print(i, ":", d1[i]) #sep=""



















# import tkinter as tk
# from tkinter import ttk

# LARGEFONT = ("Verdana", 35)

# class tkinterApp(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)

#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#         self.frame = {}

#         for F in (StartPage, Page1, Page2):
#             frame = F(container, self)
#             frame.grid(row=0, column=0, sticky="news")
#             self.frame[F] = frame 

#         self.show_frame(StartPage)

#     def show_frame(self, cont):
#         frame = self.frame[cont]
#         frame.tkraise()

# class StartPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text="Start Page", font=LARGEFONT)
#         label.grid(row=0, column=4, padx=10, pady=10)
#         button1 = ttk.Button(self, text="Page 1", command=lambda: controller.show_frame(Page1))
#         button1.grid(row=1, column=4, padx=10, pady=10)

# class Page1(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text="Page 1", font=LARGEFONT)
#         label.grid(row=0, column=4, padx=10, pady=10)
#         button1 = ttk.Button(self, text="Back to Start", command=lambda: controller.show_frame(StartPage))
#         button1.grid(row=1, column=4, padx=10, pady=10)

# class Page2(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text="Page 2", font=LARGEFONT)
#         label.grid(row=0, column=4, padx=10, pady=10)
#         button1 = ttk.Button(self, text="Back to Start", command=lambda: controller.show_frame(StartPage))
#         button1.grid(row=1, column=4, padx=10, pady=10)

# app = tkinterApp()
# app.mainloop()

# import random
# passlen = int(input("enter the length of password: "))
# s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"
# p = "".join(random.sample(s,passlen ))
# print(p)

counter = 5
while counter > 0:
    print("counter = ", counter) 
    counter = counter - 1
