#---LIST-------

#---empty list
# list=[]
# print(list)
# print(type(list))

# ------With dynamic input:
# list=eval(input("Enter list:"))
# print(list)
# print(type(list))

#----With list() function:

# l=list(range(0,10,2))
# print(l)
# print(type(l))

# s="vishal"
# l=list(s)
# print(l)

#---with split() function:
# s="Learning Python is very Easy!!!"
# l=s.split()
# print(l)
# print(type(l))


#----Accessing element of list

#---By using index:
list=[10,20,30,40]
print(list[3])

#---By using slicing
list=[10,20,30,40,40,30,20,20]
print(list[-3:2:1])

#---Traversing=The seqential access of each element in the list is called traversal.
#1.BY using while loop
n=[0,1,2,3,4,5,6,7,8,9]
i=0
while i<len(n):
    print(n[i])
    i=i+1

#2.BY using for loop
n=[0,1,2,3,4,5,6,7,8,9]
for n1 in n:
    print(n1)

#---To display only even number
n=[0,1,2,3,4,5,6,7,8,9]
for n1 in n:
    if n1%2==0:
        print(n1)


#---TO display element by index wise:
l=["A","B","C","D","E","F"]
x=len(l)
for i in range(x):
    print(l[i],"is available at positive index:",i,"and at negative index:",i-x)


#____IMPORTANT FUNCTION OF LIST
# 1__ TO get informaion about list

#1___len():
n=[10,20,30,40,50]
print(len(n))

#2_count():
n=[10,20,30,40,50]
print(n.count(10))

#3__index()function:
n=[10,20,30,40,50]
print(n.index(10))

#___Manipulating element of list:
#___Append() function
list=[]
list.append("V")
list.append("i")
list.append("s")
list.append("h")
list.append("a")
list.append("l")
print(list)



#___ To add  all elements to list upto 100 which are divisible by 10.

list=[]
for i in range(101):
    if i%10==0:
        list.append(i)
print(list)


#___insert() function:
n=[1,2,3,4,5,6]
n.insert(1,456)
n.insert(2,457)
print(n)

#___Extend () function:
order1=["chicken","mutton","egg","fish"]
order2=["kfc","rc","fo"]
order1.extend(order2)
print(order1)


#__remove() function:
order1=["chicken","mutton","egg","fish"]
order1.remove("chicken")
print(order1)

#___Pop() function
n=["chicken","mutton","egg","fish"]
print(n.pop(1))
print(n.pop(2))
print(n)

# n=[]
# print(n.pop())---------we get index error if list is empty




#____ORDERING ELEMENT OF LIST

#1__.reverse() function
n=["chicken","mutton","egg","fish"]
n.reverse()
print(n)

#___.sort() function

n=["chicken","mutton","egg","fish"]
n=[1,2,3,4,5,6,7,78]
n.sort()
print(n)

#___Aliasing and cloning of list object:
n=[40,20,50,60]
x=n
print(id(x))
print(id(n))


#___NESTED list
n=[40,20,50,[10,90],60]
print(n)
print(n[0])

#__NESted list as matrix:
n=[[10,20,30],[40,50,60],[70,80,90]]
print(n)
print("Elements of Row wise:")
for  r in n:
    print(r)
print("Elements of Matrix style:")
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end=' ')
    print()

#___LIST COPMREHENSION:

s=[x*x for x in range(1,11)]
print(s)
v=[2**x for x in range(1,6)]
print(v)
m=[x for x in s if x%2==0]
print(m)


#__Finding first element of every string:

words=["vishal","Bala","Venkatesh","Chiranjeevi"]
l=[w[0]for w in words]
print(l)


#__Finding last element of every string:
ords=["vishal","Bala","Venkatesh","Chiranjeevi"]
l=[w[-1]for w in words]
print(l)