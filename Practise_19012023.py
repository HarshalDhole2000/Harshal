#!/usr/bin/env python
# coding: utf-8

# In[2]:


num=int(input("Enter the number:- "))
sum=0
while num>0:
    n=num%10
    num=num//10
    sum=sum+n
print("Total sum of digits in given no.:- ",sum)


# In[ ]:


str1=input("Enter the string:-")
if str1[0]==("+") or str1[0]==("-"):
    x=str1[1:]
    if x.isdigit():
        print("string is number")
    else:
        print("string is not number")
elif str1.isdigit():
    print("string is number")
else:
    print("string is not number")


# In[ ]:


username=input("Enter the username:- ")#@vaibhav123 len=11
alpha=[]
digit=[]
space=[]
special=[]
if len(username)>=8: #11>=8
    if username[0]=="@": 
        un=username[1:]
        for letter in un:
            if letter.isalpha():
                alpha.append(letter)
            elif letter.isdigit():
                digit.append(letter)
            elif letter.isspace():
                space.append(letter)
            else:
                special.append(letter)

if len(username)>=8 and username[0]=="@":
    if len(alpha)>=1 and len(digit)>=1 and len(space)==0:
        print("Username is valid")
    else:
        print("Username is invalid")
        if len(alpha)<1:
            print("Please enter the alphabets")
        if len(digit)<1:
            print("Please enter the digits")
        if len(space)>0:
            print("Please remove the space")
else:
    if len(username)<8:
        print("Please enter more than 8 characters")
    if username[0]!="@":
        print("Please enter @ at the beginning")


# In[ ]:


str1=input("Enter you want:-")
if str1==str1[::-1]:
    print("String is pallindrome")
else:
    print("String is not pallindrome")# pallindrome=mirror


# In[ ]:


name=input("Enter you want:-")
print(name)
print(name[::-1])

