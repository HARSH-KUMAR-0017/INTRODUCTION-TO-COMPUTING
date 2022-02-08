#program1
enter=input("enter the input = ")
enter=enter.lower().strip()
l=0
dict={}
if " " not in enter:
    while l<len(enter):
        count=0
        y=0
        while y<len(enter):
            if enter[l]==enter[y]:
                count+=1
                y+=1
            else:
                y+=1
        dict[enter[l]]=count
        l+=1

else:
    list = str.split(enter)
    while l<len(list):
        count=0
        y=0
        while y<len(list):
            if list[l]==list[y]:
                count+=1
                y+=1
            else:
                y+=1
        dict[list[l]]=count
        l+=1
print('The total occurances')
for key,value in dict.items():
    print(key,"-",value)
print("------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------
#program 2
d=int(input("Enter the Date = "))
m=int(input("Enter the Month = "))
y=int(input("Enter the year = "))
if m in (1,3,5,7,8,10,12) and d>31:
    print("ERROR,INVALID DATE ENETERED")
elif m in (2,4,6,9,11) and d>30:
    print("ERROR,INVALID DATE ENETERED")
elif m==2 and d>28 and y%4!=0:
    print("ERROR,INVALID DATE ENETERED")
elif m==2 and d>29 and y%4==0:
    print("ERROR,INVALID DATE ENETERED")
elif d>31 or m>12 or m==0 or 2025<y or y<1800:
    print("ERROR,INVALID DATE ENETERED")
else:
    if d==31 and m==12:
        ny=y+1
    else:
        ny=y
    if m==12 and d==31:
        nm=1
    else:
        nm=m
    if m in (1,3,5,7,8,10,12):
        if d==31:
            nd=1
            if m!=12:
                nm=m+1
            else:
                nm=1
        else:
            nd=d+1


    elif m==2:
        if y%4==0:
            if d==29:
                nd=1
                nm=3
            else:
                nd=d+1
        else:
            if d==28:
                nd=1
                nm=3
            else:
                nd=d+1
    else:
        if d==30:
            nd=1
            nm=m+1
        else:
            nd=d+1
    print("The Next Date is: ",nd,"/",nm,"/",ny)
print("------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------
#program 3
l=int(input("enter the lower limit = "))
u=int(input("enter the upper limit = "))
tup=[(i,i**2) for i in range(l,u+1)]
print(tup)
print("------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------
# program 4
grade=int(input("enter the grade ="))
if grade==10:
    print("Your Grade is 'A+' and Outstanding Performance")
elif grade==9:
    print("Your Grade is 'A' and Excellent Performance")
elif grade==8:
    print("Your Grade is 'B+' and Very Good Performance")
elif grade==7:
    print("Your Grade is 'B' and Good Performance")
elif grade==6:
    print("Your Grade is 'C+' and Average Performance")
elif grade==5:
    print("Your Grade is 'C' and Below Average Performance")
elif 0<=grade<=4:
    print("Your Grade is 'D' and Poor Performance")
else:
    print("ERROR")
print(" ")
print("------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------
#program 5
n=6
for i in range(n,0,-1):
    for j in range(n-i-1,-1,-1):
        print(' ',end='')
    for k in range(2*i-1):
        print(chr(65+k),end='')
    print()

print("------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------
#program 6
cond=True
dict={}
show="y"
while cond:
    if show.upper()=="Y":
        sid=int(input("enter the SID of the student = "))
        name=input("enter the name of the student = ")
        dict[sid]=name
        show=input("Do you want to add more details? (Y/N) = ")
        cond=True
    else:
        cond=False
print("part a")
for key,value in dict.items():
    print(key,":",value)
print("\n")

print("part b")
sort=sorted(dict.values())
print("dictionary sorted by names = ",sort)
print("\n")

print("part c")
sort2=sorted(dict.keys())
print("dictionary sorted by SID = ",sort2)
print("\n")

print("part d")
src=int(input("enter the SID whose details you want to get = "))
if src in dict.keys():
    print("name of the student with SID ",sid,"is",dict[src])
else:
    print("SID not found")
print("\n")
print("------------------------------------------------------------------------------------------")
#-------------------------------------------------------------------------------------------------
# PROGRAM 7
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
s=0
x=int(input("enter the number of terms = "))
for i in range(1,x+1):
    print(fib(i),end=',')
    s=s+fib(i)
print('...')
print("the average of the above fibnocci series is = ",s/x)
print(" ")
print("------------------------------------------------------------------------------------------")
#---------------------------------------------------------------------------------------------------
# program 8
s1={1,2,3,4,5}
s2={2,4,6,8}
s3={1,5,9,13,17}
print("set1 = ",s1)
print("set2 = ",s2)
print("set3 = ",s3)
print("part a")
snb=s1^s2
print("Set of all the elements in set1 and set2 but not both is = ",snb)

print("part b")
sin=s1^s2^s3
print("Set of elements that are only in one of the three sets = ",sin)

print("part c")
sot=(s1|s2|s3)-(s1^s2^s3)-(s1&s2&s3)
print("set of elements present in exactly two sets = ",sot)

print("part d")
ns=set()
for o in range(1,11):
    ns.add(o)
nc=ns-s1
print("set of the integers from 1 to 10 that are not in set 1 = ",nc)

print("part e")
ns2=set()
for p in range(1,11):
    ns2.add(p)
nc2=ns2-(s1|s2|s3)
print("set of all the integers from 1 to 10 that are not in set 1,set 2 and set 3 = ",nc2)
