#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1=[]
while True:
    str1=input()
    if str1=="":
        break
    else:
        list1.append(str1)
        
list1
for i in list1:
    list1.sort(key=len)
print("Sorted list is:-",list1)

