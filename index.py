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
type(false)
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
