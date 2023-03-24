#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Inheritance multiple
class Mammal:
    def __init__(self,species_type,no_of_legs,food_type):
        self.species_type=species_type
        self.no_of_legs=no_of_legs
        self.food_type=food_type
        
    def describe_mammal(self):
        print("Mammal attributes are: ",self.species_type,"\t",self.no_of_legs,"\t",self.food_type)
        
    def can_walk(self):
        return True
    
class Human:
    def __init__(self,can_think,qualifications):
        self.can_think=can_think
        self.qualifications=qualifications
        
    def describe_human(self):
        print("Human attributes are: ",self.can_think,"\t",self.qualifications)
        
    def can_speak(self):
        return True
    
class Student(Mammal,Human):
    def __init__(self,species_type,no_of_legs,food_type,can_think,qualifications):
        Mammal.__init__(self,species_type,no_of_legs,food_type)
        Human.__init__(self,can_think,qualifications)
        
def main():
    s1=Student('Mammal',2,'Omni',True,"Post Graduate")
    s1.describe_mammal()
    s1.describe_human()
    print(s1.can_walk())
    print(s1.can_speak())
    
if __name__=="__main__":
    main()


# In[11]:


#Inheritance Hybrid
class A:
    def print_method(self):
        print("This is A")
        
class B(A):
    def print_method(self):
        print("This is B")
        
class C(A):
    def print_method(self):
        print("This is C")
        
class D(B,C):
    def print_method(self):
        print("This is D")
        
def main():
    d1=D()
    d1.print_method()
    
if __name__=="__main__":
    main()


# In[1]:


#Inheritance MRO
class A:
    def print_method(self):
        print("This is A")
        
class B(A):
    def print_method(self):
        print("This is B")
        
class C(B):
    def print_method(self):
        print("This is C")
        
class D(C,B):
    def print_method(self):
        print("This is D")
        
def main():
    d1=D()
    d1.print_method()
    print(D.mro())
    
if __name__=="__main__":
    main()


# In[2]:


#Inheritance MRO error
class A:
    def print_method(self):
        print("This is A")
        
class B(A):
    def print_method(self):
        print("This is B")
                
class C(A,B):
    def print_method(self):
        print("This is C")
        
def main():
    c1=C()
    c1.print_method()
    print(C.mro())
    
if __name__=="__main__":
    main()


# # Practise

# In[46]:


#1.Implement Multilevel Inheritance with any classes of your choice & show how does inheritance in classmethods work with an eg.
class University:
    university_name="Pune University"
    def __init__(self,region):
        self.region=region
        
    @classmethod
    def change_university_name(cls,university_name):
        cls.university_name=university_name
        
    def print_university_details(self):
        print("\n",self.university_name,"\t",self.region)
        
class College(University):
    college_name='ABC College'
    def __init__(self,region,college_id):
        University.__init__(self,region)
        self.college_id=college_id
        
    def print_college_details(self):
        print(self.college_name,"\t",self.college_id,"\t",self.region)
        
class Student(College):
    def __init__(self,region,college_id,name):
        super().__init__(region,college_id)
        self.name=name
        
def main():
    u1=University('Pune')
    c1=College("Mumbai",123)
    s1=Student("Pune",1234,"Tushar")
    u1.print_university_details()
    c1.print_university_details()
    c1.print_college_details()
    s1.print_university_details()
    s1.print_college_details()
    s1.change_university_name("Mumbai University")
    s1.print_university_details()
    
if __name__=='__main__':
    main()


# In[68]:


#2.Implement Hierarchical Inheritance with 3 classes and show how do protected & private variables and methods behave with an eg.
class University:
    university_name="Pune University"
    def __init__(self,region):
        self._region=region
        
    @classmethod
    def change_university_name(cls,university_name):
        cls.university_name=university_name
        
    def __print_university_details(self):
        print("\n",self.university_name,"\t",self._region)
        
class College(University):
    college_name='ABC College'
    def __init__(self,region,college_id):
        University.__init__(self,region)
        self.__college_id=college_id
        
    def print_college_details(self):
        print(self.college_name,"\t",self.__college_id,"\t",self._region)
        
class Student(University):
    def __init__(self,region,name):
        super().__init__(region)
        self.name=name
        
    def print_student_details(self):
        print(self.name,"\t",self._region)
        
def main():
    u1=University('Pune')
    c1=College("Mumbai",123)
    s1=Student("Pune","Tushar")
    u1._University__print_university_details()
    c1._University__print_university_details()
    c1.print_college_details()
    s1.print_student_details()
    #s1._University__print_university_details()
    s1.change_university_name("Mumbai University")
    #s1._University__print_university_details()
    
if __name__=='__main__':
    main()


# In[74]:


#3.Create classes Animal and Dog with the following methods print_attributes, make_sound, display_colour, display_animal_type 
#and write a method which takes in any object(Animal or Dog) and call all of the above methods
class Animal:
    def __init__(self,no_of_legs,sound,color,animal_type):
        self.no_of_legs=no_of_legs
        self.sound=sound
        self.color=color
        self.animal_type=animal_type
        
    def print_attributes(self):
        print("Animal Attributes: ",self.no_of_legs,"\t",self.sound,"\t",self.color,"\t",self.animal_type)
        
    def make_sound(self):
        return True
    
    def display_color(self):
        print("Color: ",self.color)
        
    def display_animal_type(self):
        print("Animal type: ",self.animal_type)
        
class Dog(Animal):
    def __init__(self,no_of_legs,sound,color,animal_type,nickname):
        super().__init__(no_of_legs,sound,color,animal_type)
        self.nickname=nickname
        
    def print_attributes(self):
        print("\nAnimal Attributes: ",self.no_of_legs,"\t",self.sound,"\t",self.color,"\t",self.animal_type)
        
    def make_sound(self):
        return True
    
    def display_color(self):
        print("Color: ",self.color)
        
    def display_animal_type(self):
        print("Animal type: ",self.animal_type)
        
def show(obj):
    obj.print_attributes()
    obj.make_sound()
    obj.display_color()
    obj.display_animal_type()
    
def main():
    a1=Animal(4,'Meow','Red','Cat')
    print(show(a1))
    d1=Dog(4,"bark","White","Dog","Tommy")
    print(show(d1))
    
if __name__=="__main__":
    main()


# In[79]:


#Create a class Stack and implement the push() and pop() and size() methods. #Example stack:
#stack = [] #push(1)-->[1] #push(2)-->[1,2] #push(4)-->[1,2,4] #push(10)-->[1,2,4,10] #pop()-->[1,2,4] #pop()-->[1,2]
class Stack:
    def __init__(self):
        self.__stack_list=[]
        
    def push(self,num):
        self.__stack_list.append(num)
        
    def pop(self):
        return self.__stack_list.pop()
    
    def display_elements(self):
        print(self.__stack_list)
        
stack=Stack()
stack.push(1)
stack.display_elements()
stack.push(2)
stack.display_elements()
stack.push(4)
stack.display_elements()
stack.push(10)
stack.display_elements()
stack.pop()
stack.display_elements()
stack.pop()
stack.display_elements()

