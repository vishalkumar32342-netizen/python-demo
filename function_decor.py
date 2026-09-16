# Function Decorators: 
 
# Decorator is a function which can take a function as argument and extend its functionality 
# and returns modified function with extended functionality.
# def decor(func):
#     def inner(name):
#         if name=="sunny":
#            print("Hello sunny bad morning")
#         else:
#             func(name)
#     return inner

# @decor
# def wish(name):
#     print("hello",name,"Good morning")

# # decorfunction=decor(wish)

# wish("Vishal")
# # decorfunction("sunny")
# wish("sunny")
# wish("Abhishek")

# #______
# def smart_division(func):
#     def inner(a,b):
#         print("We are dividing",a,"with",b)
#         if b==0:
#             print("OOPS....cannot divide")
#             return
#         else:
#             return func(a,b)
#     return inner

# @smart_division
# def division(a,b):
#     return a/b

# print(division(20,0))

# Decorator Chaining 
 
# We can define multiple decorators for the same function and all these decorators will 
# form Decorator Chaining

# def decor1(func):
#     def inner():
#         x=func()
#         return x*x
#     return inner

# def decor(func):
#     def inner():
#         x=func()
#         return 2*x
#     return inner


# @decor
# @decor1
# def num():
#     return 10

# print(num())


# #_____
# def decor(func):
#     def inner(name):
#         print("First decor function execution:")
#         func(name)
#     return inner

# def decor1(func):
#     def inner(name):
#         print("Second decor(decor1) function execution:")
#         func(name)
#     return inner

# @decor1
# @decor
# def wish(name):
#     print("Hello",name,"Good morning")

# wish("Vishal")




# l=(2 * x for x in range(10))
# print(l)
# print(type(l))

# for x in l:
#     print(x)

# Generators 
 
# Generator is a function which is responsible to generate a sequence of values. 
# We can write generator functions just like ordinary functions, but it uses yield keyword to 
# return values. 


def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'

g=mygen()
print(type(g))





######
def countdown(num):   
    print("Start Countdown")   
    while(num>0):   
        yield num   
        num=num-1   
    
values=countdown(12)  
for x in values:
    print(x)


#To generate first n numbers: 
def firstn(num):   
    n=1   
    while n<=num:   
        yield n   
        n=n+1   
    
values=firstn(5)   
for x in values:   
    print(x)  


######
def fib():   
     a,b=0,1 
     while True:   
        yield a   
        a,b=b,a+b   
for f in fib():   
     if f>100:   
        break   
     print(f) 


######################
#_______Advantages of Generator Functions_________:
# 1. when compared with class level iterators, generators are very easy to use 
# 2. Improves memory utilization and performance. 
# 3. Generators are best suitable for reading data from large number of large files 
# 4. Generators work great for web scraping and crawling.

#Generator vs normal collection wrt performance

import random   
import time   

names = ['Sunny','Bunny','Chinny','Vinny']   
subjects = ['Python','Java','Blockchain']   
    
def people_list(num_people):   
     results = []   
     for i in range(num_people):   
         person = {   
                     'id':i,   
                     'name': random.choice(names),   
                    'subject':random.choice(subjects)   
                   }   
         results.append(person)   
     return results   
    
def people_generator(num_people):   
     for i in range(num_people):   
         person = {   
                     'id':i,   
                     'name': random.choice(names),   
                     'major':random.choice(subjects)   


                    }   
         yield person   
    
''''t1 = time.perf_counter()  
people = people_list(10000000)  
t2 = time.perf_counter()''''' 
    
t1 = time.perf_counter()   
people = people_generator(10000000)   
t2 = time.perf_counter()  
    
print('Took {}'.format(t2-t1))



#Generators vs Normal Collections wrt Memory Utilization: 
#normal collection
l=[x*x for x in range(1000)]
print(l[29])


#Generators:
g=(x*x for x in range(100000))
print(next(g))







 
