#Conditionals & Control Flow

bool_one = 1 < 0 or not 1 >= 1 and 5 > 3 #False or not True and True

bool_two = 1 == 0 and not 2 == 0 or 5 > 3 #False and not True or True

bool_three = 6 > 5 and not (10 < 9 or 10 < 4) #True and not (False or False)

bool_four = 10 != 9 or 10 > 9 and not 1 == 0 #not not True or False and not True

bool_five = 1 < 0 or not (1 >= 1 and 3 >= 3) #False or not (True and True)

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = "Hello" == "Hello" and 2 > 1

# Make me false!
bool_three = 22 < 20 or 1 < 0

# Make me true!
bool_four = 2 > 1 and not (1 > 3)

# Make me true!
bool_five = 5 == 5 or 10 > 3

def using_control_once():
    if 2 > 1:
        return "Success #1"

def using_control_again():
    if 1 == 1:
        return "Success #2"

print (using_control_once())
print (using_control_again())


answer = "'Tis but a scratch!"
def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False       # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False       # Make sure this returns False

print (black_knight())
print (french_soldier())


def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))

# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 65:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print grade_converter(92)

# This should print a "C"
print grade_converter(70)

# This should print an "F"
print grade_converter(61)


#PYGLATIN (Pig Latin)
# move the first letter of the word to the end and add "ay"
# Python = ythonpay

print ('Welcome to the Pig Latin Translator!')

original = input("Enter a word: ")
if len(original) > 0 and original.isalpha():
  print (original)
else:
  print ("empty")

#.isalpha() checks to see if its only letters

pyg = 'ay'
original = input('Enter a word:')  #if word is Hello

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print (new_word)  #it will print  ellohay
else:
    print ('empty')