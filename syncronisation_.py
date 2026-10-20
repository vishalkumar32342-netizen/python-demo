#___Syncronization______
#___If multiple thread are executing simultaneously then there may be a chance of data inconsistency problems.


from threading import *
import time
def wish(name):
    for i in range(10):
        print('Good Evening:',end='')
        time.sleep(3)
        print(name)
#wish('Vishal')
t1=Thread(target=wish,args=('Vishal',))
t2=Thread(target=wish,args=('Kohli',))
t1.start()
t2.start()


#___To overcome this problem 
#__At a time only one thread==>>Synchronization
#1.Lock
#2.RLock
#3.semaphore

#____Lock concept____
#___l=Lock()  class name

#___l.acquire() 
#     PERFORMING synchronized operations
#  l.release()


from threading import *
import time
l=Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print('Good Evening:',end='')
        time.sleep(1)
        print(name)
    l.release()
#wish('Vishal')
t1=Thread(target=wish,args=('Vishal',))
t2=Thread(target=wish,args=('Kohli',))
t3=Thread(target=wish,args=('Mohit',))
t4=Thread(target=wish,args=('Raina',))
t1.start()
t2.start()
t3.start()
t4.start()

#__without acquiring lock we cant release lock
from threading import *
l=Lock()
#l.acquire()
print('main threading releasing lock')
l.release()


#_____________RLock___________________________________________
#1._
from threading import *
l=RLock()
print('Main thread trying to acquire lock')
l.acquire()
print('main thread trying to acquire lock again')
l.acquire()
print('main thread acquire same lock again')


#___Lock concept ---there is no tracking mechanism which thread hold the lock.
#__1.Only one Thread.
#__2. no recursive


#___RLock---ther is a tracking mechanism is there which hold the lock.
#_____..if there is no any nested and recusrsion better to go Lock concept.
#__1.multiple holds
#__2.Recursive function

#__Example___
l=RLock()
l.acquire()==>got lock==>holds=1
l.acquire()==>got lcok==>holds=2
l.acquire()==>got lock==>holds=3

l.release()==>holds=>3-1=2
l.release()==>holds=>2-1=1
l.release()==>holds=>1-1=0



from threading import *
import time
l=RLock()
def factorial(n):
    l.acquire()
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    l.release()
    return result

def result(n):
    print('The factorial of',n,'is:',factorial(n))

t1=Thread(target=result,args=(5,))
t2=Thread(target=result,args=(9,))

t1.start()
t2.start()