#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=int(input("Enter no.:- "))
i=1
while i<=10:
    b=a*i
    i+=1
    print(b)


# In[19]:


a=int(input("Enter no.:- "))
for i in range(1,11):
    print(a*i)


# In[27]:


a=int(input("Enter 1st no.:- "))
b=int(input("Enter 2nd no.:- "))
c=int(input("Enter 3rd no.:- "))
if(a>b and a>c):
    print(a," is largest")
    print(id(a))
elif(b>c):
    print(b," is largest")
    print(id(a))
else:
    print(c,"is largest")
    print(id(a))

