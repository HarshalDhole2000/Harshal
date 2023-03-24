#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


number=int(input("Enter the number:-"))
fact=1
sum=0
for i in range(1,number+1):
    fact*=i
    sum+=fact
print("Factorial of",number,"is:-",fact)
print("Sum of factorial of",number,"is:-",sum)


# In[ ]:


num=int(input("Enter the number:-"))
str1=str(num)
str2=list(str1)
temp=num
digit=sum=0
for i in str2:
    digit=temp%10
    sum=sum+digit
    temp=temp//10
if num%sum==0:
    print(num,"is harshad number")
else:
    print(num,"is not harshad number")


# # Function

# In[ ]:


def calculator():
    num1=int(input("Enter the number1:-"))
    num2=int(input("Enter the number2:-"))
    op=input("Enter your operation:-")
    
    if op=="+":
        add=num1+num2
        print("Addition is:-",add)
    elif op=="-":
        sub=num1-num2
        print("Subtraction is:-",sub)
    elif op=="*":
        mult=num1*num2
        print("Multiplication is:-",mult)
    elif op=="/":
        div=num1/num2
        print("Division is:-",div)
    elif op=="**":
        power=num1**num2
        print("Power is:-",power)
    elif op=="%":
        mod=num1%num2
        print("Remainder is:-",mod)
    elif op=="//":
        floor=num1//num2
        print("Quotient is:-",floor)
    else:
        print("Enter valid operator")
        
calculator()


# In[ ]:


def factorial():
    num=int(input("Enter factorial number:-"))
    fact=1
    if num>0:
        for i in range(1,num+1):
            fact=fact*i
        print(fact)
    else:
        print("Enter positive values only!!!")
    
factorial()


# In[ ]:


def fact1(num):
    if num>=1:
        return num*fact1(num-1)
    else:
         return 1

num=int(input("Enter factorial number:-"))
fact1(num)


# In[ ]:


def pallindrome():
    word=input("Enter the value:-")
    if word==word[::-1]:
        print("String is palindrome")
    else:
        print("String is not palindrome")
        
pallindrome()


# In[ ]:


def ispalindrome(word):
    if pallindrome(word)==True:
        print("String is palindrome")
    else:
        print("String is not palindrome")
        
        
#word=input("Enter the value:-")
   


# In[ ]:


def sum_numbers(n=0):
    sum1=0
    for i in range(n+1):
        sum1+=i
    print(sum1)

n=int(input("Enter the number:-"))
sum_numbers(n)


# In[ ]:


def sum_1(n=0):
    if n>=1:
        return n+sum_1(n-1)
    else:
        return 0

n=int(input("Enter the number:-"))
sum_1(n)


# In[ ]:


x="Tushar"
y=(lambda x : print(x,"Hello"))(x)
y


# In[4]:


list1=[10,13,15,20,25,24,24,45,35]
def cube_root(n):
    return n**(1/3)

x=map(cube_root,list1)
list(x)


# In[2]:


from functools import *
def add(a,b):
    return a+b
list1=[10,13,15,20,25,24,24,45,35]
x=reduce(add,list1)
print(x)


# In[7]:


list1=[10000,124,500,134,435,500,567,235,533,642,632]
def withdraw(a,b):
    return a-b
x=reduce(withdraw,list1)
print(x)

