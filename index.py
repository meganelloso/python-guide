#1
#Data Types = string, int, float, complex(?)


#2 - String Slicing[start:stop:step] stop not included in the string
freeCodeCamp = "freeCodeCamp"

freeCodeCamp[2:8]
#eeCode
freeCodeCamp[0:3]
#fre
freeCodeCamp[4:7]
#Cod
freeCodeCamp[8:11]
#Cam
freeCodeCamp[8:13]
#Camp
freeCodeCamp[2:10:3]
#eoC
freeCodeCamp[1:12:4]
#roa
freeCodeCamp[3:9:2]
#eoe
freeCodeCamp[10:2:-1]
#maCedoCe
freeCodeCamp[11:4:-2]
#paeo
freeCodeCamp[5:2:-4]
#o


#3 - f-Strings (only in Python 3.6)
first_name = "Megan"
favorite_language = "Python"
print(f"Hi I'm {first_name} and I'm currently studying {favorite_language}.")

value = 5
print(f"The value is {value}. If you multiply it by 2, product will be {value * 2}")

codeCamp = "CODECAMP"
print(f"{codeCamp.lower()}")

#4 - String Methods
freeCodeCamp = "freeCodeCamp"

freeCodeCamp.capitalize()
#Freecodecamp
freeCodeCamp.count("C")
#2
freeCodeCamp.find("e")
#2 - first e he can find
freeCodeCamp.index("p")
#11
freeCodeCamp.isalnum()
#True (?)
freeCodeCamp.isalpha()
#True (?)
freeCodeCamp.isdecimal()
#False
freeCodeCamp.isdigit()
#False
freeCodeCamp.isidentifier()
#True (?)
freeCodeCamp.islower()
#False
freeCodeCamp.isnumeric()
#False
freeCodeCamp.isprintable()
#True
freeCodeCamp.istitle()
#False(?)
freeCodeCamp.isupper()
#False
freeCodeCamp.lower()
#freecodecamp
freeCodeCamp.lstrip("f")
#reeCodeCamp
freeCodeCamp.rstrip("p")
#freeCodeCam
freeCodeCamp.replace("e","a")
#fraaCodaCamp
freeCodeCamp.split("C")
#['free','ode','amp']
freeCodeCamp.swapcase()
#FREEcODEcAMP
freeCodeCamp.title()
#Freecodecamp
freeCodeCamp.upper()
#FREECODECAMP

#5 Boolean value - should always be upper to recognize as boolean
type(False)
#returns boolean
#type(false)
#returns error

#6 - len() function to return length of the list

#7 - List Slicing; same structure with string slicing

#8 - Tuple like list but immutable; cant be inserted/updated
# diff tuple vs list?? ok with/without parentheses
# can also have nested tuples
# can slice
my_tuple = (1, 2, 3, 4, 5)
my_tuple = ([1, 2, 3, 4], (5, 6, 7, 8))

#9 Tuple assignment - exclusive for Python only
a, b = 1, 2
#a = 1; b = 2

#10 Dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
#dictionary key can be anything except list but dict values can be any data type.
# can add, update, call a key in dict. to add, must be a new key name
# to delete, use del statement
#del my_dict["c"]

my_dict.get("a") #1
my_dict.items() #shows all
my_dict.keys() #shows keys only

True + False #1 bec 1 + 0 = 1

#11 Operators (Unique)
#Exponentiation **: 5 ** 2 = 25; 6 ** 8 = 1679616 (6*6*6*6*6*6*6*6)
#16 ** (1/2) = 4.0?
#125 ** (1/3) 4.999999?
"Hello" * 4
#HelloHelloHelloHello
"Hello" * 0 #''
"Hello" * -1 #''
#/ Operator - returns float even operands = integer
#// Operator - returns integer if operands = integer, returns float if operands = float
"Hello" > "World" #False; this is based on alphabetical order

#If else statements
x = 5
if x < 9:
    print("Hello!")
elif x < 15:
    print("WIts gr8 to see you")
else:
    print("Bye!")

print("End")

#For Loop statements
for num in range(8):
    print("Hello" * num)
#Hello
#HelloHello
#HelloHelloHello etc

my_list = ["a", "b", "c", "d"]

