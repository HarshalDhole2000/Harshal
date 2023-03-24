#!/usr/bin/env python
# coding: utf-8

# In[16]:


a=int(input("Enter the number:- "))
if(a%2==0):
    print(a," is even")
else:
    print(a," is odd")


# In[24]:


num=int(input("Enter the no.:- "))
sum=0
min=num
count=0
if(num>0):
    while num>0:
        n=num%10
        num=num//10
        sum=sum+n
        if(n<min):
            min=n
        count+=1
    print("Sum of digits in given no.:- ",sum)
    print("Minimun digit in given no.:- ",min)
    print("Total count of digits in given no.:- ",count)
else:
    print("Enter non-zero positive no.")


# In[26]:


sal=int(input("Enter basic salary amount of employee:- "))
hra=(sal*0.35)
da=(sal*0.25)
gross=sal+hra+da
print("Gross salary amount of employee:- ",gross)

if(gross>=200000):
    print("Given employee are VP")
elif(gross>=100000):
    print("Given employee are AVP")
elif(gross>=80000):
    print("Given employee are Manager")
elif(gross>=60000):
    print("Given employee are Asst. Manager")
else:
    print("Given employee are Officer")


# In[7]:


r=int(input("Enter the range:- "))
count=0
n1=0
n2=1
sum=0
while(count<r):
    print(sum)
    sum=n1+n2
    n1=n2
    n2=sum
    count+=1


# In[33]:


r=int(input("Enter the range:- "))
n1=0
n2=1
n3=0
while(n3<r):
    print(n3)
    n1=n2
    n2=n3
    n3=n1+n2
    

