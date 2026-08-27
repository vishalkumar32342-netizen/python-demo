#__Q. Write a program to access each character of string in forward and backward direction 
#__by using while loop?
s="Learning python is very easy!!! "
n=len(s)
i=0
print("Forward direction")
while i<n:
    print(s[i],end='')
    i+=1
print()
print("Backward direction")
i=-1
while i>=-n:
    print(s[i],end='')
    i=i-1


#_ANother method using slicing:
s="Learning python is very easy:"
print("Forward direction")
for i in s:
    print(i,end=' ')
print()

print("Forward direction")
for i in s[::]:
    print(i,end=' ')
print()

print("Backward direction")
for i in s[::-1]:
    print(i,end=' ')
print()

#__Checking membership:
s=input("Enter main string:")
subs=input("Enter sub string:")
if subs in s:
    print(subs,"is found in main string")
else:
    print(subs,"is not found in main string")

#___Comparison operator.
#_We can use comparison operators (<,<=,>,>=) and equality operators(==,!=) for strings. 
 
#__Comparison will be performed based on alphabetical order.

s1=input("Enter first sting:")
s2=input("Enter Second string:")
if s1==s2:
    print("Both string are equal:")
elif s1<s2:
    print("First string is less than Second string")
else:
    print("First string is greater than Second string")

#___Removing spaces from the string_________:
#__We can use the following 3 methods 
 
#1. rstrip()===>To remove spaces at right hand side 
#2. lstrip()===>To remove spaces at left hand side 
#3. strip() ==>To remove spaces both sides

name=input("Enter your name:")
sname=name.strip()
if sname=='vishal':
    print("hello VIshal...how are you")
elif sname=='kdflg':
    print("hello kdflg....where you are from")
elif sname=='bihar':
    print("heloo bihar ....who are you")
else:
    print("Your Entered name is wrong")

