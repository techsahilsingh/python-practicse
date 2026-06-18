# Day 1 of learning python 
"""
(#) is used for comments  and triple quotes is used for multiline comments
"""
#printing hello world in python 
print("hello world")


# variables
# conditons of a vriable 
# 1. can only have numbers,letters,underscores
# 2. can start with a letter or underscore but not with a number
# 3. variable names cannot contain spaces avoid using keywords and functions as variables 
# 4. variables should be descriptive not short 
# a vriable is a container that stores data values 
# for example
a = 1  # a stores value 1 which can be printed by calling b in print
print(a)
b = 32 # b stores value 32 which can be printed by calling b in print
print(b )
# Descriptive varible eg
house_address = "Mumbai Suburban"


# data types in python

# string (It is used to print text messages it can be written using '' or "")
# Example
alpha = "Tiger" 
Beta = 'wolf'
print(alpha)

# Numbers -> Integers,float,complex
# integers (1,3,2,9) etc
# printing an integer 
c = 32
print(c)
print(type(c))
# Float 
d = 3.156
print(d)
print(type(d))
# complex
comple = 1+9j
print(comple)
print(type(comple))

# Boolean
# A boolean helps in identifying i f a statement is true or false
# True has the value of 1 and O is for False
# for example
pest = "Cockroach"
zest = "Whale"
print(pest == zest)
# It will return an output as false 
# Adding ture and false 
print(True+False)

#list 
# A list allows a varibale to store different data types in a varibale it is mutable
# A list uses square brackets
# for example 
list_1 = [1,2,3,4,5,6,7,8]
list_2 = ["Apple","Microsoft","Google","Netflix","Meta","SalesForce"]
list_3 = ["Amazon",123,5.21,False]

# Dictionary
# Uses key value pair 
data = { "name": "Jake", "age": 22 }
print(data)
data["age"] = "Jack" #updating the  dictionary
data["salary"] = 45000 # Adding to dictionary
del data["age"] # Removing data form the table
print(data)

# Tuple uses () brackets to store data in a varibale 
# Tuples are used to store non mutable list of data values it is similar to list 
Names_tuple = ("TCS","Infosys","Micron","Deloitte")
print(Names_tuple)
print(type(Names_tuple))

# Set 
# Set in python only store unique data type values it is similar to list and tuple but is unorderd 
# A set uses {} to store data
my_set ={15.3,"abc",45,63+35j,True}
print(my_set)
# trying arthimetic operations in python using print function
print(2+2)#additon
print(3*4)#multipication
print(4/3)#division
print(89%6)#modulus (used for finding the remainder)
print(4**2)#expeonetion (used to assign power to the value)
print(45//6)#floor division operator
