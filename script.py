#Python basics 

#Using print will display anything. Use quotes for Python2 and parentheses for Python3
print ("My first time using Python")
print ("Learning Python from Codecademy")

#Combining multiple strings using +
print ("Starting" + "Python")
#That still displays as Starting Python

#SyntaxError: EOL while scanning a string literal
##String wasn't closed properly

#NameError: creating a string without quotes.. Python thinks its a command

#Variables = string
todays_date = "1/6/2020"

#Math Operators
#Using % finds the remainder to the answer 
#15 % 2 = 1 ... will return 1

money_in_wallet = 40
sandwich_price = 7.50
sales_tax = 0.8*sandwich_price #use price of sandwich to calculate sales tax

sandwich_price += sales_tax #add tax to final price of sandwich
money_in_wallet -= sandwich_price

sept_rainfall = 5.16
oct_rainfall = 7.20
#annual_rainfall += sept_rainfall + oct_rainfall

#Numbers:
##integer = whole number (int)
##float = decimal number (float)
##e = power of 10 (1.5e2 = 150)

##if you want a decimal number back from dividing, make one or both numbers a float with a decimal
###7./2 = 3.5
###7/2. = 3.5
###7./2. = 3.5
###float(7)/2 = 3.5

cucumbers = 100
num_people = 6
cucumbers_per_person = cucumbers/num_people
print (cucumbers_per_person)
#16 will only print because it is a whole number and it wasn't defined as decimal

float_cucumbers_per_person = float(cucumbers)/num_people
print (float_cucumbers_per_person)
#will display 16.666667

#use triple quotes (""") for a string to span multiple lines

#BOOLEANS
#MUST USE CAPITAL T or F
a = True
b = False

age = 26
#26 is an integer so must convert to a string
print ("I am "+str(age)+" years old!")

num1 = "100"
num2 = "200"
#these are strings so must convert to integer
string_addition = num1 + num2
#answer is 100200
int_addition = int(num1) + int(num2)
#answer is 300

float_1 = 0.25
float_2 = 40.0
product = float(float_1) * float_2
#it will keep it a decimal answer
big_string = "The product was "+str(product)