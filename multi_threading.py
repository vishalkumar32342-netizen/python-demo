#Multi_Threading

# from threading import *
# def display():
#     print('This code executed by Thread:',current_thread().name)

# t=Thread(target=display)
# t.start()
# print('This thread executed by thread:',current_thread().name)

#___Ways to create thread without using any class:
# from threading import *
# def display():
#     for i in range(10):
#         print('Child thread')
# t=Thread(target=display)
# t.start()
# for i in range(10):
#     print('Main thread')



#Create a thread by extending Thread class:
# from threading import *
# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             print('Child thread-1')
# t=MyThread()
# t.start()
# for i in range(10):
#     print('Main Thread')

#___Without extending thread class:____
# from threading import *
# import time
# class Test():
#     def display(self):
#         for i in range(10):
#             print('Child thread-2')
#             time.sleep(3)
# obj=Test()
# t=Thread(target=obj.display)
# t.start()
# for i in range(10):
#     print('Main thread-2')
#     time.sleep(2)


#___Normal flow of program____
# import time
# def double(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print('Double:',2*n)
# def squares(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print('squares:',n*n)
# numbers=[1,2,3,4,5,6]
# begintime=time.time()
# double(numbers)
# squares(numbers)
# endtime=time.time()
# print('The total time taken:',endtime - begintime)


# #___By multithreading program___
# from threading import *
# def double(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print('Double:',2*n)
# def square(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print('Sqares:',n*n)
# numbers=[1,2,3,4,5,6]
# t1=Thread(target=double,args=(numbers,))
# t2=Thread(target=squares,args=(numbers,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# begintime=time.time()
# double(numbers)
# square(numbers)
# endtime=time.time()
# print("the total time taken:",endtime-begintime)


#___Thread identification numbers(ident):_____
# from threading import *
# def display():
#     print('Child thread')
# t=Thread(target=display)
# t.start()
# print('Main thread Identification number:',current_thread().ident)

# print('Child thred Identification number:',current_thread().ident)


#____Active thread______
# from threading import *
# import time
# def display():
#     print(current_thread().name,'started----')
#     time.sleep(3)
#     print(current_thread().name,'ended----')
# print('The number of active threads:',active_count())
# t1=Thread(target=display,name='child thread-1')
# t2=Thread(target=display,name='child thread-2')
# t3=Thread(target=display,name='child thread-3')
# t1.start()
# t2.start()
# t3.start()
# # t1.join()
# # t2.join()
# print('The number of active threads:',active_count())
# time.sleep(10)
# print('The number of active threads:',active_count())

#____Join()____
# from threading import *
# import time
# def display():
#     for i in range(10):
#         print('Seetha Thread')
#         time.sleep(0.1)
# t=Thread(target=display)
# t.start()
# t.join()
# for i in range(10):
#     print('Ram Thread')
# l=enumerate()    #it list out all active thread
# for t in l:
#     print('Name:',t.name)
# print(t.name,'isAlive:',t.isAlive())     #is_alive() is used to check thread is active or not




