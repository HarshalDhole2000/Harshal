#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. WAP to remove to find duplicates elements in list
list1=[1,2,3,1,2,4,5,1,2,3]
print("Original list:-",list1)
list2=set(list1)
print("After removing duplicates:-",list(list2))


# In[ ]:


#2. WAP to sort the given list
list1=[1,2,3,1,5,6,9,2,4,7,9,12,3654,88]
print("Original list:-",list1)
list1.sort()
print("Sorted list:-",list1)


# In[ ]:


#3. WAP to create a list such that new list contains alternate even and odd from given list
list1=[1,2,3,4,6,7,8,91,1,33,24,6,4,2,2,45]
even=[]
odd=[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even in list:-",even)
print("Odd in list:-",odd)


# In[ ]:


#4. Write a Python program to get the largest number from a list
list1=[1,23,54,3,5,6,32,4,6,5,3,99,43,2,54,32,15,43]
list1.sort()
print("Greatest number in the list is:-",list1[-1])


# In[ ]:


#5. Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.
string=input("Enter the string:-")
str1=list(string)
counter=0
for i in string:
    if len(str1)>=2 and str1[0]==str1[-1]:
        counter+=1
    else:
        print("Enter valid string")
        i==1
        break
print("Number of strings are:-",counter)


# In[ ]:


#6. Write a Python program to remove duplicates from a list.
list1=[1,2,3,5,1,2,4,6,7,5,1,8,2,3]
print("Original list:-",list1)
list2=set(list1)
print("After removing duplicates:-",list(list2))


# In[1]:


#7. Write a Python program to find the list of words that are longer than given words
string=input("Enter the string:-")
word=string.split()
list1=[]
for i in word:
    list1.append((len(i),i))
list1.sort()
print("The longer word in string is:-",list1[-1][1],"& its length is:-",list1[-1][0])


# In[ ]:


#8. Write a Python function that takes two lists and returns True if they have at least one common member
string1=input("Enter 1st string:-")
string2=input("Enter 2nd string:-")
list1=string1.split()
list2=string2.split()
result=False
for i in list1:
    for j in list2:
        if i==j:
            result=True
print(result)


# In[ ]:


#9. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
string=input("Enter the string:-")
word=string.split()
print("Original list:-",word)
list1=[]
for i in word:
    list1.append(i)
    i==0,4,5
    pass
print(list1)
#not done


# In[ ]:


#10. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#11. Expected Output : ['Green', 'White', 'Black']
list1=['Red','Green','White','Black','Pink','Yellow']
list2=[]
list3=[]
for i in list1:
    num=len(i)
    if num==5:
        list2.append(i)
print(list2)


# In[ ]:


#12. Write a Python program to print the numbers of a specified list after removing even numbers from it
list1=[1,2,3,4,5,6,7,89,11,32,5,4,642,32,15,54,66]
list2=[]
for i in list1:
    if i%2!=0:
        list2.append(i)
print(list2)

