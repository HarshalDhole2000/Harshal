#!/usr/bin/env python
# coding: utf-8

# In[3]:


from functools import reduce
def function_one():
    print("I am function one")

def function_two():
    return function_one

def function_three(x):
    return x, x**2, x**3

def function_four(x):
    return abs(x)

def function_five(a,b,c):
    return a+b+c

def function_six(x):
    if x%2 ==0:
        return False
    return True

def function_seven(a,b):
    return a+b

def main():
    """
    another_name = fuction_one
    another_name()
    my_list = [1,"string",function_one]
    my_list[2]()
    print(function_one)
    # function composition
    (function_two())()
    my_list_2 = ["ram", "rohit", "ansari", "aman", "surabhi"]
    print(sort(my_list_2))
    print(sorted(my_list_2, key=len))
    """
    #lamda
    lambda_ex = (lambda x: x**2)
    print(lambda_ex(5))
    print((lambda x: x + 10)(90))
    my_list_2 = ["ran", "rohit", "ansari", "aman", "surabhi"]
    print(sorted(my_list_2, key=lambda x: -len(x)))
    
    #multiple values
    print(function_three(3))
    
    lambda_multiple = (lambda x: [x, x * 2, x * 3])
    print(lambda_multiple(4))
    lambda_multiple = (lambda x: (x, x*2,x*3))
    print(lambda_multiple(4))

    #map:(map(function/operation, list/iterable))
    my_list_3 = [1,-4,7,-10,101,-123]
    map_lambda_obj = map(function_four, my_list_3)
    print("Lambda method abs: ",list(map_lambda_obj))
    for item in map_lambda_obj:
        print(item)
    map_output =list(map(function_four, my_list_3))
    print(map_output)
    
    #map multiple iterables
    list1 = [1,2,3,4,5]
    list2 = [6,7,8,9,10]
    list3 = [11,12,13,14,15]
    print(map(function_five, list1,list2,list3))
    print(list(map(lambda x1,x2,x3: x1 + x2 + x3, list1, list2, list3)))
    
    #filter
    list4 = []
    for i in range(1,101,1):
        list4.append(i)
    #print(list4)
    print(list(filter(function_six, list4)))
    print(list(filter(lambda x: x%2 == 1, list4)))
    
    #reduce
    list5 = []
    for i in range(1,11,1):
        list5.append(i)
    print(list5)
    print(reduce(function_seven, list5))
    print(reduce(function_seven, list5, 10))
    print("List5 is: ", list5)
    print(sum(list5))
    
    #List comprehension
    list6 = []
    for i in range(1, 51, 1):
        list6.append(i)
    print(list6)
    list7 = [itr for itr in range(1,51,1)]
    print(list7)
    list8 = [i + j for i in range(1,10) for j in range(1,10) if i == j]
    print(list8)
    
    #dictionary comprehension
    my_dict ={i: i ** 3 for i in range(1,10) if i%2 ==0}
    print(my_dict)
    
    #set comprehension
    duplicates_list = [1,2,3,4,4,5,5,5]
    my_set = {i for i in duplicates_list if i%2 ==1}
    print(my_set)
    my_tuple = (i for i in range(1,10))
    for i in my_tuple:
        print(i)
    #print(my_tuple)
    
if __name__=="main__":
    main()


# # Practise 

# In[17]:


#1.Define any class of your choice and use these keywords to introspect your object: 
#dir, id, type, hasattr(), getattr(), __repr__, __doc__, __name__
class Car:
    def __init__(self,company_name,model,year_of_release,price):
        self.company_name=company_name
        self.model=model
        self.year_of_release=year_of_release
        self.price=price
        
    def print_car_details(self):
        print("Company name: ",self.company_name,"\tModel: ",self.model,"\tYear of market release: ",self.year_of_release,"\tPrice: ",self.price)

    def __repr__(self):
        return "Car attributes: ",self.company_name,self.model,self.year_of_release,self.price
        
def main():
    c1=Car("Tata","Punch",2020,600000)
    c1.print_car_details()
    print(dir(c1))
    print(id(c1))
    print(type(c1))
    print(hasattr(c1,"print_car_details"))
    print(getattr(c1,"model"))
    #print(repr(c1))
    #print(c1)
    print(Car.__doc__)
    print(Car.__name__)

if __name__=="__main__":
    main()


# In[22]:


#2.Define 1 parent class and 3 child classes of your choice. The parent class should be an abstract class and you must 
#create 3 abstractmethods in it which should be overridden in the child classes
from abc import ABC, abstractmethod
class Laptop(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def print_laptop_details(self):
        pass
    
class Dell(Laptop):
    def __init__(self,model,ram,storage,price):
        self.model=model
        self.ram=ram
        self.storage=storage
        self.price=price
        
    def print_laptop_details(self):
        print("Dell Laptop have, Model no: ",self.model,"\tRAM: ",self.ram,"\tStorage: ",self.storage,"\tPrice: ",self.price)
        
class HP(Laptop):
    def __init__(self,model,ram,storage,price):
        self.model=model
        self.ram=ram
        self.storage=storage
        self.price=price
        
    def print_laptop_details(self):
        print("HP Laptop have, Model no: ",self.model,"\tRAM: ",self.ram,"\tStorage: ",self.storage,"\tPrice: ",self.price)
        
class Lenovo(Laptop):
    def __init__(self,model,ram,storage,price):
        self.model=model
        self.ram=ram
        self.storage=storage
        self.price=price
        
    def print_laptop_details(self):
        print("Lenovo Laptop have, Model no: ",self.model,"\tRAM: ",self.ram,"\tStorage: ",self.storage,"\tPrice: ",self.price)
        
def main():
    d1=Dell("Dell1","4GB","250GB HDD",35000)
    d1.print_laptop_details()
    h1=HP("HP4","8GB","512GB HDD",55000)
    h1.print_laptop_details()
    l1=Lenovo("GamerX","16GB","2TB SSD",87000)
    l1.print_laptop_details()
    
if __name__=="__main__":
    main()


# In[30]:


#3.Create 3 classes in which 2 are parent child and 1 is completely different and utilise the isinstance and issubclass 
#keywords to show  their usage.
class Language:
    def __init__(self,name,level):
        self.name=name
        self.level=level
        
    def print_details(self):
        print("Programming language name: ",self.name,"\tLevel: ",self.level)
        
class Programming(Language):
    def __init__(self,name,level,applications):
        super().__init__(name,level)
        self.applications=applications
        
    def print_details(self):
        print("Programming language name: ",self.name,"\tLevel: ",self.level,"\tApplications: ",self.applications)
        
class Speaking:
    def __init__(self,name,applications):
        self.name=name
        self.applications=applications
        
    def print_details(self):
        print("Speaking language name: ",self.name,"\tApplications: ",self.applications)
        
def main():
    l1=Language("Java","High Level")
    l1.print_details()
    p1=Programming("Python","High Level","AI")
    p1.print_details()
    s1=Speaking("English","Communication")
    s1.print_details()
    print(issubclass(Programming,Language))
    print(issubclass(Speaking,Language))
    print(issubclass(Speaking,Programming))
    print(issubclass(Language,Programming))
    print(issubclass(Language,Speaking))
    
if __name__=="__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:




