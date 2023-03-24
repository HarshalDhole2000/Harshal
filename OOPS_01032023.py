#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Inheritance method overriding
class Shape:
    def __init__(self,sides):
        self.sides=sides
        
    def print_shape(self):
        print("This shape is not defined")
        
    def print_sides(self):
        print(self.sides)
        
class Square(Shape):
    def __init__(self,sides):
        super().__init__(sides)
        
    def print_shape(self):
        print("This shape is Square")
        
class Circle(Square):
    def __init__(self,sides):
        self.sides=sides
        
    def print_shape(self):
        print("This shape is Circle")
        
    def print_sides(self):
        print(self.sides)
        
class Triangle(Square):
    def __init__(self,sides):
        super().__init__(sides)
    
    def print_shape(self):
        print("This shape is Triangle")
        
    def print_sides(self):
        print(self.sides)
        
def main():
    circle=Circle(100)
    square= Square(4)
    square.print_shape()
    square.print_sides()
    circle.print_sides()
    triangle=Triangle(3)
    triangle.print_shape()
    triangle.print_sides()
    
if __name__=="__main__":
    main()


# In[6]:


#Inheritance method overriding LSP(Liskov Substitution Principle)
class Shape:
    def __init__(self,sides):
        self.sides=sides
        
    def print_shape(self):
        print("This shape is not defined")
        
class Square(Shape):
    def __init__(self,sides):
        super().__init__(sides)
        
    def print_shape(self,arg='default_arg'):
        print("This shape is Square",arg)
        
class Triangle(Square):
    def __init__(self,sides):
        super().__init__(sides)
    
    def print_shape(self,arg='default_arg_triangle'):
        print("This shape is Triangle",arg)
        
def main():
    shape=Shape(4)
    square=Square(5)
    triangle=Triangle(3)
    shape_list=[shape,square,triangle]
    for shape_obj in shape_list:
        print_shape_wrapper(shape_obj)
        
def print_shape_wrapper(obj):
    obj.print_shape()
    
if __name__=='__main__':
    main()


# In[2]:


#inheritance super()
class Animal:
    def __init__(self,no_of_legs,sound):
        self.no_of_legs=no_of_legs
        self.sound=sound
        
    def print_no_of_legs(self):
        print(self.no_of_legs)
        
    def print_sound(self):
        print(self.sound)
        
class Dog(Animal):
    def __init__(self,no_of_legs,sound,collar):
        super().__init__(no_of_legs,sound)
        self.collar=collar
        
    def print_sound(self):
        super().print_sound()
        print(self.collar)
        super().print_no_of_legs()
        
def main():
    a1=Animal(4,'Woof')
    a1.print_sound()
    a1.print_no_of_legs()
    d1=Dog(4,'Woof',True)
    d1.print_sound()
    d1.print_no_of_legs()
    
if __name__=='__main__':
    main()


# # Practise

# In[19]:


#1.Write any class of your choice and create a child class of it using single inheritance
class Class:
    def __init__(self,standard,division):
        self.standard=standard
        self.division=division
        
    def print_class_details(self):
        print("Class:-",self.standard,"\tNo.of students:-",self.division)
        
class Student(Class):
    def __init__(self,roll_no,name,standard,division):
        super().__init__(standard,division)
        self.roll_no=roll_no
        self.name=name
        
    def print_student_details(self):
        print("Roll no:-",self.roll_no,"name:-",self.name,"Class:-",self.standard,"\tNo.of students:-",self.division)
        
def main():
    c1=Class(8,'A')
    c1.print_class_details()
    s1=Student(1,'Ram',8,'B')
    s1.print_class_details()
    s1.print_student_details()
    
if __name__=='__main__':
    main()


# In[26]:


#2.Write any 3 classes of your choice to showcase multilevel inheritance.
class School:
    def __init__(self,school_name,city):
        self.school_name=school_name
        self.city=city
        
    def print_school_details(self):
        print("\nSchool name:-",self.school_name,"\tCity:-",self.city)
        
class Class(School):
    def __init__(self,standard,division,school_name,city):
        super().__init__(school_name,city)
        self.standard=standard
        self.division=division
        
    def print_class_details(self):
        print("Class:-",self.standard,"\tNo.of students:-",self.division,"\tSchool name:-",self.school_name,"\tCity:-",self.city)
        
class Student(Class):
    def __init__(self,roll_no,name,standard,division,school_name,city):
        super().__init__(standard,division,school_name,city)
        self.roll_no=roll_no
        self.name=name
        
    def print_student_details(self):
        print("Roll no:-",self.roll_no,"\tname:-",self.name,"\tClass:-",self.standard,"\tNo.of students:-",self.division,"\tSchool name:-",self.school_name,"\tCity:-",self.city)
        
def main():
    sc1=School('New English School','Pune')
    sc1.print_school_details()
    c1=Class(8,'A','English School','Pune')
    c1.print_school_details()
    c1.print_class_details()
    s1=Student(1,'Ram',8,'B','Ganesh Vidya Mandir','Pune')
    s1.print_school_details()
    s1.print_class_details()
    s1.print_student_details()
    
if __name__=='__main__':
    main()


# In[48]:


#3.Create any class of your choice and then create 3 child classes of it to exhibit hierarchical inheritance
class Mobile:
    def __init__(self,rank,company_name):
        self.rank=rank
        self.company_name=company_name
        
    def print_mobile_details(self):
        print("Rank:-",self.rank,"\tCompany name:-",self.company_name)
        
class Samsung(Mobile):
    def __init__(self,rank,company_name,model,price):
        super().__init__(rank,company_name)
        self.model=model
        self.price=price
        
    def print_samsung_details(self):
        print("Rank:-",self.rank,"\tCompany name:-",self.company_name,"\tModel name:-",self.model,"\tPrice:-",self.price)
        
class Apple(Mobile):
    def __init__(self,rank,company_name,model,price):
        super().__init__(rank,company_name)
        self.model=model
        self.price=price
        
    def print_apple_details(self):
        print("Rank:-",self.rank,"\tCompany name:-",self.company_name,"\tModel name:-",self.model,"\tPrice:-",self.price)
        
class Redmi(Mobile):
    def __init__(self,rank,company_name,model,price):
        super().__init__(rank,company_name)
        self.model=model
        self.price=price
        
    def print_redmi_details(self):
        print("Rank:-",self.rank,"\tCompany name:-",self.company_name,"\tModel name:-",self.model,"\tPrice:-",self.price)
        
def main():
    m1=Mobile(2,'Oneplus')
    m1.print_mobile_details()
    s1=Samsung(3,'Samsung','A51',45000)
    s1.print_samsung_details()
    s1.print_mobile_details()
    a1=Apple(1,'Apple','14 Pro',145000)
    a1.print_apple_details()
    a1.print_mobile_details()
    r1=Redmi(4,'Redmi','Note 12',25000)
    r1.print_redmi_details()
    r1.print_mobile_details()
    
if __name__=="__main__":
    main()


# In[38]:


#4.Create any class with a classmethod and then delete it using the del keyword and using the delattr keyword
class Company:
    school_name='Capgemini'
    
    def __init__(self,name):
        self.name=name
        
    @classmethod
    def change_company_name(cls,company_name):
        cls.company_name=company_name
        
def main():
    #del Company.change_company_name
    delattr(Company,'change_company_name')
    Company.change_company_name('Infoys')
    
if __name__=='__main__':
    main()

