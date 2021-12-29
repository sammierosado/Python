# working with str and int types together 

# this does not work because result is an int type and cannot be concatenated
# result = 5 + 5
# print ("I am " + result + " years old.")


# TypeError: unsupported operand type(s) for +: 'str' and 'int'

# use the str function to resolve this issue

# result = 5 + 5
# name = "Sammie"
# name2 = "Kavin"
# job = "programmer"
# age = 28
# city = "New York"
# print("The result is " + str(result))

# # using f-strings

# print(f"{name} and {name2} are currently studying to be a {job}")

# using commas 
# Notice the automatically inserted whitespace between each comma-separated part of the printout. 
# Preventing print from adding the extra spaces is technically possible, but not worth the trouble 
# given that we can instead use f-strings.

# print("Hi", name, ", you are", age, "years old. You live in", city,".")

# name = "Tim Tester"
# age = 20
# skill1 = "python"
# level1 = "beginner"
# skill2 = "java"
# level2 = "veteran"
# skill3 = "programming"
# level3 = "semiprofessional"
# lower = 2000
# upper = 3000

# print(f"my name is {name}, I am {age} years old \n\nmy skills are \n - {skill1} ({level1}) \n - {skill2} ({level2}) \n - {skill3} ({level3}) \n\nI am looking for a job with a salary of {lower}-{upper} euros per month")

# x = 27
# y = 15
# print(f"{x} + {y} = {x + y}\n{x} - {y} = {x - y}\n{x} * {y} = {x * y}\n{x} / {y} = {x / y} ")

# Each print command usually prints out a line of its own, complete with a change of line at the end. 
# However, if the print command is given an additional argument end = "", it will not print a line change.

# print(5, end="")
# print(" + ", end="")
# print(8, end="")
# print(" - ", end="")
# print(4, end="")
# print(" = ", end="")
# print(5 + 8 - 4)

# +	Addition	2 + 4	6
# -	Subtraction	10 - 2.5	7.5
# *	Multiplication	-2 * 123	-246
# /	Division (floating point result)	9 / 2	4.5
# //	Division (integer result)	9 // 2	4
# %	Modulo	9 % 2	1
# **	Exponentiation	2 ** 3	8

# The data type of an operand usually determines the data type of the result: 
# if two integers are added together, the result will also be an integer. If a 
# floating point number is subtracted from another floating point number, the 
# result is a floating point number. In fact, if a single one of the operands 
# in an expression is a floating point number, the result will also be a floating 
# point number, regardless of the other operands.

# Division / is an exception to this rule. Its result is a floating point number, 
# even if the operands are integers. For example 1 / 5 will result in the floating 
# point number 0.2.

# Notice Python also has an integer division operator //. If the operands are integers, 
# it will produce an integer. The result is rounded down to the nearest integer. For 
# example this program

# x = 3
# y = 2

# print(f"/ operator {x/y}")
# print(f"// operator {x//y}")
# prints out

# Sample output
# / operator 1.5
# // operator 1

# number = input("Please type in a number: ")
# print(f"{number} times 5 is {int(number) * 5}")

# days = input("How many times a week do you eat at the student cafeteria?")
# price = input("The price of a typical student lunch?")
# money = input("How much money do you spend on groceries in a week?")

# weekly = float(days) * float(price) + float(money)
# daily = weekly / 7

# print("Average food expenditure:")
# print(f"Daily: {daily} euros")
# print(f"Weekly: {weekly} euros")

#____________________________________________________________________________________

# Please write a program which asks for the number of students on a course and the desired group size. The program will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.

# If you can't get your code working as expected, it is absolutely okay to move on and come back to this exercise later. The topic of the next section is conditional statements. This exercise can also be solved using a conditional construction.

# Sample output
# How many students on the course? 8
# Desired group size? 4
# Number of groups formed: 2

# Sample output
# How many students on the course? 11
# Desired group size? 3
# Number of groups formed: 4

# my solution :

# student = input("How many students on the course? ")
# group = input("Desired group size? ")

# if (int(student) % int(group) == 0):
#     number = int(student) / int(group)

# else:
#     number = int(student) // int(group) + 1


# print("Number of groups formed:", number)

# helsinki solution

# students = int(input("How many students on the course? "))
# group_size = int(input("Desired group size? "))
 
# groups = (students + group_size - 1) // group_size
 
# print("Number of groups formed:", groups)

# year = input("Please type in a number:")
# if (year == 1984):
#     print("Orwell")


# points = int(input("How many points are on your card? "))
# if (points < 100):
#     points *= 1.1
#     print("Your bonus is 10 %")
    
# else:
#     (points >= 100)
#     points *= 1.15
#     print("Your bonus is 15 %")

# print("You now have", points, "points")


temp = int(input("What is the weather forecast for tomorrow?"))
rain = input("Will it rain (yes/no):")

if temp >= 20:
    print("Wear jeans and a T-shirt")
if temp < 20 and temp >= 10:
    print("Wear jeans and a T-shirt\nI recommend a jumper as well")
if temp < 10 and temp <= 5:
    print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you")
if temp < 5:
    print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you\nMake it a warm coat, actually\nI think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")

# temp = int(input("What is the weather forecast for tomorrow?"))
# rain = input("Will it rain (yes/no):")
# coldest = False
# cold = False
# normal = False
# warm = False


# if temp < 5:
#     coldest = True
# if temp < 10:
#     cold = True
# if temp > 10 and temp < 20:
#     normal = True
# if temp > 20:
#     warm = True


# if coldest == True and rain == "yes":
#     print("Wear jeans and a T-shirt\nI recommend a jumper as well\Take a jacket with you\nMake it a warm coat, actually\nI think gloves are in order\nDon't forget your umbrella!")
# if coldest == True and rain == "no":
#         print("Wear jeans and a T-shirt\nI recommend a jumper as well\Take a jacket with you\nMake it a warm coat, actually\nI think gloves are in order")
# if cold == True and rain == "yes":
#     print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you\nDon't forget your umbrella!")
# if cold == True and rain == "no":
#     print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you")
# if normal == True and rain == "yes":
#     print("Wear jeans and a T-shirt\nI recommend a jumper as well\nDon't forget your umbrella!")
# if normal == True and rain == "no":
#         print("Wear jeans and a T-shirt\nI recommend a jumper as well")
# if warm == True and rain == "yes":
#     print("Wear jeans and a T-shirt\nDon't forget your umbrella!")
# if warm == True and rain == "no":
#     print("Wear jeans and a T-shirt")

# Python comparison operators can also be used on strings. String a is smaller than string b if it comes alphabetically before b. Notice however that the comparison is only reliable if

# the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
# only the standard English alphabet of a to z, or A to Z, is used.
# Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

# You can assume all words will be typed in lowercase entirely.

# Some examples of expected behaviour:

# Sample output
# Please type in the 1st word: car
# Please type in the 2nd word: scooter
# scooter comes alphabetically last.

# Sample output
# Please type in the 1st word: zorro
# Please type in the 2nd word: batman
# zorro comes alphabetically last.

# Sample output
# Please type in the 1st word: python
# Please type in the 2nd word: python
# You gave the same word twice.

a = input("Please type in the 1st word: ")
b = input("Please type in the 2nd word: ")

if a > b:
    print(f"{a} comes alphabetically last.")
elif a < b:
    print(f"{b} comes alphabetically last.")
else:
    print("You gave the same word twice.")