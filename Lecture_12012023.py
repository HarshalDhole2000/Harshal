#!/usr/bin/env python
# coding: utf-8

# In[ ]:


radius=int(input("Enter the radius:- "))
pi=3.14
area=pi*radius**2
print("Area of circle with",radius,"is",area)


# In[ ]:


emp_name=input("Enter employee name:-")
emp_id=int(input("Enter employee id:-"))
basic_salary=int(input("Enter the salary:-"))
hra=0.20*basic_salary
dra=0.30*basic_salary
gross_salary=basic_salary+hra+dra
print("Gross salary of employee",emp_name,"with employee id",emp_id,"is",gross_salary)


# In[ ]:


print("Welcome to the bank")
name=input("May I have your name?")
ac_no=int(input("May I have your account number?"))
ac_bal=int(input("Please enter the account balance:-"))
print("Initial account balace of",ac_no,"with name",name,"is:-",ac_bal)
transaction=int(input("Enter the amount:-"))
new_bal=ac_bal+transaction
print("Thanks for choosing the bank!")
print("Transaction is completed",new_bal,"is updated balance.")


# In[ ]:


#conditional statements
marks=int(input("Enter the marks:-"))
if marks>35:
    print("Congratulations you have passed!")
else:
    print("Unfortunately you have failed")


# # types of conditional statements
# #if--> one conditon
# #if-else--> two condition
# #elif--> else if
# #nested if-else
# 

# In[ ]:


num=int(input("Enter the number:-"))
if num%2==0:
    print(num,"is even number")
else:
    print(num,"is odd number")


# In[ ]:


num=int(input("Enter the number:-"))
if num>0:
    print(num,"is positive number")
elif num==0:
    print(num,"is zero")
else:
    print(num,"is negative")


# In[ ]:


marks=int(input("Enter the marks:-"))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=35:
    print("Grade D")
else:
    print("Grade F")


# In[3]:


#Simple calculator
num1=int(input("Enter the number1:-"))
num2=int(input("Enter the number2:-"))
print("Options are-->1-Addition, 2-Subtraction, 3-Multiplication, 4-Division")
choice=int(input("Enter the option:-"))
if choice==1:
    print("Addition of",num1,"&",num2,"is",num1+num2)
elif choice==2:
    print("Subtraction of",num1,"&",num2,"is",num1-num2)
elif choice==3:
    print("Multiplication of",num1,"&",num2,"is",num1*num2)
elif choice==4:
    print("Division of",num1,"&",num2,"is",num1/num2)
else:
    print("Invalid option")


# In[ ]:


marks=int(input("Enter the marks:-"))
if marks>=35:
    if marks>=90:
        print("Your grade A")
    elif marks>=75:
        print("Your grade B")
    elif marks>=60:
        print("Your grade C")
    else:
        print("Your grade D")
    print("Congratulations you have passed")
else:
    print("Hard Luck! You failed!")

