'''reading a file'''
# ------------------------------------------------------- #

'''Other method to read the file'''
File = open('SAMPLE.TXT')
# read first line
# use open function to read content of the file
File = open('SAMPLE.TXT', 'r')
File = open('SAMPLE.TXT') # by defalut the mode is r
data = File.read()
# data = File.read(20) # read first charecters from the file
print(data)
File.close()
data = File.readline()
print(data)

# read second line
data = File.readline()
print(data)

# read third line... and so on...
data = File.readline()
print(data)
File.close()

# ------------------------------------------------------- #

'''Writing file'''
File = open('ANOUTHER.TXT', 'w')
File.write("i am Writing")
File.close()

# ------------------------------------------------------- #

'''with statment'''
# first commentout this then run
'''
File = open('ANOUTHER.TXT', 'w')
File.write("i am Writing")
File.close()
'''
with open("ANOUTHER.TXT", 'r') as File:
    a = File.read()
with open("ANOUTHER.TXT", 'w') as File:
    a = File.write("me")
print(a)

# ------------------------------------------------------- #

# ---> PRECTICE SET✍🏻👩🏻‍💻
'''
Q.1 Write a program to read the text from a given file poem.txt, and find out who there it
continus the word twinkle
'''
file = open('POEM.TXT')
text = file.read()
if 'twinkle' in text:
    print("twinle is present")
else:
    print("twinkle is not present")
file.close()

# ------------------------------------------------------- #

'''
Q.2 The game() function in a program lets a user play game and return the score as an
integear you need to read a file 'hiscore.txt' which is either blank or contains the 
previous hi-score you need to write a program to update the hi-scoore whenaver game()
breaks the hi-score
'''
# Simple method
def game():
    return 100000000

score = game()
with open("HIGH-SCORE.TXT") as f:
    hisscore = int(f.read())

if hisscore<score:
    with open("HIGH-SCORE.TXT", 'w') as f:
        f.write(str(score))

# Second logical Method
def game():
    return 456564

score = game()
with open("HIGH-SCORE.TXT") as f:
    hisscoreStr = f.read()

if hisscoreStr == "":
    with open("HIGH-SCORE.TXT", 'w') as f:
        f.write(str(score))

elif int(hisscoreStr)<score:
    with open("HIGH-SCORE.TXT", 'w') as f:
        f.write(str(score))

# ------------------------------------------------------- #

'''
Q.3 Write a python program to genrate multiplication tables from 2 to 20 and write
it to the defrent fies. place these files in a folder for a 13 - year old.
'''
# # Ex:- Two Table
for i in range(2, 20):
    with open(f"TABLES/multiplication_table_of_Two_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i * j}\n")
    break
# Ex: Ninteen Table
for i in range(19, 190):
    with open(f"TABLES/multiplication_table_of_Ninteen_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i * j}\n")
    break
# Ex:- Eighteen Table
for i in range(18, 180):
    with open(f"TABLES/multiplication_table_of__Eighteen{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i * j}\n")
    break

# ------------------------------------------------------- #

'''
Q.4 A file contains a word "Donky" tmultiplication times you need to write a program which replace
this word with # # # # # by update the same file.
'''
with open("SAMPLE2.TXT") as f:
    content = f.read()

content1 = content.replace("donky", "%$@^&()&^%$")

with open("SAMPLE2.TXT", "w") as f:
    f.write(content1)

# ------------------------------------------------------- #

'''
Q.5 Reapt program 4 for a list of such words to be conserd
'''
words = ["donky", "kaddu", "mote"] 

with open("SAMPLE2.TXT") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "%$@^&()&^%$")
    with open("SAMPLE2.TXT", "w") as f:
        f.write(content)

# ------------------------------------------------------- #

'''
Q.6 Write a program to mine a log file and find out whether it contains 'python'
'''
with open("LOG.TXT") as f:
    content = f.read()

if 'python' in content.lower():
    print("yes python is present")
else:
    print("No python is not present")

# ------------------------------------------------------- #

'''
Q.7 Write a program to find out the line number where python is present
from qution 6
'''
i = 1
content = True
with open("LOG.TXT") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"yes python is present on line number {i}")
        i+=1

# ------------------------------------------------------- #

'''
Q.8 Write a program to make a copy of a text file "THIS.TXT"
'''
with open("THIS.TXT") as f:
    content = f.read()

with open("COPY.TXT", 'w') as f:
    f.write(content)

# ------------------------------------------------------- #

'''
Q.9 Write a program to find out whether a file is identical & matches the
content of onether file
'''
file1 = "COPY.TXT" # EX:- put this <-- file1 = "LOG.TXT"
file2 = "THIS.TXT"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("File are identical")
else:
    print("File are not identical")
    
# ------------------------------------------------------- #

'''
Q.10 Write a program to wipe out content of a file using python
'''
# IF YOU **RUN** THIS PROGRAM THEN ERRESE ALL DATA IN SAMPLE3.TXT
filename = "SAMPLE3.TXT"
with open("FILENAME", 'w') as f:
    f2 = f.write("")

# ------------------------------------------------------- #

'''
Q.11 Write a program to rename a file to "REMOVE_BY_PYTHON.TXT"
'''
import os

oldName = "SAMPLE4.TXT"
newName = "RENAMED_BY_PYTHON.TXT"
with open(oldName) as f:
    content = f.read()

with open(newName, 'w') as f:
    f.write(content)

os.remove(oldName)
 
