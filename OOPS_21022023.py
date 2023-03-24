#!/usr/bin/env python
# coding: utf-8

# In[101]:


#constructor
class Student:
    def __init__(self):
        pass
    
def main():
    student=Student()
    print("Object created")
    
if __name__=="__main__":
    main()


# In[9]:


#class varaible
class Student:
    school_name="New English Medium School"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
def main():
    student1=Student("Ram",24)
    student2=Student("Shyam",25)
    print(student1.name,student1.age)
    print(student2.name,student2.age)
    print(student1.school_name,student2.school_name,Student.school_name)
    
if __name__=="__main__":
    main()


# In[19]:


#getter setter
class Student:
    school_name="New English Medium School"
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.__marks=marks
    
    def get_marks(self):
        return self.__marks
    
    def set_marks(self,marks):
        if self.age<20:
            print("Not allowed")
        else:
            self.__marks=marks
            print("Successful")
    
def main():
    student1=Student("Ram",24,100)
    student2=Student("Shyam",25,95)
    print(student1.name,student1.age,student1.get_marks())
    student2.set_marks(98)
    print(student2.name,student2.age,student2.get_marks())
    
if __name__=="__main__":
    main()


# In[26]:


#name mangling
class Student:
    school_name="New English Medium School"
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.__marks=marks
    
def main():
    student1=Student("Ram",24,100)
    student2=Student("Shyam",25,95)
    print(student1.name,student1.age,student1._Student__marks)
    print(student2.name,student2.age,student2._Student__marks)
    
if __name__=="__main__":
    main()


# In[35]:


#constructor types
class Student:#default constructor provide bt python
    def print_student_details(self):
        print("This is for student details example 0.")
        
class StudentExample1:#constructor with no arguments
    def __init__(self):
        pass
    
    def print_student_details(self):
        print("This is for student details example 1.")
    
class StudentExample2:#argument constructor
    def  __init__(self,name,age):
        self.name=name
        self.age=age
        
    def print_student_details(self):
        print("This is for student details example 2.","name:-",self.name,"age:-",self.age)
        
def main():
    s1=Student()
    s2=StudentExample1()
    s3=StudentExample2("Ram",24)
    s1.print_student_details()
    s2.print_student_details()
    s3.print_student_details()
    
if __name__=="__main__":
    main()


# In[39]:


#default value constructor
class Student:
    def __init__(self,name,age=24):
        self.name=name
        self.age=age
        
    def print_student_details(self):
        print("This is for student details-->","name:-",self.name,"age:-",self.age)
        
def main():
    s1=Student("Ram",25)
    s2=Student("Shyam")
    s1.print_student_details()
    s2.print_student_details()
    
main()


# # Practise

# In[45]:


#1.Create a Animal class without any variables and methods
class Animal:
    def __init__(self):
        pass
        
def main():
    a1=Animal()
    print("Successfully created")
    
if __name__=="__main__":
    main()


# In[51]:


#2.Create a Animal class with attributes sound(string), number_of_legs(integer) and is_omnivore(boolean)
class Animal:
    def __init__(self,sound,no_of_legs,is_omnivore):
        self.sound=sound
        self.no_of_legs=no_of_legs
        self.is_omnivore=is_omnivore
        
def main():
    a1=Animal("Roar",4,True)
    a2=Animal("Chatter",2,False)
    print("Sound:-",a1.sound,"\tno_of_legs:-",a1.no_of_legs,"\tis_mnivore:-",a1.is_omnivore)
    print("Sound:-",a2.sound,"\tno_of_legs:-",a2.no_of_legs,"\tis_mnivore:-",a2.is_omnivore)
    
    
if __name__=="__main__":
    main()


# In[62]:


#3.Add a private attribute to the Animal class defined above named can_swim(boolean) and define a getter and setter method 
#for the same
class Animal:
    def __init__(self,name,can_swim,no_of_legs=2):
        self.name=name
        self.__can_swim=can_swim
        self.no_of_legs=no_of_legs
        
    def get_can_swim(self):
        return self.__can_swim
    
    def set_can_swim(self,can_swim):
        if self.no_of_legs==2:
            print("Can't swim")
        else:
            self.__can_swim=can_swim
            print("Can swim")
        
def main():
    a1=Animal("Dog",True,4)
    a2=Animal("Peacock",False)
    a3=Animal("Cow",False,4)
    print("Name:-",a1.name,"\tCan swim:-",a1.get_can_swim(),"\tNo of legs:-",a1.no_of_legs)
    print("Name:-",a2.name,"\tCan swim:-",a2.get_can_swim(),"\tNo of legs:-",a2.no_of_legs)
    a3.set_can_swim(True)
    print("Name:-",a3.name,"\tCan swim:-",a3.get_can_swim(),"\tNo of legs:-",a3.no_of_legs)

   
    
if __name__=="__main__":
    main()


# In[65]:


#4.Define a property for Animal class called hunts_for_food(boolean) that must have the same value for every class instance
#(object) equalling true
class Animal:
    def __init__(self):
        self.hunts_for_food=True
        
def main():
    a1=Animal()
    print("Hunts for food:-",a1.hunts_for_food)

if __name__=="__main__":
    main()


# In[80]:


#5.Modify the Animal class to count number of instances of the Animal class
class Animal:
    count=0
    def __init__(self):
        Animal.count=Animal.count+1

def main():
    a1=Animal()
    a2=Animal()
    a3=Animal()
    print(Animal.count,"Objects are created")

if __name__=="__main__":
    main()


# In[99]:


#6.Create a list of Animal objects(minimum 5) and then iterate through them and print their attributes
class Animal:
    def __init__(self,name):
        self.name=name

def main():
    a1=Animal('Tiger')
    a2=Animal('Lion')
    a3=Animal('Elephant')
    a4=Animal('Camel')
    a5=Animal('Horse')
    list1=[a1,a2,a3,a4,a5]
    for i in list1:
        print(i.name)
        
if __name__=="__main__":
    main()

