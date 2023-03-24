


# In[1]:


#1.Find the length of the dictionary
dict1={'Name':'Harshal', 'Age':22, 'Designation':'Programmer'}
print("Dictionary:",dict1)
print("Length of dictionary:",len(dict1))


# In[5]:


#2.Print the dictionary in sorted manner
dict1={'Name':'Harshal', 'Surname':'Dhole', 'Age':22, 'Designation':'Programmer'}
keys=list(dict1.keys())
sort1=keys.sort()
sorted_dict={i: dict1[i] for i in keys}
print(sorted_dict)


# In[ ]:


#3.Check whether the value is present in dictionary-create-print-print


# In[6]:


#4.Convert a tuple in dictionary
tuple1=[('A',1),('B',2),('C',3),('D',4),('E',5)]
dict1=dict(tuple1)
print(dict1)


# In[ ]:


#5.Create a dictionary student with student details
#Add elelments to students dictionary
#Delete one elements from student dictionary
#Return a element with key 101 from student dictionary
#Print only the keys from dictionary student
#Print only the values from dictionary students


# In[6]:


#6.Create a dict employee with ename as key and salary as value.
#.Print the employee dict
#.Delete the employee with salary 10000
dict1={"Harshal":24000,"Tushar":17000,"Adesh":10000,"Amar":29000,"Suyash":20000,"Aniket":9000}
print(dict1)
for keys,values in list(dict1.items()):
    if values<=10000:
        del dict1[keys]
print(dict1)


# In[14]:


dict1={'Name':'Harshal', 'Surname':'Dhole', 'Designation':'Programmer'}
print("Original dictionary is:-",dict1)
dict1['Age'] = 22
print("After adding elements:-",dict1)
del dict1["Surname"]
print("After removing element:-",dict1)
print("Elements of the dictionary are:-")
for i in dict1:
    print(i,"-",dict1[i])


# In[ ]:




