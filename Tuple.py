#!/usr/bin/env python
# coding: utf-8

# In[12]:


#1.WAP to create a nested tuple
tuple1=(3,4),
tuple2=(5,6),
print("The original tuple 1:-"+str(tuple1))
print("The original tuple 2:-"+str(tuple2))
result=tuple1+tuple2
print("Nested tuple is:-"+str(result))


# In[ ]:


#2.Provided a tuple with nested tuple, try to access the elements from the inner tuple
tuple1=((3, 4), (5, 6))
print(tuple1[0][0])
print(tuple1[0][1])
print(tuple1[0])
print(tuple1[1][0])
print(tuple1[1][1])
print(tuple1[1])


# In[16]:


#3.Given a tuple with nested list with 5 elements. Try to access the elements of list and modify elements of list.
#Add elements to the list and delete  1 element from the inner list
tuple1=(234,1223,[1,2,3,4,5,6,7],1,4)
print(tuple1[2][2])
tuple1[2][2]=10
print(tuple1)
tuple1[2].insert(3,9)
print(tuple1)
del tuple1[2][3]
print(tuple1)


# In[14]:


#4.Given a tuple with nested tuples.Iterate through the tuple to print 2nd element from every nested tuple
tuple1=((1,2,3),(4,5,6,7),(8,9,10))
for i in tuple1:
    print("Second elements of",i,"is",i[1])


# In[11]:


#5.Given a tuple, return the position of element "x"
tuple1=(1,2,3,4,5,6,7,8,9)
tuple1.index(3)


# In[ ]:


#6.Given a tuple, check how many times 'abc' occurs
tuple1=(ab,abc,abcd,abcabc,abfabctabcr)

