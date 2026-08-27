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
print("Forward diection")
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