#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Abstract class ABC
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def has_shape(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def has_shape(self):
        print("The shape is circle")
        
    def calculate_area(self):
        print("Area of circle is:- ",3.14*self.radius*self.radius)
        
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def has_shape(self):
        print("The shape is rectangle")
        
    def calculate_area(self):
        print("The area of rectangle is: ",self.length*self.breadth)
def main():
    c1=Circle(3)
    c1.has_shape()
    c1.calculate_area()
    r1=Rectangle(3,4)
    r1.has_shape()
    r1.calculate_area()
    
if __name__=="__main__":
    main()


# In[14]:


#isinstance keyword
#int,float,complex,list,inside class
class Animal:
    def __init__(self,animal_type,sound):
        self.animal_type=animal_type
        self.sound=sound
        
class Dog(Animal):
    def __init__(self,animal_type,sound,breed):
        super().__init__(animal_type,sound)
        self.breed=breed
        
def main():
    d1=Dog("Dog","Bark","Husky")
    a1=Animal("Cat","Meow")
    print(isinstance(a1,Dog))
    print(isinstance(a1,Animal))
    print(isinstance(d1,Dog))
    print(isinstance(d1,Animal))
    print(isinstance(a1,list))
    
    num=10
    float_num=2.3
    my_list=['a','b','c',1,1.5]
    my_string="Random String"
    complex_num=complex(3,4)
    print(isinstance(num,int))
    print(isinstance(num,float))
    print(isinstance(float_num,float))
    print(isinstance(float_num,list))
    print(isinstance(my_list,list))
    print(isinstance(my_string,str))
    print(isinstance(complex_num,complex))
    print(isinstance(complex_num,int))
    print(type(num))
    
if __name__=="__main__":
    main()


# In[21]:


#issubclass method
class Animal:
    def __init__(self,animal_type,sound):
        self.animal_type=animal_type
        self.sound=sound
        
class Dog(Animal):
    def __init__(self,animal_type,sound,breed):
        super().__init__(animal_type,sound)
        self.breed=breed
        
class StreetDog(Dog):
    def __init__(self,animal_type,sound,breed):
        super().__init__(animal_type,sound,breed)
        
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
def main():
    d1=Dog("Dog","Bark","Husky")
    a1=Animal("Cat","Meow")
    p1=Person("Ram",24)
    print(issubclass(Dog,Animal))
    print(issubclass(StreetDog,Animal))
    print(issubclass(Animal,Dog))
    print(issubclass(Dog,Person))
    print(issubclass(Animal,Person))
    #print(issubclass(d1,a1))
    
if __name__=="__main__":
    main()


# In[30]:


#introspection
class Animal:
    def __init__(self,animal_type,sound):
        self.animal_type=animal_type
        self.sound=sound
        
    def print_animal_attributes(self):
        print("Animal attributes: ",self.animal_type,self.sound)
        
    def __repr__(self):
        return "Animal attributes: ",self.animal_type,self.sound
    
def main():
    a1=Animal("Dog","Bark")
    a2=Animal("Cat","Meow")
    a3=a2
    print(id(a1))
    print(id(a2))
    print(id(a3))
    print(dir(a1))
    print(len(dir(a1)))
    num=5
    #print(dir(num))
    my_string="Super Class"
    '''
    print(len(dir(my_string)))
    print(my_string.__contains__("MIni"))
    print(my_string.__eq__("Max"))
    print(my_string.__len__())
    print(type(my_string))
    print(type(a1))
    '''
    print(Animal.__doc__)
    print(Animal.__name__)
    print(hasattr(a1,"print_animal_attributes"))
    print(getattr(a1,"sound"))
    print(a1.sound)
    #print(repr(a1))
    #print(a1)
    a1.print_animal_attributes()

if __name__=="__main__":
    main()


# # Practise

# In[33]:


#1.Implement Hybrid Inheritance using any class of your choice (examples: Shape, Animal etc)
class Shape:
    def print_method(self):
        print("Welcome to the Shape World")
        
class Rectangle(Shape):
    def print_method(self):
        print("This is the Rectangle which having 2 same sides means length and another 2 sides are also same means breadth")
        
class Square(Shape):
    def print_method(self):
        print("This is Square which having a 4 equal sides")
        
class Circle(Rectangle,Square):
    def print_method(self):
        print("This is circle which is having a one radius")
        
def main():
    c1=Circle()
    c1.print_method()
    s1=Square()
    s1.print_method()
    r1=Rectangle()
    r1.print_method()
    sh1=Shape()
    sh1.print_method()
    
if __name__=="__main__":
    main()


# In[48]:


#2.Write classes linked through multiple inheritance and print their MRO 
class Shape:
    def print_method(self):
        print("Welcome to the Shape World")
        
class Rectangle(Shape):
    def print_method(self):
        print("This is the Rectangle which having 2 same sides means length and another 2 sides are also same means breadth")
        
class Square(Shape):
    def print_method(self):
        print("This is Square which having a 4 equal sides")
        
class Circle(Rectangle,Square):
    def print_method(self):
        print("This is circle which is having a one radius")
        
def main():
    c1=Circle()
    c1.print_method()
    print(Circle.mro())
    
if __name__=="__main__":
    main()


# In[49]:


#3.Write classes linked through multiple inheritance but make sure their MRO throws an error
class Shape:
    def print_method(self):
        print("Welcome to the Shape World")
        
class Rectangle(Shape):
    def print_method(self):
        print("This is the Rectangle which having 2 same sides means length and another 2 sides are also same means breadth")
        
class Square(Rectangle):
    def print_method(self):
        print("This is Square which having a 4 equal sides")
        
class Circle(Rectangle,Square):
    def print_method(self):
        print("This is circle which is having a one radius")
        
        
def main():
    c1=Circle()
    c1.print_method()
    print(Circle.mro())
    
if __name__=="__main__":
    main()


# In[50]:


#4.Try to correct the MRO that threw an error in the previous step and print it
class Shape:
    def print_method(self):
        print("Welcome to the Shape World")
        
class Rectangle(Shape):
    def print_method(self):
        print("This is the Rectangle which having 2 same sides means length and another 2 sides are also same means breadth")
        
class Square(Rectangle):
    def print_method(self):
        print("This is Square which having a 4 equal sides")
        
class Circle(Square,Rectangle):
    def print_method(self):
        print("This is circle which is having a one radius")
        
        
def main():
    c1=Circle()
    c1.print_method()
    print(Circle.mro())
    
if __name__=="__main__":
    main()


# In[78]:


#5.Implement a Queue class in Python which you add elements at the end and remove from the front.
class Queue:
    def __init__(self):
        self.__queue=[]
        
    def push(self,num):
        self.__queue.append(num)
        
    def remove(self):
        return self.__queue.pop(0)
    
    def display_elements(self):
        print(self.__queue)
        
q1=Queue()
q1.push(1)
q1.display_elements()
q1.push(2)
q1.display_elements()
q1.push(3)
q1.display_elements()
q1.remove()
q1.display_elements()
q1.remove()
q1.display_elements()
q1.remove()
q1.display_elements()

