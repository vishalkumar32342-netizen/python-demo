#______MODULES_________
#  A group of functions, variables and classes saved to a file, which is nothing but module. 
 
#    Every Python file (.py) acts as a module. 
from math import*
print(sqrt(4))
print(factorial(5))
print(sin(8))
print(ceil(12))


#math_module.
# sqrt()
# pow()
# sin()
# cos()
# factorial()
# ceil()
# floor()

# Various possibilties of import: 
 
# import modulename 
# import module1,module2,module3 
# import module1 as m 
# import module1 as m1,module2 as m2,module3 
# from module import member 
# from module import member1,member2,memebr3 
# from module import memeber1 as x 
# from   module import *


# member aliasing: 
 
# from durgamath import x as y,add as sum 
# print(y) 
# sum(10,20) 
 
# Once we defined as alias name,we should use alias name only and we should not use 
# original name 
  
# Eg: 
# from durgamath import x as y 
# print(x)     #==>NameError: name 'x' is not defined 


# Reloading a Module: 
#By default module will be uploaded only once eventhough we are importing multiple times.
# program for module reloading
# import time
# from imp import reload
# import module1
# time.sleep(30)
# reload(module1)
# time.sleep(30)
# reload(module1)
# print("This is test file")

#Finding members of module by using dir() function: 
x=10
y=20
def f1():
    print("hello")
print(dir())


# The Special variable __name__: 
# For every Python program , a special variable __name__ will be added internally. 
# This variable stores information regarding whether the program is executed as an 
# individual program or as a module. 
 
# If the program executed as an individual program then the value of this variable is 
# __main__ 
# If the program executed as a module from some other program then the value of this 
# variable is the name of module where it is defined. 
 
# Hence by using this __name__ variable we can identify whether the program executed 
# directly or as a module.

#working with random module:
# This module defines several functions to generate random numbers. 
# We can use these functions while developing games,in cryptography and to generate 
# random numbers on fly for authentication.

#1.random()function:
#___This function always generate some flat value between o and 1(not inclusive)

from random import*
for i in range(20):
    print(random()) 

#__randint()function:
#To generate random integer between two given numbers(inclusive)
from random import*
for i in range(10):
    #print(randint(1,10),randint(1,10),randint(1,10),randint(1,10),"")
    print(randint(10000,99999))

#__uniform():
#It returns random float values between 2 given numbers(not inclusive)
from random import*
for i in range(10):
    print(uniform(1,10))

#__Choice () function:
#It wint return random number.
#It will return a random object from the given list or tuple
from random import*
list=["sunny","vishal","rohit","bunny","chunny","gunny"]
for i in range(10):
    print(choice(list))


# import secrets

# otp = secrets.randbelow(900000) + 100000
# print(otp)

from random import randint

otp = randint(0, 999999)

print(f"{otp:06d}")