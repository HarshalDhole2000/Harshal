#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Polymorphism class methods
class Vehicle:
    def __init__(self,color,make):
        self.color=color
        self.make=make
        
    def get_color(self):
        return self.color
    
    def get_make(self):
        return self.make
    
class Car:
    def __init__(self,color,make):
        self.color=color
        self.make=make
        
    def get_color(self):
        return self.color
    
    def get_make(self):
        return self.make
    
def main():
    v1=Vehicle('Black','Merc')
    c1=Car('White','BMW')
    for obj in (v1,c1):
        print(obj.get_color(),obj.get_make())
    
if __name__=='__main__':
    main()


# In[ ]:


#Polymorphism methods object
class Vehicle:
    def __init__(self,color,make):
        self.color=color
        self.make=make
        
    def get_color(self):
        return self.color
    
    def get_make(self):
        return self.make
    
class Car:
    def __init__(self,color,make):
        self.color=color
        self.make=make
        
    def get_color(self):
        return self.color
    
    def get_make(self):
        return self.make
    
def print_values(obj):
    print(obj.get_color(),obj.get_make())
    
def main():
    v1=Vehicle('Black','Merc')
    c1=Car('White','BMW')
    print_values(v1)
    print_values(c1)
    
if __name__=='__main__':
    main()


# In[ ]:


#Polymorphism overloading
def print_values(a,b):
    print(a,b)
    
def print_values(a,b,c):
    print(a,b,c)
    
def main():
    #print_values(1,2)
    print_values(1,2,3)
    
if __name__=='__main__':
    main()


# In[ ]:


#Polymorphism overloading default value
def add(a,b,c=0):
    return a+b+c

def main():
    print(add(1,2))
    print(add(1,2,3))
    
if __name__=='__main':
    main()


# In[ ]:


#Polymorphism dispatch
from multipledispatch import dispatch

@dispatch(int,int)
def add(a,b):
    return a+b

@dispatch(int,int,int)
def add(a,b,c):
    return a+b+c

@dispatch(float,float)
def add(a,b):
    return a+b

def main():
    print(add(1,2,3))
    print(add(1.2,2.1))
    print(add(1,2))
    
if __name__=='__main__':
    main()


# In[ ]:


#Polymorphism operator overloading
class Employee:
    def __init__(self,name,age,_id,salary_per_hour):
        self.name=name
        self.age=age
        self.id=_id
        self.salary_per_hour=salary_per_hour
        
    def get_salary_per_hour(self):
        return self.salary_per_hour
    
class Timesheet:
    def __init__(self,_id,hours):
        self.id=_id
        self.hours=hours
        
    def get_hours(self):
        return self.hours
    
    def __mul__(self,other):
        return (self.get_hours()*other.get_salary_per_hour())
    
def main():
    e1=Employee('Ram',22,'123',11)
    t1=Timesheet('123',11)
    print(t1 * e1)
    
if __name__=='__main__':
    main()


# In[ ]:


#Class method static method
class Student:
    school_name='Saraswati Vidya Mandir'
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @classmethod
    def change_school_name(cls,school_name):
        cls.school_name=school_name
        
    @staticmethod
    def addition(a,b):
        return a+b
    
    def get_name(self):
        return self.name
    
def main():
    s1=Student('Ram',24)
    s2=Student('Shyam',25)
    
if __name__=='__main__':
    main()


# In[6]:


#1.In Day 3, problem 3 how would you handle items with the same name being added if while deleting you need to remove all items 
#with name from the plate? Also can you make sure if “palak_paneer” is added 2 times you save it only once? 
#What data structure would you use? Can you use a dict or set?
class Plate:
    def __init__(self):
        self.items_on_plate=[]
        
    def add_to_plate(self,item):
       
        if item in self.items_on_plate:
            pass
        else:
            self.items_on_plate.append(item)
        
    def remove_from_plate(self,item):
        self.items_on_plate.remove(item)
        
    def display_items_on_plate(self):
        print(self.items_on_plate)
        
def main():        
    p=Plate()
    p.add_to_plate("Palak_paneer")
    p.add_to_plate("Palak_paneer")
    p.display_items_on_plate()
    p.remove_from_plate('Palak_paneer')
    p.display_items_on_plate()
    
if __name__=='__main__':
    main()


# In[36]:


#2.Create a class named Number which has object attributes called datatype(string) and value(can be int/float), 
#create getter and setter methods for datatype and value. Add the constraint that if the datatype is changed 
#from int to float then the value should also be typecast to float, and if the value is changed then the datatype 
#is also changed (Example: if datatype = int and value = 2, and using the setter method we change datatype to float 
#then value should become 2.0, and if value is changed from 2.0(float) to 3(int) change datatype from float to int)
class Number:
    def __init__(self,datatype,value):
        self.datatype=datatype
        self.value=value
        
    def get_datatype(self):
        return self.datatype
    
    def set_datatype(self,datatype):
        if datatype==self.datatype:
            pass
        else:
            if datatype=='float':
                self.value=float(self.value)
            else:
                self.value=int(self.value)
              
    def get_value(self):
        return self.value
    
    def set_value(self,value):
        if self.datatype==type(value):
            self.value=value
        else:
            self.datatype=str(type(value))
            self.value=value
            
def main():
    n1=Number('float',2.1)
    print(n1.get_datatype())
    print(n1.get_value())
    n1.set_datatype('int')
    print(type(n1.get_value()))
    print(n1.get_value())
    
if __name__=='__main__':
    main()


# In[6]:


#3.In the above Number class override the in-built method for __add__ so that when we add two numbers they should 
#return the sum of their values, override the below methods as well:
class Number:
    def __init__(self,value):
        self.value=value
    
    def __add__(self,other):
        return self.value+other.value
        
def main():
    n1=Number(1)
    n2=Number(2)
    print(n1+n2)
    
if __name__=='__main__':
    main()

