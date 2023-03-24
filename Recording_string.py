#!/usr/bin/env python
# coding: utf-8

# In[1]:


s="I love python"
print(s)


# In[2]:


s='python'
print(s)


# In[4]:


s='''Hi,
I love python.
I have basic knowledge of python.'''
print(s)


# In[2]:


s1="Python "
s2="Java "
s2+s1


# In[5]:


"Hiii "*3


# In[9]:


8*"Hiii "


# In[8]:


s="Python"
print(s[2])#character
print(len(s))#length
print(s[-1])#last character
#String is immutale.


# In[6]:


name=input("Enter the name:- ")
for i in range(len(name)):
    print(i,"-->",name[i])


# In[26]:


#slicing
s="Python"
#s[start(0):stop/end(required):step(1)]
#s[2:len(s)]
#s[-1:-7:-2]
#s[1:len(s):2]
#s[::3]
#s[-6::2]
#s[len(s):-7:-1]
#s[::-1]
#s[-1:-6:-3]
s[7:1:-1]


# In[51]:


name=input("Enter the string:- ")
if name==name[::-1]:
    print(name,"is pallindrome")
else:
    print(name,"is not pallindrome")


# In[27]:


name=input("Enter the string:- ")
count=0
for i in name:
    if i in "aeiou":
        count+=1
print("No. of vowels:-",count)


# In[29]:


for i in 'harshal':
    print(i)


# In[59]:


#"a" in "harshal"
#'b' in 'harshal'
#"a" not in "harshal"
'b' not in 'harshal'


# In[4]:


s='My name is Harshal Dhole'
#s.capitalize()#--> convert first letter into capital

#s.title()#--> convert first letter of every word into capital
#s1=s.upper()#--> convert all letter into uppercase
#s1
#s2=s1.lower()#--> convert all letter into lowercase
#s2
#s.swapcase()#--> convert letter into alternative case
#s.count("a")#--> return how many occurrence are found
#s.find("er")#--> if find occurence then return their position else return -1 
#s.find("ar")
#s.isupper()#--> use to check string having uppercase or not
#s.islower()#--> use to check string having lowercase or not
#s.isalnum()#--> use to check string having alphanumeric or not
#s.isalpha()#--> use to check string having alphabets or not
#s.isdigit()#--> use to check string having digits/numeric or not
#s.strip()#--> use to remove spaces from both sides
#s.lstrip()#--> use to remove spaces from left side
#s.rstrip()#--> use to remove spaces from right side
#s.replace("My name is","Hello, I am")#--> use change the words
#s3=s.split()#--> convert the string into list of substring
#" ".join(s3)#--> to join the substrings and make a string
#"Hi,"+" I"+" am"+" Tushar" #--> only string data are concatenate by +
#l1=sorted(s)#--> sorting each elements in alphabetical format and return in list
#"".join(l1)
#s[::-1]
#list(reversed(s))#--> to return string in reverse format and return in list
#sorted(s,reverse=True)#--> sorting each elements in alternative of alphabetical format and return in list
#s.ljust(100,"*")#--> use to padding after string(right side of the string) upto certain length instead of string
#s.rjust(100,"*")#--> use to padding before string(left side of the string) upto certain length instead of string


# In[42]:


name='    My name is Harshal Dhole    '
#print(len(name))
#name.capitalize()-->0-position
#name.casefold()
#name.center(50)
#name.encode()
#name.endswith(" ")
#name.expandtabs()
#name.find("h")
#name.index("g")
#name.count("a")
#str.format()
name.format_map()

