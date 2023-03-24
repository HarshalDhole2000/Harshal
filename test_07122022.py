#!/usr/bin/env python
# coding: utf-8

# In[4]:


#swapping integers without third variable
a=int(input("Enter 1st value:- "))
b=int(input("Enter 2nd value:- "))
a,b=b,a
print("Swapped value of a:- ",a)
print("Swapped value of b:- ",b)


# In[3]:


n=int(input("Enter the range:- "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j%2, end=" ")
    print()


# In[37]:


n=int(input("Enter the range:- "))

for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print("\n")


# In[16]:


n=int(input("Enter the no. of person's in the room:- "))
for i in range (n):
    n-=1
    n=n+i
print(n, "Handshakes possible in room")


# In[31]:


test=input("Enter the name:- ")
t=len(test)
test = test[-(t//2):-1] + test[-1].upper()
print(test)


# In[ ]:




