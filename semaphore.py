#____Semaphore________(Synchronization concept)
#__s=Samaphore(countValue)
from threading import *
import time
s=Semaphore(5)
def wish(name):
    s.acquire()
    for i in range(10):
        print('Good Evening:',end='')
        time.sleep(0.5)
        print(name)
    s.release()
t1=Thread(target=wish,args=('Dhoni',))
t2=Thread(target=wish,args=('Yuvi',))
t3=Thread(target=wish,args=('Kohli',))
t4=Thread(target=wish,args=('Rohit',))
t5=Thread(target=wish,args=('Pandya',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

#___BoundedSemaphore:_______
#__No of release call should not be exceeds with acquire calls.

