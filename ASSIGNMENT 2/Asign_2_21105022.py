print('\tprogram 1')
st="Python is a case sensitive language"
#part a
print("length of the string is=",len(st))
#part b
print("printing string in reverse=",st[::-1])
#part c
st2=st[10:26]
print(st2)
#part d
st3=st.replace("a case sensitive","object oriented")               #program 1
print(st3)
#part e
ind=st.index("a")
print("index of (a) is =",ind)
#part f
wh=st.replace(' ','')
print("string without white spaces=",wh)
#--------------------------------------------------------------------------------------------------------------------------------------------

print( "\tprogram 2")
'\n'
name="Harsh Kumar"                                               #program 2
sid=21105022
dept="ECE"
cgpa=9.9
print("Hey, %s Here!"%(name),'\n'"My SID is %d"%(sid),'\n'"I am from %s department"%(dept),"and my CGPA is %f"%(cgpa))

#--------------------------------------------------------------------------------------------------------------------------------------------

print("\tprogram 3")
a=56
b=10
print("a =",a)
print("b =",b)
print("binary representation of a=",bin(a))
print("binary representation of b=",bin(b))                       #program 3
print("a&b=",a&b)
print("a|b=",a|b)
print("a^b=",a^b)
print("Left shift both a and b with 2 bits"'\n',"a<<2=",a<<2,'\n',"b<<2=",b<<2)
print("Right shift a with 2 bits and b with 4 bits"'\n',"a>>2=",a>>2,'\n',"b>>4=",b>>4)

#--------------------------------------------------------------------------------------------------------------------------------------------

print("\tprogram 4")
num1=float(input("enter a first number="))
num2=float(input("enter the second number="))
num3=float(input("enter the third number="))                    #program 4
maxi=num1
if num2>maxi:
    maxi=num2
if num3>maxi:
    maxi=num3
    print("greatest number is",num3)
else:
    print("greatest number is ",maxi)


#--------------------------------------------------------------------------------------------------------------------------------------------

print("\tprogram 5")
str=input("enter the string : ")
if "name" in str:
    print("yes")                                               #program 5
else:
    print("no")

#--------------------------------------------------------------------------------------------------------------------------------------------

print("\tprogran 6")
a=float(input("enter the first side length="))
b=float(input("enter the second side length="))               #program 6
c=float(input("enter the third side length="))
if a+b>c and b+c>a and c+a>b:
    print("can a triangle can be formed with the above given sides = Yes") 
else: 
    print("can a triangle can be formed with the above given sides = No")
