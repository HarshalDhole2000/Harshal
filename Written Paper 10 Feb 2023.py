#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1) Ram needs to convey his regards to his friends on friendship day he has almost 10 friends. 
#write a code for the above situation.
n=int(input("Enter the no. of Friend's:- "))
for i in range (n):
    n-=1
    n=n+i
print("Ram needs",n,"regards to convey his friends on friendship day!!!")


# In[ ]:


#2) Sita has scored good marks in exam.according the marks secured by sita check what grade she baged.
#85+ distinction, 75-85 - first class , 65-75 second class. except the marks from the user
marks=int(input("Enter Sita's marks:-"))
if marks>=85:
    print("Sita got distinction!")
elif marks>=75:
    print("Sita got First class!")
elif marks>=65:
    print("Sita got Second class")
else:
    print("Pass class!")


# In[ ]:


#3) Using nested for loop print the pattern
#**
#***
#****
#*****
#******
n=int(input("Enter the range:-"))
for i in range(2,n+1):
    for j in range(i):
        print("*",end="")
    print();


# In[ ]:


#4) Write a Python program which accepts the user's first and last name and print them in reverse order.
firstname=input("Enter your First Name:-")
lastname=input("Enter your Last Name:-")
print("Hello, "+lastname+" "+firstname)


# In[ ]:


#5) Write a Python program to get a new string from a given string where "Is" has been added to the front. 
#If the given string already begins with "Is" then return the string unchanged
string1=input("Enter the string:-")
starts_with=string1.startswith("Is")
if starts_with==False:
    print("Is",string1)
else:
    print(string1)


# In[ ]:


#6)Display Fibonacci series up to 10 terms
num1=0
num2=1
count=0
while count<10:
    print(num1)
    sum=num1+num2
    num1=num2
    num2=sum
    count=count+1


# In[ ]:


a={5,6,7}
print(a)
a.add(5)
print(a)


# In[ ]:


list1=[2,33,222,14,25]
list1[-1]


# In[ ]:


a=[1,2,3,4,5]
for i in range(1,5):
    a[i-1]=a[i]
for i in range (0,5):
    print(a[i],end=" ")


# In[ ]:


t1=(1,2,4,3)
t2=(1,2,3,4)
t1<t2


# In[ ]:


a,b,c=1,2,3
a,b,c


# In[ ]:


a,b=6,7
a,b=b,a
a,b


# In[ ]:


d1={"a":40,"b":45}
d2={"a":466,"b":45}
d1==d2


# In[ ]:


s1={1,2,3,8}
s2={3,4,5,6}
print(s1|s2)
s1.union(s2)


# In[ ]:


a={1:"A",2:"B",3:"C"}
del a
print(a)


# In[ ]:


a=(1,2)
b=(3,4)
c=a+b
c


# In[ ]:


n=set([1,1,2,3,3,3,4,4])
print(len(n))


# In[ ]:


s=0
l=[2,4,6,8,10]
for i in range(1,len(l),1):
    s=s+l[i]
print(s)


# In[1]:


d={"A":40,"B":45}
print(list(d.keys()))


# In[2]:


t=(1,2,4,3)
t[1:-1]

