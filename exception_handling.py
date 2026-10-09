#__In any programming language there are two types of error
#1.syntax errror --The error which occurs because of invalid syntax are called Syntax error.

# x=10
# if x==10
#     print("hello")
    
#2.Runtime error--While executing the program if something goes wrong because of user end such type of error are called Runtime error.
# print(10/0)--zero division errror
# print(10/"nine")--Type error

#__Exeption
#__An unwanted and unexcepted event that disturb normal  flow of program is called exception.

#__EXCEPTION HANDLING--Graceful termination of the program.
#--Exception handling does not mean repairing exception. We have to define alternative way 
#-- to continue rest of the program normally.

#--Customized Exception Handling by using try-except: 
#--Try--risky code
#--except--handling code
#finally--cleaning of code

# print("stmt-0")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(10/2)


#--EXercise for calculator
# try:
#     a=eval(input("enter first number:"))
#     b=eval(input("enter Second number:"))
#     operator= input("Enter operator(+,-,*,/): " )

#     if operator =='+':
#         result= a+b

#     elif operator=='-':
#         result=a-b

#     elif operator=='*':
#         result=a*b

#     elif operator=='/':
#         result=a/b

#     else:
#         print("Invalid oprator")

# except ValueError:
#     print("Enter valid numbers:")

# except ZeroDivisionError:
#     print("cannot divide by zero:")

# else:
#     print("Result:",result)

# finally:
#     print("Calculator program finished:")


#---EXercise

# try:
#     numbers=[10,20,30,50]
#     a=int(input("Enter index number:"))
#     b=int(input("enter divisor:"))

#     print(numbers[a] / b)

# except ValueError:
#     print("enter valid numbers:")
# except ZeroDivisionError:
#     print("cannot divide by zero:")
# except IndexError:
#     print("plz provide right index:")

# else:
#     print("numbers",numbers)
# finally:
#     print("program completed")

#--Exercise-3

# try:
#     age=int(input("enter your age:"))

#     if age < 0:
#         raise ValueError("Age cannot be negative:")
#     if age > 100:
#         raise ValueError("You are too old, go die:")
    
#     print(" valid age",age)
# except ValueError as e:
#     print(e)


#--Exercise
# try:
#     name=input("Enter students name:")
#     marks=float(input("Enter student's marks:"))

#     if marks > 90:
#         print('A+')
#     elif marks >80:
#         print('B+')
#     elif marks > 70:
#         print('C+')
#     elif marks > 60:
#         print('D')
#     elif marks >40:
#         print("pass")
#     else:
#         print("better luck next time")
# except ValueError:
#     print("Invalid number:") 



import logging

logging.basicConfig(level=logging.INFO)

logging.info("This is an information message")
logging.warning("This is a warning")
logging.error("This is an error")
        