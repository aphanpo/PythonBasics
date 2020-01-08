#Strings and Console output

#use backslash ( \ ) if there is an apostrophe in a word if using single quotes
'There\'s an apostrophe in that word'
"There's an apostrophe in that word"

#Will print " Y " because its the 4th index
fifth_letter = "MONTY"[4]
print (fifth_letter)

#String Methods
##len() returns the number of characters in a string
parrot = "Norwegian Blue"
print (len(parrot))
#returns 14
##.lower() returns all characters lower case.. only works with strings
print (parrot.lower())
##.upper() returns ALL CAPS.. only works with strings
print (parrot.upper())
##str() turns non-strings into strings
print (str(2))

#%s is a placeholder for a variable and using % followed by the variable will replace %s in order
string_1 = "Camelot"
string_2 = "place"

print ("Let's not go to %s. It's a silly %s." % (string_1, string_2))

#when you run this code, the console will ask each question and then populate the sentence
name = input("What is your name? ")
quest = input("What is your quest? ")
color = input("What is your favorite color? ")

print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))


#Date and Time Library

from datetime import datetime #imports datetime from library
now = datetime.now()
print (now)
print (now.month)
print (now.day)
print (now.year)

#print date in mm/dd/year
print ("%02d/%02d/%04d" %(now.month, now.day, now.year))
print ("%02d:%02d:%02d" %(now.hour, now.minute, now.second))