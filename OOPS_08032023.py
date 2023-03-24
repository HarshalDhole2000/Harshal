#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Generators
import sys
import cProfile

def inf_seq():
    num=1
    while True:
        if num%47==0:
            print("Inside if: ",num)
            i=(yield num)
            if i is not None:
                print("i: ",i)
                num=i
            else:
                print("i:none")
        num=num+1
        #print(num)
        
def finite_seq():
    num=1
    while True:
        return num
        num=num+1
        
def yield_example():
    str1="This is first yield"
    yield str1
    str2="This is second yield"
    yield str2
    str3="This is third yield"
    yield str3
    
def main():
    my_list=[i for i in range(1,6)]
    print(my_list)
    
    #print(finite_seq())
    """
    for num in inf_seq():
        print(num)
        
    gen_obj=inf_seq()
    print(next(gen_obj))
    print(next(gen_obj))
    print(next(gen_obj))
    print(next(gen_obj))
    print(next(gen_obj))
    
    list_comp=[i for i in range(1,10000)]
    gen_comp=[i for i in range(1,10000)]
    
    print(sys.getsizeof(list_comp))
    print(sys.getsizeof(gen_comp))
    
    cProfile.run("sum([i for i in range(1,10000)])")
    cProfile.run("sum((i for i in range(1,10000))")
    
    gen_obj=yield_example()
    print(next(gen_obj))
    print(next(gen_obj))
    print(next(gen_obj))
    print(next(gen_obj))
    """
    
    inf_obj=inf_seq()
    num=inf_obj.send(None)
    while True:
        print("The num divisible by 47 is: ",num)
        num=inf_obj.send(num*10)
        print("num: ",num)
        if num>10000:
            inf_obj.close()
            break
            
if __name__=="__main__":
    main()


# In[17]:


#Decorators
def fuction_one():
    return "This is fuction one"

def fuction_two():
    def fuction_three():
        return "This is fuction three"
    return function_three

def fuction_four():
    string="This is function four"
    def fuction_five():
        return string +" "+"and fuction five"
    return function_five

def convert_to_upper(function):
    def inner_logic():
        func=function()
        updated_func_val=func.upper()
        return updated_func_val
    return inner_logic

def split_the_string(function):
    def inner_logic():
        func=function()
        updated_func_val=func.split()
        return updated_func_val
    return inner_logic

@split_the_string
@convert_to_upper
def hello_world():
    return "Hello to the world"

def main():
    """
    f1=function_one
    print(f1())
    f2=function_two
    print(f2())
    f4=function_four
    print(f4())
    """
    print(hello_world())
    
if __name__=="__main__":
    main()


# # Practise

# In[19]:


from functools import reduce


# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]


# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]


# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]


# Fix all three respectively.
map_result = list(map(lambda x: round(x**2,3), my_floats))
filter_result = list(filter(lambda name: len(name)<=7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)


print(map_result)
print(filter_result)
print(reduce_result)


# In[18]:


#1.Write a Python program to triple all numbers in a given list of integers, use map.
list1=[1,2,3,4,5,6,7,8,9]
print(list(map(lambda x: x*3,list1)))


# In[20]:


#2.Write a Python program to add three given lists using Python map and lambda
list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]
print(list(map(lambda x1,x2,x3:x1+x2+x3,list1,list2,list3)))


# In[33]:


#3.Write a Python program to convert a given list of integers into a list of strings. Use map and lambda
list1=[1,2,3,4,5,6,7,8,9]
print(list(map(lambda x:str(x),list1)))
print(list(map(str,list1)))


# In[38]:


#4.Using the filter function, filter the even numbers so that only odd numbers are passed to the new list.
list1=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2!=0,list1)))


# In[40]:


#5.Using filter() function filter the list so that only negative numbers are left.
list1=[-1,2,-3,4,-5,-6,7,8,-9]
print(list(filter(lambda x: x<0,list1)))


# In[44]:


#6.Using filter() and list() functions and .lower() method filter all the vowels in a given string 
#str = "Winter Olympics in 2022 will take place in Beijing China”
string = "Winter Olympics in 2022 will take place in Beijing China"
print(list(filter(lambda x: x.lower() in 'aeiou',string)))


# In[61]:


#7.Using map() and filter() functions add 2000 to the values below 8000 for lst1 = [1000, 500, 600, 700, 5000, 90000, 17500]
list1 = [1000, 500, 600, 700, 5000, 90000, 17500]
print(list(map(lambda x:x+2000,filter(lambda x: x<8000,list1))))


# In[67]:


#8.Use reduce to find the average of all numbers in a list
list1=[1,2,3,4,5,6,7,8,9,9]
print(reduce(lambda x,y:x+y,list1)/len(list1))


# In[71]:


#9.Find the max number in a list using reduce
list1=[1,2,3,4,5,6,7,8,9,9]
print(reduce(max,list1))


# In[74]:


#10.Filter only negative and zero in the list using list comprehension numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_no=[i for i in numbers if i<=0]
print(filter_no)


# In[4]:


#11.Flatten the following list of lists of lists to a one dimensional list :
#list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]] output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
x=[k for i in list_of_lists for j in i for k in j]
print(x)

