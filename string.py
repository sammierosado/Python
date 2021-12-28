# working with str and int types together 

# this does not work because result is an int type and cannot be concatenated
# result = 5 + 5
# print ("I am " + result + " years old.")


# TypeError: unsupported operand type(s) for +: 'str' and 'int'

# use the str function to resolve this issue

result = 5 + 5
name = "Sammie"
name2 = "Kavin"
job = "programmer"
age = 28
city = "New York"
print("The result is " + str(result))

# using f-strings

print(f"{name} and {name2} are currently studying to be a {job}")

# using commas 
# Notice the automatically inserted whitespace between each comma-separated part of the printout. 
# Preventing print from adding the extra spaces is technically possible, but not worth the trouble 
# given that we can instead use f-strings.

print("Hi", name, ", you are", age, "years old. You live in", city,".")

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old \n\nmy skills are \n - {skill1} ({level1}) \n - {skill2} ({level2}) \n - {skill3} ({level3}) \n\nI am looking for a job with a salary of {lower}-{upper} euros per month")

x = 27
y = 15
print(f"{x} + {y} = {x + y}\n{x} - {y} = {x - y}\n{x} * {y} = {x * y}\n{x} / {y} = {x / y} ")