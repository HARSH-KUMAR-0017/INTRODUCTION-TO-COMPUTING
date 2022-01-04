#Assignment 1



                 #1st program
print("                   1st program")
#python program to find the avergage of the three numbers
num_1=float(input("enter the first number ="))
num_2=float(input("enter the second number ="))
num_3=float(input("enter the third number ="))
sum=num_1+num_2+num_3
avg=sum/3
print("the average of the numbers entered by you are=",avg)


               #2nd program
print("                     2nd program")
#program to find the a person's income tax
print('\n',"all tax payers are charged a flat tax rate of 20%",'\n',"all tax payers are allowed a $10000 standard deduction",'\n',"for each dependen, a taxpayer is allowed an additional $3000 deduction")
Gross_income=float(input("enter the gross income to the nearest penny ="))
std_ded=10000
dep=int(input("enter the number of dependents ="))
dep_ded=3000
taxable_income=Gross_income-std_ded-(dep_ded*dep)
print("Taxable income =$",taxable_income)
tax=(taxable_income*20)/100
print("the tax to be paid by the person is = $",tax)






            #3rd prograkm
print("                     3rd program")
#program to store different data types values into a list
sid=int(input("enter the sid="))
name=input("enter the name")
gender=input("enter the gender F/M=")
branch=input("enter the branch name=")
cgpa=float(input("enter the cgpa="))
st=[sid,name,gender,branch,cgpa]
print(st)





             #4th program
print("                      4th program")
#program to enter the marks of 5 students
m1=float(input("enter the marks of 1st student="))
m2=float(input("enter the marks of 2nd student="))
m3=float(input("enter the marks of 3rd student="))
m4=float(input("enter the marks of 4th student="))       
m5=float(input("enter the marks of 5th student="))
marks=[m1,m2,m3,m4,m5]
marks.sort()
print(marks)




             #5th program
print("                       5th program")
#5th question of assignment
color=['RED','GREEN','WHITE','BLACK','PINK','YELLOW']
COLOR1=[]
COLOR1.extend(color)
print("ORIGINAL LIST:",COLOR1)
COLOR1.pop(3)
print("LIST AFTER REMOVING 4TH ELEMENT:",COLOR1)
color[3:5]=['PURPLE']
print("LIST AFTER REPLACING BLACK AND PINK BY PURPLE:",color)

