#!/usr/bin/env python
# coding: utf-8

# In[19]:


password=input("Enter the password:- ")
digit=[]
upper=[]
lower=[]
space=[]
special=[]
for letter in password:
    if letter.isdigit():
        digit.append(letter)
    elif letter.isupper():
        upper.append(letter)
    elif letter.islower():
        lower.append(letter)
    elif letter.isspace():
        space.append(letter)
    else:
        special.append(letter)

if len(digit)>=1 and len(upper)>=1 and len(lower)>=1 and len(space)==0 and len(special)>=1 and len(password)>=8:
    print("Strong password")
else:
    print("Weak password")
    if len(digit)==0:
        print("Please enter digit")
    if len(upper)==0:
        print("Please enter upper case letter")
    if len(lower)==0:
        print("Please enter lower case letter")
    if len(space)>=1:
        print("Please remove space")
    if len(special)==0:
        print("Please enter special character")
    if len(password)<8:
        print("Please enter at least 8 characters")


# In[30]:


#shift+tab--> docstring
str='harshal'
l1=[]
l1.extend(str)
print(l1)


# In[31]:


str='harshal'
l1=[]
for letter in str:
    l1.append(letter)
print(l1)


# In[32]:


str='harshal'
print([*str])

