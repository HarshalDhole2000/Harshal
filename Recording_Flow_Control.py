#!/usr/bin/env python
# coding: utf-8

# In[ ]:


10+20


# In[ ]:


a=10
type(a)


# In[ ]:


#Type conversion int, float, bool, hex(), oct(), bin()
height=float(input("Enter height:- "))
height


# In[ ]:


bool(0)


# In[ ]:


bool(56)


# In[ ]:


bool("Harshal")


# In[ ]:


hex(16)


# In[ ]:


bin(2)


# In[ ]:


age=int(input("Enter your age:- "))
if age>=18:
    print("You are eligible to vote...")
    print("Good luck")
else:
    print("You are not eligible to vote...")
print("Bye")


# In[ ]:


percentage=int(input("Enter your percentage:- "))
if percentage>=75:
    print("Distinction")
elif percentage>=60:
    print("First class")
elif percentage>=50:
    print("Second class")
else:
    print("Failed")
print("Good luck")


# In[ ]:


#Nested if
choice=input("Enter Desktop or Laptop:- ")
if choice=="Laptop":
    brand=input("Enter brand:- ")
    if brand=="Dell":
        print("Dell")
    else:
        print("Other laptop")
elif choice=="Desktop":
    print("Desktop")


# In[ ]:


a=int(input("Enter 1st no:- "))
b=int(input("Enter 2nd no:- "))
maxx= a if a>b else b
print(maxx)


# In[ ]:


age=int(input("Enter your age"))
print("Eligible to vote" if age>=18 else "Not eligible to vote")


# In[ ]:


for i in range(0,11,2):
    print(i)


# In[ ]:


for i in range(1,11):
    print(i,"-->",i*i)


# In[ ]:


for i in range(10,0,-1):
    print(i)


# In[ ]:


i=int(input("Enter the start point:- "))
n=int(input("Enter the range:- "))
while i<=n:
    print(i)
    i=i+1


# In[ ]:


i=5
while i>=1:
    print(i)
    i=i-1


# In[3]:


#Armstrong number
n=int(input("Enter the no:- "))
a=n
sum=0
while n>0:
    r=n%10
    sum=sum+(r**3)
    n=n//10
print(sum)
if sum==a:
    print("Given no is armstrong number.")
else:
    print("Given no is not armstrong number")


# In[ ]:


#Jump statements
i=1
while i<=10:
    i=i+1
    if i%2==0 and i%3==0:
        continue
    print(i)
    
#i=1
#while i<=10:
#    i=i+1
#    if i%2==0 and i%3==0:
#        break
#    print(i)


# In[ ]:


for i in range(1,11):
    if(i%3==0):
        break
    print(i)
    
#for i in range(1,11):
#    if(i%3==0):
#        continue
#    print(i)


# In[ ]:


for i in range(1,10):
    if(i%2==0):
        pass
    else:
        print(i)


# In[ ]:


for i in range(1,10):
    pass


# In[3]:


n=int(input("Enter the number:- "))
i=2
flag=1
while i<=n//2:
    if n%i==0:
        flag=0
        break
    i=i+1
if flag==1:
    print(n,"is prime number")
else:
    print(n,"is not prime number")


# In[6]:


for i in range(1,11):
    print(i)
    if(i==8):
        break
else:
    print("Completed successfully")


# In[12]:


n=int(input("Enter the number:- "))
i=2
while i<=n//2:
    if n%i==0:
        print(n,"is not prime number")
        break
    i=i+1
else:
    print(n,"is prime number")

