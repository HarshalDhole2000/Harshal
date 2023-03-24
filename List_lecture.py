#!/usr/bin/env python
# coding: utf-8

# In[ ]:


l1=[4,5,6,7,8,9,10]
l2=[i**2 for i in l1]
l2


# In[ ]:


l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
a=zip(l1,l2)
l3=[i+j for (i,j) in a]
l3


# In[5]:


d1=[1,2,3,4,5,6]
d2=[1,2,3,4,5,6]
d3=[i+j for i in d1 for j in d2]
d4=[]
for k in d3:
    if k>6:
        d4.append(k)
print(d4)
probability=len(d4)/len(d3)
print("Probability is:-",probability)


# In[4]:


coin1=["H","T"]
coin2=["H","T"]
h=0
coin3=[i+j for i in coin1 for j in coin2]
for k in coin3:
    a=k.count("H")
    b=k.count("T")
    if a==1:
        h+=1
prob=(h/len(coin3))
print("Probability of H is:-",prob)


# In[ ]:


list1=[1,2,3,4,5,6,7,8]
print(list1)
list1.append(10)
print(list1)
list1.append([11,12,13,14,15])
print(list1)
list1.extend([16,17,18,19,20])
print(list1)
list1.insert(1,21)
print(list1)


# In[ ]:


l1=[1,2,3,4,5]
l1.reverse()


# In[ ]:


s1={1,2,3,4,5,6}
s2={5,6,7,8,9,0}
s1.add(8)
s1.update()
s1


# In[16]:


d1=[1,2,3,4,5,6]
d2=[1,2,3,4,5,6]
d3=zip(d1,d2)
d4=[]
for i,j in (d3):
    k=i+j
    d4.append(k)
    print(k)


# In[12]:


d1=[1,2,3,4,5,6]
d2=[1,2,3,4,5,6]
for i in d1:
    for j in d2:
        k=i+j
        print(k)

