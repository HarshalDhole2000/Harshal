#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and
#a tuple of those numbers.Sample data : 3, 5, 7, 23-- Output :List : ['3', ' 5', ' 7', ' 23'],Tuple : ('3', ' 5', ' 7', ' 23')
n=input("Enter some comma separated values:-")
sample=n.split(",")
print("List of given sequence is:-",list(sample))
print("Tuple of given sequence is:-",tuple(sample))


# In[ ]:


#2.Write a Python program to calculate the difference between a given number and 17. 
#If the number is greater than 17, return twice the absolute difference.
num1=int(input("Enter the number:-"))
num2=17
diff=num1-num2
if num1>num2:
    print("Absolute difference is:-",2*diff)
else:
    print("17 is greater than",num1)


# In[ ]:


#3.Python program to find the sum of the digits of an integer using a while loop
num=int(input("Enter the number:-"))
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
     num=num%10
print("Sum of all digit of",num,"is:-",sum)


# In[10]:


#4.Python program to check whether the given integer is a prime number or not
num=int(input("Enter the number:-"))
if num%i!=0:
    print(num,"is prime")
    i=i+1
else:
    print(num,"is not prime")


# In[14]:


#5.Python program to generate the prime numbers from 1 to N
n=int(input("Enter the range for generate prime number:-"))
for num in range(1,n+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)


# In[38]:


# 6.Python program to print the numbers from a given number n till 0 using recursion

def reverse(num):
    print(num)
    if num==0:
        pass
    else:
        return reverse(num-1)
num=int(input("Enter the range:-"))
reverse(num)


# In[46]:


#7.Python program to find the largest number in a list without using built-in functions
list1=[1,11,23,564,6764,124,865,1234,6541,56,9878]
def greater(list1):
    large=list1[0]
    for i in list1:
        if i>large:
            large=i
    return large
greater(list1)


# In[48]:


#8.Python program to insert a number to any position in a list
list1=[1,11,23,564,6764,124,865,1234,6541,56,9878,34,53,553,7,543,222]
index=int(input("Enter the position:-"))
number=int(input("Enter the number:-"))
print("Original list is:-",list1)
list1.insert(index,number)
print("List after insert new number:-",list1)


# In[51]:


#9.Python program to check leap year
year=int(input("Enter the year:-"))
if year%400==0 and year%100==0 or year%4==0:
    print(year,"is Leap year")
else:
    print(year,"is not Leap year")


# In[52]:


#10.Write a Program to extract each digit from an integer in the reverse order
num=int(input("Enter the number:-"))
temp=num
rev=0
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
print("Reverse of",num,"is",rev)


# In[61]:


list1=['harshal','tushar','sham','ram','vaibhav','sunny','shubham']
def palindrome(str1):
    if str1==str1[::-1]:
        return True
    else:
        return False

print(list(filter(palindrome,list1)))


# In[66]:


list1=['harshal','tushar','sham','ram','vaibhav','sunny','shubham']
def convert(str1):
    return str1.title()
print(list(map(convert,list1)))

