#s1=vishal
#s2=Raj
#output=vRiasjhal

s1=input("enter first string:")
s2=input("enter second string:")
output=''
i=j=0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
print(output)


# ----Write a program to sort the characters of the string and first alphabet symbols 
#-----------followed by numeric values 
#---input=B4A1d3
#---output=ABD134

s=input("Enter some string:")
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)


#--- Write a program for the following requirement  
 
#input: a4b3c2 
#output: aaaabbbcc 

s=input("Enter somes string:")
output=''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+previous*(int(x)-1)
print(output)

#---. Write a program to perform the following activity 
 
#---input: a4k3b2 
#---output:aeknbd 

s=input("Enter some string:")
output=''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+chr(ord(previous)+int(x))
print(output)


#---Write a program to remove duplicate characters from the given input string? 
 
#---input: ABCDABBCDABBBCCCDDEEEF 
#----output: ABCDEF

s=input("Enter some string:")
l=[]
for x in s:
    if x not in l:
        l.append(x)
output=''.join(l)
print(output)

#-- Write a program to find the number of occurrences of each character present in the 
#given String? 
 
#input: ABCABCABBCDE 
#output: A-3,B-4,C-3,D-1,E-1
# s=input("Enter the some dtring")

s=input("Enter the some string: ")
d={}
for x in s:
    if x in d.keys():
        d[x]=d[x]+1
    else:
        d[x]=1
for k,v in d.items():
    print("{}={}times".format(k,v))
