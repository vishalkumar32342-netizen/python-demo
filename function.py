#__---A function is a group of statements that can be used repeatedly to perform a specific task
#__---a function is of two types
#____-1.Pre-defined function
#___--2.User defined function

#__Check whether the number is even or odd

# def even_odd(n):
#     if n%2==0:
#         print("{} is even".format(n))
#     else:
#         print("{} is odd".format(n))
# even_odd(19)
# even_odd(40)

#__Find factorial of number without using recursion:
# def fact(n):
#     result=1
#     while n>=1:
#         result=result*n
#         n=n-1
#     return result
# for i in range(1,8):
#     print("The factorial of {} is {}".format(i,fact(i)))

#Calculator
# def calc(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return sum,sub,mul,div
# t=calc(100,400)
# print("The result are")
# for x in t:
#     print(x)

#__Types of arguments
#__1.Positional arguments
def sub(a,b):
    print(a-b)
sub(100,40)


#__2.Keyword arguments
def wish(name,msg):
    print("hello",name,msg)

wish(name="vishal",msg="good morning")
wish(msg="good morning",name="muskan")

#Note: 
 
# We can use both positional and keyword arguments simultaneously. But first we have to 
# take positional arguments and then keyword arguments,otherwise we will get 
# syntaxerror.


#__3.Default arguments
#___ Sometimes we can provide default values for our positional arguments.
def wish(name="guest"):
    print("Hello",name,"Good morning")
wish()
wish("vishal")

#__4._____Variable length arguments
# Sometimes we can pass variable number of arguments to our function,such type of 
# arguments are called variable length arguments. 
 
# We can declare a variable length argument with * symbol   as follows 
 
# def f1(*n): 
 
# We can call this function by passing any number of arguments including zero number. 
# Internally all these values represented in the form of tuple. 

def sum(*n):
    total=0
    for n1 in n:
        total=total+n1
    print("The sum=",total)

sum()       
sum(10)
sum(10,20,30)
sum(10,20,30,40,453)

#__VARIABLE:
#__1.GLOBAL VARIABLE
# ----The variables which are declared outside of function are called global variables. 
# ----These variables can be accessed in all functions of that module. 


#__2.LOCAL VARIABLE
#-- The variables which are declared inside a function are called local variables. 
#-- Local variables are available only for the function in which we declared it.i.e from outside 
# --of function we cannot access. 
a=10  #global
def f1():
    global a   #creating inside of global variable.
    a=50
    print(a)

def f2():
    print(a)

def f3():
    a=40 #local variable
    print(a)

f3()
f2()
f1()


#___RECURSIVE FUNCTION
# A function which calls itself is called recusive function.
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print(factorial(4))
print(factorial(65))

#___LAMBDA FUNCTION(ANONYMOUS FUNCTION)
# SOMETIOMES WE CAN DECLARE A FUNCTION WITHOUT ANY NAME,SUCH TYPE OF NAMELESS  FUNCTION ARE 
# CALLED ANONYOMOUS FUNCTION OR LAMBDA FUNCTION.

#Write a program to create a lambda function to find square of given NUMBER
s=lambda n:n*n
print("the square of 4 is",s(4))
print("THe square of 89 is",s(89))

# Lambda function to find sum of 2 given numbers 
s=lambda a,b:a+b
print("the sum of 4,5 is",s(4,5))

# Lambda Function to find biggest of given values. 
s=lambda a,b: a if a>b else b
print("the biggest of 100,200 is",s(100,200))
print("the biggest of 340,500 is",s(340,500))

# Note: 
# Lambda Function internally returns expression value and we are not required to write 
# return statement explicitly. 
 
# Note: Sometimes we can pass function as argument to another function. In such cases 
# lambda functions are best choice. 

# We can use lambda functions very commonly with filter(),map() and reduce() functions,b'z 
# these functions expect function as argument. 

#FILTER() FUUNCTION
#  We can use filter() function to filter values from the given sequence based on some 
# condition.

# Q. Program to filter only even numbers from the list by using filter() 
# function? 
 
# without lambda Function: 
def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,10,20,30,24,25,45,56,55]
l1=list(filter(isEven,l))
print(l1)

#_with lambda function
l=[0,10,20,30,24,25,45,56,55,89,66]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
l2=list(filter(lambda x:x%2!=0,l))
print(l2)

# map() function: 
 
#  For every element present in the given sequence,apply some functionality and generate 
# new element with the required modification.  For this requirement we should go for 
# map() function.

#without lambda
l=[10,20,49,50,30,40]
def doubleIt(x):
    return 2*x
l1=list(map(doubleIt,l))
print(l1)

#with lambda
l=[10,20,40,45,56,78]
l1=list(map(lambda x:2*x,l))
print(l1)

 # To find square of given numbers by taking input from the user.
# l=list(map(int,input("Enter some number: ").split(',') ))
# l1=list(map(lambda x:x*x,l))
# print(l1)

#reduce() function: 
 
# reduce() function reduces sequence of elements into a single element by applying the 
# specified function. 
 
# reduce(function,sequence) 
 
# reduce() function present in functools module and hence we should write import 
# statement. 

from functools import*
l=[10,20,30,40,50,5060,30]
result=reduce(lambda x,y:x*y,l)
print(result)

from functools import*
result=reduce(lambda x,y:x+y,range(1,101))
print(result)


#__Function ALiasing
#For the existing function we can give another name, which is nothing but function aliasing

def wish(name):
    print("Good morning:",name)

greeting=wish

greeting("vishal")
wish("kjbn")


wish("vishsl")
greeting("vishal")

#__NESTED FUNCTION
# we can declare function inside another function,such type of function are called Nested function.
def outer():
    print("outer function is executed:")
    def inner():
        print("inner function execution:")
    print("outer function is calling inner function: ")
    inner()
outer()


# def numbers():
#     yield 1
#     yield 2
#     yield 3


# x = numbers()

# # print(next(x))
# # print(next(x))
# print(next(x))