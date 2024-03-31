a = "Kishan's" # --> Use yhis if you have single quates in your string
b = '''Kishan's and kishan'''
print(a)
print(b)
print(type(a))

# ------------------------------------------------------- #

''' Concatenating two string'''
greeting = "Good After Noon"
name = "Kishan"
c = greeting + name
print(c)

# ------------------------------------------------------- #

'''String slicing'''
name = "Kishan"
print(name[0])
print(name[0:7])
print(name[1:5])
print(name[:4]) # --> is same as name[0:4]
print(name[1:]) # --> is same as name[1:4]
c = name[2:-1]
print(c)
print("The function of the minimize of the power tranjection of the minimum power")

# ------------------------------------------------------- #

'''Slicing with skip value'''
name = "Kishanisgood"
d = name[1:4:2]
e = name[0::2] # they are skip one variable
f = name[0::3] # they are skip 2 variable
print(d); print(e); print(f)

# ------------------------------------------------------- #

'''String functions'''
story = "once apon a time there was a influancere name Kishan who uploaded python"
# Len function
print(len(story))
# string endswith function
print(story.endswith("python"))
# string count function
print(story.count("a"))
# string capitalize function
print(story.capitalize())
# string find function
print(story.find("Kishan"))
# string replace function
print(story.replace("Kishan", "Code With Kishan"))

# ------------------------------------------------------- #

'''Escape Sequence character'''
story = "Kishan is good.\nHe is Verry good" # Ex:- \n, \t, \, \\ ect.
print(story) 

# ------------------------------------------------------- #

# ---> PRECTICE SET✍🏻👩🏻‍💻
'''
Q.1 Write a program to display a user enterd name follow by good
afternoon using user input function
'''
name = input("Please inter your name: ")
# print("Good Afternoon", name)

# ------------------------------------------------------- #

'''
Q.2 Write a program to fill in a letter template given below with name and date
'''
latter = ''' Dear <|"Kishan|>,
You are selected!

Date: |DATE|>
'''
name = input("Enter your name: ")
date = input("Enter date: ")
latter = latter.replace("<|NAME|>", name)
latter = latter.replace("DATE", date)
print(latter)

# ------------------------------------------------------- #

'''
Q.3 Write a program to detect dubble space  in a string
'''
st = "This is a string with a dubble spease"
dS = st.find("  ")
print(dS)

# ------------------------------------------------------- #

'''
Q.4 replacea a double spaces from problem 3 with single spaces
'''
st = "This is a string with a single   spease"

st = st.replace("   ", " ")
print(st)

# ------------------------------------------------------- #

'''
Q.5 Write a program to formate the following letter using scape sequence charactor
EX:- "Dear Kishan.This python course is nice.Thanks!"
'''
letter = "Dear Kishan.This python course is nice.Thanks!"
print(letter)

formatted_letter = "Dear Kishan,\n\tThis python course is nice!\nThanks,"
print(formatted_letter)

print("Kishan")
print("Kishan")
print("Kishan")
print("Kishan")
print("Kishan")
