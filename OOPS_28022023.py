#!/usr/bin/env python
# coding: utf-8

# In[27]:


#inheritance
class Shape:
    def __init__(self,sides):
        self.sides=sides
        
    def print_sides(self):
        print(self.sides)
        
class Rectangle(Shape):
    def __init__(self,sides,length,breadth):
        super().__init__(sides)
        self.length=length
        self.breadth=breadth
        
    def print_length(self):
        print(self.length)
        
    def print_breadth(self):
        print(self.breadth)
        
def main():
    rect=Rectangle(4,2,2)
    #print(rect.sides)
    rect.print_sides()
    rect.print_length()
    rect.print_breadth()
    
if __name__=='__main__':
    main()


# In[12]:


#Single inheritance
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def print_name(self):
        print("Person name is ", self.name)
        
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id
    
    def print_student_id(self):
        print("Student ID is ",self.student_id)
        
    def print_age(self):
        print("Person age is ",self.age)
        
def main():
    student=Student("Ram",17,1234)
    student.print_student_id()
    student.print_name()
    student.print_age()
    
if __name__=="__main__":
    main()


# In[19]:


#Multilevel Inheritance
class Vehicle:
    def __init__(self,num_of_wheels,engine_power,vehicle_type):
        self.num_of_wheels=num_of_wheels
        self.engine_power=engine_power
        self.vehicle_type=vehicle_type
        
    def print_vehicle_attributes(self):
        print("Vehicle attributes: ",self.num_of_wheels,self.engine_power,self.vehicle_type)
        
class Car(Vehicle):
    def __init__(self,num_of_wheels,engine_power,vehicle_type,color):
        super().__init__(num_of_wheels,engine_power,vehicle_type)
        self.color=color
        
    def print_car_attributes(self):
        print("Car attributes: ",self.num_of_wheels,self.engine_power,self.vehicle_type,self.color)
        
class SportsCar(Car):
    def __init__(self,num_of_wheels,engine_power,vehicle_type,color,turbo_acc):
        super().__init__(num_of_wheels,engine_power,vehicle_type,color)
        self.turbo_acc=turbo_acc
        
    def print_sports_car_attributes(self):
        print("Sports car attributes: ",self.num_of_wheels,self.engine_power,self.vehicle_type,self.color,self.turbo_acc)
        
def main():
    car=Car(4,1200,"SUV","Red")
    sports_car=SportsCar(4,1600,"F1","Blue",4)
    car.print_car_attributes()
    sports_car.print_vehicle_attributes()
    sports_car.print_car_attributes()
    sports_car.print_sports_car_attributes()
    
if __name__=="__main__":
    main()


# In[26]:


#Hierarchical Inheritance
class Vehicle:
    def __init__(self,num_of_wheels,engine_power,vehicle_type):
        self.num_of_wheels=num_of_wheels
        self.engine_power=engine_power
        self.vehicle_type=vehicle_type
        
    def print_vehicle_attributes(self):
        print("Vehicle attributes: ",self.num_of_wheels,self.engine_power,self.vehicle_type)
        
class Car(Vehicle):
    def __init__(self,num_of_wheels,engine_power,vehicle_type,color):
        super().__init__(num_of_wheels,engine_power,vehicle_type)
        self.color=color
        
    def print_car_attributes(self):
        print("Car attributes: ",self.num_of_wheels,self.engine_power,self.vehicle_type,self.color)
        
class Truck(Vehicle):
    def __init__(self,num_of_wheels,engine_power,vehicle_type,load_capacity):
        super().__init__(num_of_wheels,engine_power,vehicle_type)
        self.load_capacity=load_capacity
        
    def print_truck_attributes(self):
        print("Truck attributes: ",self.num_of_wheels,self.engine_power,self.vehicle_type,self.load_capacity)
        
def main():
    car=Car(4,1200,"SUV","Red")
    truck=Truck(4,2000,"Eicher",'25000 tonnes')
    car.print_car_attributes()
    car.print_vehicle_attributes()
    truck.print_truck_attributes()
    truck.print_vehicle_attributes()
    
if __name__=="__main__":
    main()


# # Practise

# In[63]:


#1.Create 2 classes Student (properties: age, name, subjects[list], marks[list]) and Exams( properties: subjects[list], 
#pass_marks:[list] ) and override the __mul__ method in Student and Exams such that if the values in each index of  marks 
#in Student are greater than values in each index of pass_marks in Exams then return Pass else Fail.
class Student:
    def __init__(self,age,name,subjects=[],marks=[]):
        self.age=age
        self.name=name
        self.subjects=subjects
        self.marks=marks
        
    def print_student_details(self):
        print("Student details is: ",self.age,self.name,self.subject,self.marks)
        
    def __mul__(self,other):
        if self.marks[0]>other.pass_marks[0] and self.marks[1]>other.pass_marks[1]:
            return "PASS"
        else:
            return"FAIL"
        
class Exams(Student):
    def __init__(self,age,name,subjects=[],marks=[],pass_marks=[]):
        super().__init__(age,name,subjects,marks)
        self.pass_marks=pass_marks
    
    def print_students_exam_details(self):
        print("Student exam details is: ",self.subject,self.pass_marks)
        
def main():
    s1=Student(21,'Ram',['English','Maths'],[67,38])
    e1=Exams(21,'Ram',['English','Maths'],[67,38],[35,40])
    print(s1 * e1)
    
if __name__=="__main__":
    main()


# In[65]:


class Student:
    def __init__(self,age,name,subjects=[],marks=[]):
        self.age=age
        self.name=name
        self.subjects=subjects
        self.marks=marks
        
    def print_student_details(self):
        print("Student details is: ",self.age,self.name,self.subject,self.marks)
        
    def __mul__(self,other):
        for idx,subjects in enumerate(self.marks):
            if self.marks[idx]>other.pass_marks[idx]:
                continue
            else:
                return"FAIL"
        return "PASS"
        
class Exams(Student):
    def __init__(self,age,name,subjects=[],marks=[],pass_marks=[]):
        super().__init__(age,name,subjects,marks)
        self.pass_marks=pass_marks
    
    def print_students_exam_details(self):
        print("Student exam details is: ",self.subject,self.pass_marks)
        
def main():
    s1=Student(21,'Ram',['English','Maths'],[67,38])
    e1=Exams(21,'Ram',['English','Maths'],[67,38],[35,40])
    print(s1 * e1)
    
if __name__=="__main__":
    main()


# In[60]:


#2.Create any class of your choice and create any function of your choice outside the class and then dynamically add it to the 
#class using classmethod keyword
class Employee:
    company_name='Infosys'
    
    def __init__(self,e_id,name):
        self.e_id=e_id
        self.name=name
        
    def print_employee_details(self):
        print("ID:-",self.e_id,"\tName:- ",self.name,"\tCompany name:- ",self.company_name)
        
        
def another_change_company_name(cls,company_name):
    cls.company_name=company_name
    
def main():
    e1=Employee(1234,'Ram')
    e1.print_employee_details()
    Employee.another_change_company_name=classmethod(another_change_company_name)
    Employee.another_change_company_name('Capgemini')
    e1.print_employee_details()
    
if __name__=='__main__':
    main()

