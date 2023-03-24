#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Modules
#Users/rohitt/PycharmProjects/PythonTraining
"""
import mod
import sys
print(mod.my_lst)
print(mod.my_string)
print(mod.my_function)
print(sys.path)
"""

#sys.path.append(r'/Users/rohitt/PycharmProjects/PythonTraining/Week3)
#import mod2

#System Path (Windows Env Variables), Python Installed Directories, Same Directory

import re
import math

#print(mod.__name__,mod.__file__)
#print(re.__name__,re.__file__)
#print(math.__name__,math.__file__)

#print(pi)
print(math.pi)

#from mod import my_lst,my_function
#from mod import *
#from mod import my_lst as some_lst

#print(some_lst)

#my_function()

def main():
    import math
    print(math.pi)
    #from math import * --> Not correct
    #from math import pi --> This is okay
    
try:
    import mod2
except ModuleNotFoundError as:
    print(me)

print(dir())
import mod
print(dir())

mod.my_lst.append(4)
print(mod.my_lst)
#from mod import my_lst
#print(dir())
import mod

import importlib
importlib.reload(mod)


# In[ ]:


#mod
my_lst=[1,2,3]
my_string='This is a string in mod.py'
def my_function():
    print('This is my_fuction')
    
class Shape:
    pass

print(my_lst)

if __name__=='__main__':
    print(my_lst)
    print(my_string)
    my_function()


# In[25]:


#fact
import sys

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
if __name__=='__main__':
    if len(sys.argv)>1:
        print(sys.argv)
        print(fact(int(sys.argv[1])))
    else:
        print(fact(5))


# In[ ]:


#packages
#from newpkg import mod1,mod2 as mod3
#from newpkg.mod2 import mod2_function
#print(mod1.mod1_function())
#mod3.mod2_function

import newpkg

from newpkg.mod1 import *

newpkg.mod1.mod1_function()
newpkg.mod2.mod2_function()
import math
print(math.pi)

from newpkg.mod1 import pi
print(pi)


# In[ ]:


#newpkg/mod1
def mod1_function():
    print("This is the mod1 function")
    
class Circle:
    pass


# In[ ]:


#newpkg/mod2
def mod2_function():
    print("This is the mod1 function")
    
class Rectangle:
    pass


# In[ ]:


print("Initialisation happening for newpkg ", __name__)

import newpkg.mod1, newpkg.mod2


# 
# # Practise

# In[21]:


#1.
import os

def main():
    print(os.getcwd())
    with open("speech1.txt",'r') as f:
        no_of_lines=0
        no_of_words=0
        print(f)
        lines=f.read()
        print(lines)
        lines=lines.splitlines()
        print(lines)
        
        for line in lines:
            print(line)
            no_of_lines=no_of_lines+1
            words=line.split()
            no_of_words=no_of_words+len(words)
            
    print(no_of_lines)
    print(no_of_words)
        
if __name__=='__main__':
    main()


# In[22]:


#2.
import os

def main():
    print(os.getcwd())
    with open("speech2.txt",'r') as f:
        no_of_lines=0
        no_of_words=0
        print(f)
        lines=f.read()
        print(lines)
        lines=lines.splitlines()
        print(lines)
        
        for line in lines:
            print(line)
            no_of_lines=no_of_lines+1
            words=line.split()
            no_of_words=no_of_words+len(words)
            
    print(no_of_lines)
    print(no_of_words)
        
if __name__=='__main__':
    main()


# In[ ]:


#3.
import json
import codecs

def main():
    with open("sample.json","r") as f:
        json_dict=json.load(f)
    print('JSON Deserilization: ',json_dict)
    
if __name__=='__main__':
    main()


# In[ ]:




