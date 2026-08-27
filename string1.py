#What is String
#__Any sequence of character within either single quotes o double quotes is considered as a sting.


#___How to access characters of a string.
#___We can access characters of a sting by using the following ways:
#_1.BY USING INDEX.
#_2.BY USING SLICE OPERATOR.

S='durga'
print(S[0])
print(S[1])
print(S[2])
print(S[3])
print(S[4])

#__Q. Write a program to accept some string from the keyboard and display its characters by 
#__index wise(both positive and nEgative index)

s=input("Enter some string:")
i=0
for x in s:
    print("The character present at positive index{} and at negative index{} is {}".format(i,i-len(s),x))
    i=i+1

#__BY USING SLICE OPERATOR.
#__s[begin:end:step]
s="Learning Python is very easy!!!"
print(s[1:7:1])
print(s[0:1:7])
print(s[::-1])
print(s[:])

#Mathematical operator for strngs:
#_1. + operator for concatenation(To use +,both arguments should be str type)
#_2. * operator for repetition(To use *,one arguments should be str and other should be str)

print("vishal"+"raj")
print("vishal"*4)

#____LEN()IN-BUILT FUNCTION
s='vishal'
print(len(s))