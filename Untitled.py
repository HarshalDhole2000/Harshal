#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Given a string of words separated by spaces, write a function to reverse the order of the letters in each words.
#	input: HELLO MY NAME IS JHON
#	output: OLLEH YM EMAN SI NOHJ

string1=input("Enter the string:-")
split_string=[]
temp=''
for word1 in string1:
    if word1==' ':
        split_string.append(temp)
        temp=''
    else:
        temp=temp+word1
if temp:
    split_string.append(temp)

string2=[]
for word2 in split_string:
    string2.append(word2[::-1])

string3=''    
for word3 in string2:
    string3=string3+' '+word3
print(string3)


# In[ ]:




