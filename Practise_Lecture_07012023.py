#!/usr/bin/env python
# coding: utf-8

# # String

# In[ ]:


str1='nashik pune delhi'
#1.Print the 10th element of the string
print(str1[10])
#2.Print the substring starting from 9th element
print(str1[9:])
#3.Print the substring ending at 20th element
print(str1[:20])
#4.Check whether Pune is present in the string
if "Pune" in str1:
    print("Yes! it is present in the string")
else:
    print("No! it is not present")
#5.Check if Delhi is not in string
if "Delhi" not in str1:
    print("Yes! it is not present in the string")
else:
    print("No! it is present")
#6.Given a string, find all the duplicates characters which are similar
x=[]
for i in str1:
    if i not in x and str1.count(i)>1:
        x.append(i)
print(" ".join(x))


# # Function

# In[16]:


#1.Define a function that can receive two integral numbers in string form and compute their sum and then print it in console
def add():
    num1=input("num1:-")
    num2=input("num2:-")
    print(int(num1)+int(num2))
add()


# In[23]:


#2.Define a function that can accept two strings as input and print the string with maximum length in console.
#If two strings have the same length, then the function should print all strings line by line
def string1():
    str1=input("String1:-")
    str2=input("String2:-")
    if len(str1)>len(str2):
        print(str1)
    elif len(str1)==len(str2):
        print(str1,'\n',str2)
    else:
        print(str2)
string1()


# In[26]:


#3.Define a function that can accept an integer number as input and print the "It is an even number" if the number is even,
#otherwise print "It is an odd number".
def number():
    number=int(input("Number:-"))
    if number%2==0:
        print("It is an even number")
    else:
        print("It is an odd number")
number()


# In[28]:


#4.Define a function which can generate a dictionary where the keys are numbers between 1 and 20(both included) amd the values
#are square of keys. The function should just print the keys only
def dict1(number):
    d={}
    for i in range(1,number+1):
        d[i]=i**2
    return d
number=int(input("Enter the number:-"))
dict1(number)


# In[ ]:


#5.Write a function that has 1 argument which excepts any number of values and print those values in the function.
#e.g. func1(val1,val2), func(val1,val2,val3,val4)

