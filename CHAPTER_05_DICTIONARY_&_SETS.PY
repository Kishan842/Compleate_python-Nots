''' Dictionary is a collection of rey - value paires '''

MY_LIST = {
    "Kishan": " He is sigma programmer",
    "Kajal": " She is a medical lab tecnition",
    "Bunny": {'Bunny': 'Is a supar Space Cluster'},
    "Sarthik": " He is a good programmer",
    "Marks": [1, 6, 8]
}
print(MY_LIST["Sarthik"]); print(MY_LIST["Kishan"]) # print the keys of the dictionry
print(MY_LIST["Kajal"]); print(MY_LIST["Marks"]) # print the keys of the dictionry
print(MY_LIST["Bunny"]) # print the (keys, value) for all contents of the dictionry
print(MY_LIST)

updateList = {
    "Mohan": "Friend",
    "Deva": "Friend",
    "Suhani": "Friend",
    "Kishan": "brocken person",
}
MY_LIST.update(updateList) # update the dictionry by adding key-value pairs from updateList 
print(MY_LIST)

print(MY_LIST.get("Kishan")) # prints  value aassosiated with key "Kishan"
print(MY_LIST["Kishan"]) # prints  value aassosiated with key "Kishan"

# The difrens betwen..get [] sytax in dictionrys?
print(MY_LIST.get("Kishan2")) # Returns none as harry2 is not present in the dictionry
print(MY_LIST["Kishan2"]) # throws an harry as harry2 is not present in the dictionry

# ---------------------------------------------------------------------------------------------------------------------------- #

''' Sets '''

a = {1, 2, 3, 4, 5, 1}
print(a)
print(type(a))

# ---------------------------------------------------------------------------------------------------------------------------- #

''' Empty set '''
# --> Important: This syntax will create an empty dictionary and not an empyu set
a = {}
print(type(a))

# --> an empty set be created using the below syntax
b = set()
print(type(b))

# ---------------------------------------------------------------------------------------------------------------------------- #

''' Set Methods '''

## Creating an empty set
b = set()
print(type(b))

## Adding value to an empty set
b.add(4)
b.add(5)
b.add(5) # Adding a value respectedly dose not change a set
b.add(5)

## b.add([7, 8, 12]) # Cannot add list or dictionry to sets
b.add((7, 8, 12))
print(b)

## Length of the set
print(len(b)) # print the lenght of this set

## Removel of an Item
b.remove(5) # Remove 5 from set b


## b.remove(12) # throw an error while trying to remove is(which is not present in the set)
print(b)


print(b.pop())
print(b)

# ---------------------------------------------------------------------------------------------------------------------------- #

# ---> PRECTICE SET✍🏻👩🏻‍💻
'''
Q.1 Write a program to create a dictionry of Hindi words with values
as this english translation provided user with an option to look it up
'''
myDict = {
    "pankha": "Fan",
    "Dabba": "Box",
    "vastu": "Item"
}
print("Option are ", myDict.keys())
a = input("Enter the Hindi word: ")
print("The meaning of your word is:",myDict.get(a))

# ---------------------------------------------------------------------------------------------------------------------------- #

'''
Q.2 write a program to input eight numbers from the user and display all the 
unique numbers
'''
num1 = int(input("Enter  nimber 1: "))
num2 = int(input("Enter  nimber 2: "))
num3 = int(input("Enter  nimber 3: "))
num4 = int(input("Enter  nimber 4: "))
num5 = int(input("Enter  nimber 5: "))
num6 = int(input("Enter  nimber 6: "))
num7 = int(input("Enter  nimber 7: "))
num8 = int(input("Enter  nimber 8: "))

s = {num1, num2, num3, num4, num5, num6, num7, num8}
print(s)

# ---------------------------------------------------------------------------------------------------------------------------- #

'''
Q.3 Can we have a set with 18 (int) and "18" (str) as a value in it?
'''
s = {18, "18"}
print(s)

# ---------------------------------------------------------------------------------------------------------------------------- #

'''
Q.4 What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add("20")
'''
s = {20, 20.0, "20"}
print(s)
print(len(s))

# ---------------------------------------------------------------------------------------------------------------------------- #

'''
Q.5 S = {}, what is the type of S ?
'''
S = {}
print(type(S))

# ---------------------------------------------------------------------------------------------------------------------------- #

'''
Q.6 Create an empty dictionry Allo 4 friends to enter their
favorate language as values and use keys as their name asume
that the names are unique.
'''
favLang = {}
first_Friend = input("Enter your favorite Alex : ")
second_Friend = input("Enter your favorite Toredo : ")
third_Friend = input("Enter your favorite Robart : ")
fourth_Friend = input("Enter your favorite Junior : ")

favLang["Alex"] = first_Friend
favLang["Toredo"] = second_Friend
favLang["Rpbart"] = third_Friend
favLang["Junior"] = fourth_Friend
print(favLang)

# ---------------------------------------------------------------------------------------------------------------------------- #

'''
Q.7 If name of 2 friends are same; What will to the program
in problem 6?
'''
favLang = {}
first_Friend = input("Enter your favorite Alex : ")
second_Friend = input("Enter your favorite Toredo : ")
third_Friend = input("Enter your favorite Robart : ")
fourth_Friend = input("Enter your favorite Junior : ")

favLang["Alex"] = first_Friend
favLang["Toredo"] = second_Friend
favLang["Alex"] = third_Friend
favLang["Junior"] = fourth_Friend
print(favLang)

# ---------------------------------------------------------------------------------------------------------------------------- #

'''
Q.8 Can you chage the value inside a list witch is contaned
in set S? S = {8, 7, 12, "Kishan", [1,2]}
'''
S = {8, 7, 12, "Kishan", [1,2]}
print(S)

# Ans:- No Why : Explaination
# S = {8, 7, 12, "Kishan", [1,2]}
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'list'
