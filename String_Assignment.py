#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. WAP program to check whether given string is palindrome
string=input("Enter the string:-")
if string==string[::-1]:
    print("String is pallindrome")
else:
    print("String is not pallindrome")


# In[ ]:


#2. WAP program to count number of vowels in given string
string=input("Enter the string:-")
count=0
for i in string:
    if i in "aeiouAEIOU":
        count+=1
print(count)


# In[ ]:


#3. WAP to remove all occurences of given char from String
string=input("Enter the string:-")
char=input("Enter the character:-")
for i in string:
    if i != char:
        print("".join([i]))


# In[ ]:


#4. WAP to accept 2 string and check whether they are anagram or not eg) MARY ARMY
string1=input("Enter 1st string:-")
string2=input("Enter 2nd string:-")
str1=string1.lower()
str2=string2.lower()
if len(str1)==len(str2):
    sort1=sorted(str1)
    sort2=sorted(str2)
    if sort1==sort2:
        print(string1,"&",string2,"is anagram")
    else:
        print(string1,"&",string2,"is not anagram")
else:
    print(string1,"&",string2,"is not anagram")


# In[ ]:


#5. WAP to reverse each word in a sentence Python is fun -->nohtyP si nuf
string=input("Enter your string:-")
str1=string.split(" ")
for i in range(len(str1)):
    str1[i]=str1[i][::-1]
reverse=" ".join(str1)
print(reverse)


# In[ ]:


#6. WAP program to find frequency of each character in given String
string=input("Enter your string:-")
for i in string:
    print(i,":",string.count(i))


# In[ ]:


#7. WAP to extract first alphabet from given sentence to form a new word
string=input("Enter your string:-")
str1=string.split()
word=[]
for i in str1:
    word.append(i[0])
print(word)


# In[ ]:


#8. star Pattern Programs
number=int(input("Enter the number:-"))
for i in range(number):
    for j in range(i+1):
        print("*",end="")
    print()
    
#number=int(input("Enter the number:-"))
#for i in range(number,0,-1):
#    for j in range(i):
#        print("*",end="")
#    print()


# In[ ]:


#9. ABCDE
#ABCD
#ABC
#AB
#A
n=int(input("Enter the range:-"))
for i in range(n+65,65,-1):
    for j in range(65,i):
        print(chr(j),end="")
    print()


# In[ ]:


#10. WAP to replace every character by its next subsequent character
string=input("Enter the string:-")
string=list(string)
for i in range(len(string)):
    asc=ord(string[i])
    string[i]=chr(asc+1)
print(''.join(string))


# In[ ]:


#11. Write a Python program to count the number of characters (character frequency) in a string.
string=input("Enter your string:-")
for i in string:
    print(i,":",string.count(i))


# In[ ]:


#12. Write a Python program to remove the characters which have odd index values of a given string.
string=input("Enter your string:-")
str1=[]
for i in range(len(string)):
    asc=ord(string[i])
    if asc%2==0:
        str1.append(chr(asc))
print("".join(str1))


# In[ ]:


#13. Write a Python program to count the occurrences of each word in a given sentence.
string=input("Enter your string:-")
for i in string:
    print(i,":",string.count(i))


# In[ ]:


#14. Write a Python program to swap cases or toggle cases of a given string
string=input("Enter your string:-")
print(string.swapcase())

