                                      #assignmneent 4
#program 1
print("program 1")
print("The steps to solve the THE TOWER OF HANOI with three disk where source rod,auxilary rod and destination rod are labelled as rod, 'A','B','C',respectively:")
def toh(n,s,d,a):#(n=number of disks)(s=source rod)(d=final rod)(a=auxilary rod)
    if n==0:
        return None
    else:
        toh(n-1,s,a,d)
        print("Move disk",n,"from rod",s,"to rod",d)
        toh(n-1,a,d,s)
toh(3,'A','C','B')
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------------------------
#program 2
print("program 2")
n=int(input("enter the number of rows u want in the pascal's triangle : "))
#using recusrion
print("using recusion")
def psc(n,s=n):
      if n==0:
            return None
      psc(n-1,s)
      print(' '*(s-n),end='')
      c=1
      for i in range(1,n+1):
            print(c,end=' ')
            c=c*(n-i)//i
      print()
psc(n)
#using iteration
print("using iteration")
for row in range(1,n+1):
      print(' '*(n-row),end='')
      t=1
      for i in range(1,row+1):
            print(t,end=' ')
            t=t*(row-i)//i
      print()
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------------------------
#program 3
print("program 3")
n=int(input("enter the dividend : "))
m=int(input("enter the divisor : "))
r=n%m
q=n//m
print("The remainder is : ", r)
print("The quotient is : ",q)
cl=callable(divmod(n,m))
if cl==True:
    print("fuction is callable")
if cl==False:
    print("fuction is not callable")
if q==0 and r==0:
      print("Both the values are zero")
if q!=0 or r!=0:
      if r!=0 and q!=0:
            print("Both the values are non zero")
      else:
            print("One of the values is zero")
s1=set()
for i in range (4,7):
    o=r+i
    p=q+i
    if(o>4):
        s1.add(o)
        print(s1)
    if(p>4):
        s1.add(p)
        print(s1)

print(s1)
s2=frozenset(s1)
print("immutable set : ", frozenset(s1))
print("the max value in the set : ", max(s2))
w=max(s2)
print("the hash value of the max value in the set : ", hash(w))
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------------------------
#program 4
print("program 4")
class Student:
       def __init__(self, student, sid):
             self.name = student
             self.sid = sid
       def __del__(self):
             print("The object created has been destroyed.")
s1=Student("Harsh Kumar",21105022)
print(s1.name,":",s1.sid)
del s1
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------------------------
#program 5
print("progran 5")
class Emp:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(self.name,"record is deleted")
e1=Emp("Mehak", 40000)
e2=Emp("Ashok", 50000)
e3=Emp("Viren", 60000)
print(e1.name,":",e1.salary)
print(e2.name,":",e2.salary)
print(e3.name,":",e3.salary)
#a part
e1.salary=70000
print("the updated salary of ",e1.name,":",e1.salary)
#b part
del e3
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------------------------
#program 6
print("program 6")
word = input("Enter the word: ")
new_word = input("Enter a new meaningful word rearranging the letters of the word entered by your friend to test your friendship: ")
def letter_count(word):
    count={}
    list_1= list(word)
    n=len(list_1)
    for i in range(n):
        if list_1[i] in count:
            count[list_1[i]]=count[list_1[i]]+1
        else:
            count[list_1[i]] = 1
    return count
if letter_count(word)!=letter_count(new_word):
    print("the number of letters used aren't same,thus friendship is fake!")

else:
      def forshopkeeper():
            ans = input("Does the word makes sense?(y or n)")
            if ans == 'y':
                  print("The friendship true!")
            elif ans == 'n':
                        print("The word doesn't have a meaning, friendship is fake!")
            else:
                  print("Invalid input, try again")
                  forshopkeeper()
      forshopkeeper()
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------------------------

