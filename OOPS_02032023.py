#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Inheritance LSP
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def set_length(self,length):
        self.length=length
        
    def set_breadth(self,breadth):
        self.breadth=breadth
        
class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
        
    def set_length(self,length):
        self.length=self.breadth=length
    
    def set_breadth(self,breadth):
        self.length=self.breadth=breadth
        
def calculate_area(obj):
    obj.set_length(10)
    return "Area is:- " + str(10*obj.breadth)

def main():
    r1=Rectangle(4,5)
    s1=Square(4)
    print(calculate_area(r1))
    print(calculate_area(s1))
    
if __name__=="__main__":
    main()


# In[15]:


#Inheritance Class method
class Student:
    school_name='ABC School'
    def __init__(self,name):
        self.name=name
        
    @classmethod
    def change_school_name(cls,school_name):
        cls.school_name=school_name
        
class CollegeStudent(Student):
    college_name='DEF College'
    def __init__(self,college_id,name):
        super().__init__(name)
        self.college_id=college_id
        
def main():
    s1=Student('Ram')
    c1=CollegeStudent(1234,'Shyam')
    print(CollegeStudent.school_name)
    CollegeStudent.change_school_name('FGH School')
    print(CollegeStudent.school_name)
    
if __name__=='__main__':
    main()


# In[16]:


#Inheritance access modifier
class Student:
    school_name='ABC School'
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        
    @classmethod
    def change_school_name(cls,school_name):
        cls.school_name=school_name
        
    def __print_student_details(self):
        print(self.name)
        
class CollegeStudent(Student):
    college_name='DEF College'
    def __init__(self,college_id,student_id,name):
        super().__init__(name,student_id)
        self.college_id=college_id
        
    def __print_student_details(self,some_str):
        print(self.name,self.college_id,some_str)
        
def main():
    s1=Student('Ram',2345)
    c1=CollegeStudent(1234,2345,'Shyam')
    print(CollegeStudent.school_name)
    c1._CollegeStudent__print_student_details('Some String')
    
if __name__=='__main__':
    main()


# In[2]:


#Inheritance Polymorphism
class Student:
    def __init__(self,name):
        self.name=name
        
    def print_name(self):
        print("Student: ",self.name)
        
class CollegeStudent(Student):
    def __init__(self,name):
        super().__init__(name)
        
    def print_name(self):
        print("College Student: ",self.name)
        
def main():
    s1=Student('Ram')
    c1=CollegeStudent('Shyam')
    s1.print_name()
    c1.print_name()
    
if __name__=='__main__':
    main()


# # Practise

# In[6]:


#1.Write a parent and child class Shape and Rectangle. Create 3 instance attributes in the constructor for Shape 
#(height, width, shape_name). Create methods in Shape for display_attributes and number_of_sides override it in Rectangle
class Shape:
    def __init__(self,height,width,shape_name):
        self.height=height
        self.width=width
        self.shape_name=shape_name
        
    def display_attributes(self):
        print("Height: ",self.height,"\tWidth: ",self.width,"\tShape name: ",self.shape_name)
        
    def no_of_sides(self):
        print("Number of sides:"+'4')
        
class Rectangle(Shape):
    def __init__(self,height,width,shape_name):
        super().__init__(height,width,shape_name)
        
    def display_attributes(self):
        print("Height: ",self.height,"\tWidth: ",self.width,"\tShape name: ",self.shape_name)
        
    def no_of_sides(self):
        print("Number of sides:"+'4')
        
def main():
    s1=Shape(4,4,'Square')
    s1.display_attributes()
    s1.no_of_sides()
    r1=Rectangle(4,5,'Rectangle')
    r1.display_attributes()
    r1.no_of_sides()
    
if __name__=="__main__":
    main()


# In[16]:


#2.Create a method calculate_area in Shape class and override it in Rectangle & use the super keyword to help calculate the area
class Shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def calculate_area(self):
        return (2*self.length*self.breadth)
    
class Rectangle(Shape):
    def __init__(self,length,breadth):
        super().__init__(length,breadth)
        
    def calculate_area(self):
        return super().calculate_area()
    
def main():
    s1=Shape(4,5)
    print(s1.calculate_area())
    r1=Rectangle(3,4)
    print(r1.calculate_area())
    
if __name__=="__main__":
    main()


# In[20]:


#3.Create a method calculatePerimeter and override it in Rectangle
class Shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def calculate_perimeter(self):
        print(2*(self.length+self.breadth))
    
class Rectangle(Shape):
    def __init__(self,length,breadth):
        super().__init__(length,breadth)
        
    def calculate_perimeter(self):
        return super().calculate_perimeter()
    
def main():
    s1=Shape(4,5)
    s1.calculate_perimeter()
    r1=Rectangle(3,4)
    r1.calculate_perimeter()
    
if __name__=="__main__":
    main()


# In[23]:


#4.Do the same steps from 1 to 3 for Circle instead of Rectangle
#1
class Shape:
    def __init__(self,height,width,shape_name):
        self.height=height
        self.width=width
        self.shape_name=shape_name
        
    def display_attributes(self):
        print("Height: ",self.height,"\tWidth: ",self.width,"\tShape name: ",self.shape_name)
        
    def no_of_sides(self):
        print("Number of sides:"+'4')
        
class Circle(Shape):
    def __init__(self,radius):
        super().__init__(radius,radius)
        self.radius=radius
        
    def display_attributes(self):
        print("Radius:",self.radius,"\tShape name: ",self.shape_name)
        
    def no_of_sides(self):
        print("Number of sides:"+'1')
        
def main():
    s1=Shape(4,4,'Square')
    s1.display_attributes()
    s1.no_of_sides()
    c1=Circle(4,5,'Circle',3)
    c1.display_attributes()
    c1.no_of_sides()
    
if __name__=="__main__":
    main()


# In[24]:


#2.
class Shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def calculate_area(self):
        return (2*self.length*self.breadth)
    
class Circle(Shape):
    def __init__(self,radius):
        super().__init__(radius,radius)
        self.radius=radius
        
    def calculate_area(self):
        return 3.14*self.radius*self.radius
    
def main():
    s1=Shape(4,5)
    print(s1.calculate_area())
    r1=Circle(3)
    print(r1.calculate_area())
    
if __name__=="__main__":
    main()


# In[26]:


#3.
class Shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def calculate_perimeter(self):
        print(2*(self.length+self.breadth))
    
class Circle(Shape):
    def __init__(self,radius):
        super().__init__(radius,radius)
        self.radius=radius
        
    def calculate_area(self):
        return 2*3.14*self.radius
    
def main():
    s1=Shape(4,5)
    s1.calculate_perimeter()
    r1=Circle(3)
    r1.calculate_perimeter()
    
if __name__=="__main__":
    main()

