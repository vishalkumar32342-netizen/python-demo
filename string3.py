#SPlitting of string
s="hii my name is vishal "
s=input("Enter any string:")
l=s.split()
for x in l:
    print(x)


# #joining of string:
r=('amit','ellisa','john','johnny')
s='-'.join(r)
print(s)

#Changing cases of string.
s='hii my name is Vishal I am from bihar'
s=input("Enter any string:")
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())

#checking starting and ending part of the string.
s='learning python is veyu easy'
print(s.startswith('learning'))
print(s.endswith('Easy'))
print(s.endswith('easy'))

#TO check type of character present in a string:
s=input("Enter any character:")
if s.isalnum():
    print("Alpha numeric character")
    if s.isalpha():
        print("Alphabet character")
        if s.islower():
            print("Lower case character")
        else:
            print("upper case character")
    else:
        print("It is digit")
elif s.isspace():
    print("It is space character")
else:
    print("Non space special character")

#FOrmatting of string
name='vishal'
salary=30000
age=23
print("{} salary is {} and his age is {}".format(name,salary,age))

#TO reverse the string:
#_1st way.

s=input("Enter some string:")
print(s[::-1])

#2nd way
s=input("Enter some string:")
print(''.join(reversed(s)))

#3rd way
s=input("Enter some string:")
i=len(s)-1
target=''
while i>=0:
    target=target+s[i]
    i=i-1
print(target)

#to reverse order of words:
s=input("Enter some string:")
l=s.split()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1
output=' '.join(l1)
print(output)

#Program to reverse Intenal content of each word.
s=input("Enter some string:")
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
output=' '.join(l1)
print(output)