for i in range(len(my_list)):
    print(my_list[i])

for i in range(2,10):
    print(i)
#prints 2 - 9

for key in my_dict:
    print(key)
#prints a b c

#for value in my_dict.values:
#    print(value)
#prints 1 2 3

for key, value in my_dict.items():
    print(key, value)
#prints a 1, b 2, c 3

for key in my_dict.items():
    print(key)
#prints ('a', 1) ('b', 2) ('c', 3) a tuple

#Break and Continue in Python
#break - ends the loop
#continue - skips but loop continues

todays_list = [1, 2, 3, 4, 5]

for num in todays_list:
    if num % 2 == 0:
        print("Even:", num)
        print("break")
        break
    else:
        print("Odd:", num)

#prints Odd: 1, Even: 2 break

for num in todays_list:
    if num % 2 == 0:
        print("continue")
        continue
    else:
        print("Odd", num)

#prints Odd: 1, continue, Odd: 3, continue etc

#zip() function - iterate multiple sequences at once in a for loop
my_list1 = [1, 2, 3, 4]
my_list2 = [5, 6, 7, 8]

for elem1, elem2 in zip(my_list1, my_list2):
    print(elem1,elem2)
#prints 1 5, 2 6, 3 7, 4 8

#enumerate() function - keep track of the index on loop

for i, elem in enumerate(my_list):
    print(i, elem)

for i, elem in enumerate(my_list, 2):
    print(i, elem)
#magsstart sa 2 instead of 0

#else clause in for loop
#if you want a block of code after the loop completes
#else does not run if "break" was executed vice versa

for elem in my_list1:
    if elem > 6:
        print("Found")
        break
else:
    print("Not Found")

#prints not found
#we can also do this in while loop

#Nested loops - the inner loop runs for each iteration of the other loop
for i in range(3):
    for j in range(2):
        print(i,j)
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1

for i in range(3):
    print("==> Outer Loop")
    print(f"i = {i}")
    for j in range(2):
        print("Inner loop")
        print(f"j = {j}")
        

def print_product(a, b=5):
    print(a * b)

#kapag walang binigay na value for b, 5 yung default value.
#pwede maoverride ung 5 kapag binigyan ng value
#note na kailangan magkadikit yan pag arguement

#Exception Handling
#ZeroDivisionError when divisor is 0
#IndexError sobra index na namention
#KeyError key is not in the dictionary
#NameError variable that does not even defined

index = int(input("Enter the index here: "))

try:
    sample_list = [1, 2, 3, 4]
    print(sample_list[index])
except IndexError as e:
    print("Error raised: ", e)

a = int(input("Enter value of a variable: "))
b = int(input("Enter value of b variable: "))

try:
    division = a / b
    print(division)
except ZeroDivisionError as e:
    print("Error raised: ", e)
else:
    print("both variables are valid.")
#prints try and else block if no 0 on the variables
#you can add "finally:" if u want to run it with or without error
#finally can be used if you want to close a file even when it throws an exception

#OOP in Python
#__int__ - to store attributes

#Set = only accepts unique value
myset = set()
myset.add(1)
myset.add(2)
myset.add(2)
set(myset)

#from python lib
from random import shuffle

example_shuffle = [1,2,3,4,5,6,7,8,9]

def shuffle_dict(sample_list):
    shuffle(sample_list)
    return sample_list

shuffle_dict(example_shuffle)

#*args **kwargs
#*args - to have multiple arguements in a function; will pass as a tuple
#pwede iba pangalan for args and kwargs

def myfunc(*args):
    for item in args:
        print(item)

myfunc(1,2,3,4,5,6,7,8,9,0)

#**kwargs - same as args pero dictionary yung 

def myfunc_kwargs(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
         print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('i dont see any fruit here')

myfunc_kwargs(fruit='apple', veggie = 'lettuce')

#pwede *args and **kwargs in one function
#pero kung nauna ung args, args dapat unang ipapasok

def myfunc_both(*args, **kwargs):
    print(args, kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc_both(10, 20, 30, food='eggs', animal='dog')

#SUMMARY
# Lists: Ordered sequence of objs (mutable)
# Tuples;: Ordered seq of obj (immutable)
# Dictionary: Key-value pairing that is unordered