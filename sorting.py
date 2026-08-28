#input=BR439B9203
#output=BBR023399
s=input("Enter some string:")
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for  x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)
