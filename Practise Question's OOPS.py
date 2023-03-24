#!/usr/bin/env python
# coding: utf-8

# # OOPS Practise 21/02/2023

# In[ ]:


#1.Create a Animal class without any variables and methods
class Animal:
    def __init__(self):
        pass
        
def main():
    a1=Animal()
    print("Successfully created")
    
if __name__=="__main__":
    main()


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# # OOPS Practise 22/02/2023

# In[ ]:


#1. Create a Vehicle class which has the following instance attributes: color(string), type_of_vehicle(string), 
#year_of_market_release(int) and the following class attributes: wheels(int) , no_of_doors(int) and 
#the following methods: changeColor, describeVehicle(print all the attributes), 
#brakeCar(print the attributes along with “braking”) and startCar (print the attributes along with “starting”)
class Vehicle:
    wheels = 4
    no_of_doors = 4
    def __init__(self, color, type_of_vehicle, year_of_market_release):
        self.color = color
        self.type_of_vehicle = type_of_vehicle
        self.year_of_market_release = year_of_market_release
        
        
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        if color == 'White':
            self.color=color
            print('\tColor changed')
        else:
            print('\tNot allowed')
            
    def describeVehicle(self):
        print(self.color,'\t', self.type_of_vehicle,'\t', self.year_of_market_release, '\t', self.wheels, '\t', self.no_of_doors)

    def brakeCar(self):
        self.describeVehicle()
        print('\tBraking')
        
    def startCar(self):
        self.describeVehicle()
        print('\tStarting')
        
    
def main():
    veh1=Vehicle('Black','Bike',2011)
    veh1.describeVehicle()
    veh1.brakeCar()
    veh1.startCar()
    veh2=Vehicle('White','Car',2010)
    veh2.describeVehicle()
    veh2.set_color('White')
    veh2.brakeCar()
    veh2.startCar()

if __name__=='__main__':
    main()


# In[ ]:


#2.Create a dictionary for Vehicle objects in which the objects having the same value for “year_of_market_release” are grouped 
#together with the key being the year_of_market_release and the value being the list of objects having the attribute 
#year_of_market_release equal
class Vehicle:
    wheels = 4
    no_of_doors = 4
    def __init__(self, color, type_of_vehicle, year_of_market_release):
        self.color = color
        self.type_of_vehicle = type_of_vehicle
        self.year_of_market_release = year_of_market_release
        
def main():
    v1=Vehicle('Red','Merc',2010)
    v2=Vehicle('White','Audi',2012)
    v3=Vehicle('Blue','Merc',2011)
    v4=Vehicle('Yellow','Ferrari',2011)
    v5=Vehicle('Black','BMW',2013)
    list1=[v1,v2,v3,v4,v5]
    dict1={}
    for i in list1:
        print(i.year_of_market_release)
        if (i.year_of_market_release) in dict1.keys():
            dict1[i.year_of_market_release].append(i)
        else:
            dict1[i.year_of_market_release]=[i]
            
    for key,value in dict1.items():
        print('\t',key)
        for item in value:
            print('\t\t',item.type_of_vehicle)

if __name__=='__main__':
    main()


# In[ ]:


#3.Create a class Plate that has a method called add_to_plate(), remove_from_plate() and display_items_on_plate(). 
#The Plate object will initially be empty and have an attribute called items_on_plate which should be a list and 
#whenever add_to_plate() is called with an item argument which is a string, add that item to the items_on_plate, 
#similarly if remove_from_plate() is called with an item, if that item is present in items_on_plate remove it, 
#else print “Item not on plate” and whenever display_items_on_plate() is called, print the list items_on_plate.
class Plate:
    def __init__(self):
        self.items_on_plate=[]
        
    def add_to_plate(self,item):
        self.items_on_plate.append(item)
        
    def remove_from_plate(self,item):
        self.items_on_plate.remove(item)
        
    def display_items_on_plate(self):
        print(self.items_on_plate)
        
p=Plate()
p.add_to_plate("Paneer")
p.display_items_on_plate()
p.remove_from_plate('Paneer')
p.display_items_on_plate()


# In[ ]:


l1=[[5,6],[2,3],[7,5],[1,1],[4,3],[9,1],[2,1]]
l1.sort(key=lambda x: (x[-1],x[0]))
print(l1)


# # OOPS Practise 23/02/2023

# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# # OOPS Practise 24/022023

# In[ ]:


#1.Complete the above Day 4 problem 3 question for the others
class Number:
    def __init__(self,value):
        self.value=value
    
    def __add__(self,other):
        return self.value+other.value
    
    def __sub__(self,other):
        return self.value-other.value
    
    def __mul__(self,other):
        return self.value*other.value
    
    def __truediv__(self,other):
        return self.value/other.value
    
    def __floordiv__(self,other):
        return self.value//other.value
    
    def __mod__(self,other):
        return self.value%other.value
    
    def __pow__(self,other):
        return self.value**other.value
        
def main():
    n1=Number(10)
    n2=Number(5)
    print(n1+n2)
    print(n1-n2)
    print(n1*n2)
    print(n1/n2)
    print(n1//n2)
    print(n1%n2)
    print(n1**n2)
    
if __name__=='__main__':
    main()


# In[ ]:


#2.Choose any class of your liking and write 2 instance variable, 1 class variable, and write one class method that can change 
#the value of that class variable and one class method that can display the value of that class variable, write a static method 
#that does not utilise either the class variable or the instance variable
class State:
    state_name='Maharashtra'
    def __init__(self,state_id,capital):
        self.state_id=state_id
        self.capital=capital
    
    @classmethod
    def change_state_name(cls,state_name):
        cls.state_name=state_name
        
    @classmethod
    def display_state_name(cls):
        return cls.state_name
        
    @staticmethod
    def addition(economy):
        return economy
    
def main():
    s1=State(1,'Mumbai')
    print('Name:-',s1.state_name,'\tId:-',s1.state_id,'\tCapital:-',s1.capital)
    State.change_state_name('Uttar Pradesh')

    print(State.display_state_name())
    
if __name__=='__main__':
    main()


# In[ ]:


#3.Create a Calculator class that only has add and subtract functionality in which we can pass 2 numbers or 3 numbers as 
#arguments to the addNumbers or subtractNumbers methods. Try using default values in the method or the dispatch keyword.
from multipledispatch import dispatch

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    @dispatch()
    def addNumbers(self):
        return self.num1+self.num2

    @dispatch()
    def subtractNumbers(self):
        return self.num1-self.num2
    
    @dispatch()
    def mulNumbers(self):
        return self.num1*self.num2

    @dispatch()
    def divNumbers(self):
        return self.num1/self.num2
    
    @dispatch()
    def floordivNumbers(self):
        return self.num1//self.num2

    @dispatch()
    def modNumbers(self):
        return self.num1%self.num2
    
    @dispatch()
    def powerNumbers(self):
        return self.num1**self.num2

def main():
    c1=Calculator(10,5)
    print(c1.addNumbers())
    print(c1.subtractNumbers())
    print(c1.mulNumbers())
    print(c1.divNumbers())
    print(c1.floordivNumbers())
    print(c1.modNumbers())
    print(c1.powerNumbers())
    
if __name__=='__main__':
    main()


# # OOPS Practise 28/02/2023

# In[ ]:


#3.Create a Calculator class that only has add and subtract functionality in which we can pass 2 numbers or 3 numbers as 
#arguments to the addNumbers or subtractNumbers methods. Try using default values in the method or the dispatch keyword.
from multipledispatch import dispatch

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    @dispatch()
    def addNumbers(self):
        return self.num1+self.num2

    @dispatch()
    def subtractNumbers(self):
        return self.num1-self.num2
    
    @dispatch()
    def mulNumbers(self):
        return self.num1*self.num2

    @dispatch()
    def divNumbers(self):
        return self.num1/self.num2
    
    @dispatch()
    def floordivNumbers(self):
        return self.num1//self.num2

    @dispatch()
    def modNumbers(self):
        return self.num1%self.num2
    
    @dispatch()
    def powerNumbers(self):
        return self.num1**self.num2

def main():
    c1=Calculator(10,5)
    print(c1.addNumbers())
    print(c1.subtractNumbers())
    print(c1.mulNumbers())
    print(c1.divNumbers())
    print(c1.floordivNumbers())
    print(c1.modNumbers())
    print(c1.powerNumbers())
    
if __name__=='__main__':
    main()


# In[ ]:


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


# # OOPS Practise 01/03/2023

# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# # OOPS Practise 02/03/2023

# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# # OOPS Practise 03/03/2023 

# In[ ]:


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


# In[ ]:


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
    s1=Student("Pune","Harshal")
    u1._University__print_university_details()
    c1._University__print_university_details()
    c1.print_college_details()
    s1.print_student_details()
    #s1._University__print_university_details()
    s1.change_university_name("Mumbai University")
    #s1._University__print_university_details()
    
if __name__=='__main__':
    main()


# In[ ]:


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


# In[ ]:


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


# # OOPS Practise 04/03/2023

# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# # OOPS Practise 06/03/2023

# In[ ]:


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


# In[ ]:


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


# In[ ]:


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


# # OOPS Practise 08/03/2023

# In[ ]:


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


# In[ ]:


#1.Write a Python program to triple all numbers in a given list of integers, use map.
list1=[1,2,3,4,5,6,7,8,9]
print(list(map(lambda x: x*3,list1)))


# In[ ]:


#2.Write a Python program to add three given lists using Python map and lambda
list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]
print(list(map(lambda x1,x2,x3:x1+x2+x3,list1,list2,list3)))


# In[ ]:


#3.Write a Python program to convert a given list of integers into a list of strings. Use map and lambda
list1=[1,2,3,4,5,6,7,8,9]
print(list(map(lambda x:str(x),list1)))
print(list(map(str,list1)))


# In[ ]:


#4.Using the filter function, filter the even numbers so that only odd numbers are passed to the new list.
list1=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2!=0,list1)))


# In[ ]:


#5.Using filter() function filter the list so that only negative numbers are left.
list1=[-1,2,-3,4,-5,-6,7,8,-9]
print(list(filter(lambda x: x<0,list1)))


# In[ ]:


#6.Using filter() and list() functions and .lower() method filter all the vowels in a given string 
#str = "Winter Olympics in 2022 will take place in Beijing China”
string = "Winter Olympics in 2022 will take place in Beijing China"
print(list(filter(lambda x: x.lower() in 'aeiou',string)))


# In[ ]:


#7.Using map() and filter() functions add 2000 to the values below 8000 for lst1 = [1000, 500, 600, 700, 5000, 90000, 17500]
list1 = [1000, 500, 600, 700, 5000, 90000, 17500]
print(list(map(lambda x:x+2000,filter(lambda x: x<8000,list1))))


# In[ ]:


#8.Use reduce to find the average of all numbers in a list
list1=[1,2,3,4,5,6,7,8,9,9]
print(reduce(lambda x,y:x+y,list1)/len(list1))


# In[ ]:


#9.Find the max number in a list using reduce
list1=[1,2,3,4,5,6,7,8,9,9]
print(reduce(max,list1))


# In[ ]:


#10.Filter only negative and zero in the list using list comprehension numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_no=[i for i in numbers if i<=0]
print(filter_no)


# In[ ]:


#11.Flatten the following list of lists of lists to a one dimensional list :
#list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]] output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
x=[k for i in list_of_lists for j in i for k in j]
print(x)


# # OOPS Practise 10/03/2023

# In[ ]:


#1.Write a generator that generates prime numbers in the range 1 to 5000
def isPrime():
    for num in range(1,5000):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                yield num
            
def main():
    p=isPrime()
    for i in p:
        print(i)
    
if __name__=="__main__":
    main()


# In[ ]:


#2.Rewrite the below code to utilise a generator function instead of using map and lambda
#names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
#names = map(lambda name: name.strip().title(), names)
def name():
    names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy   "]
    
    for name in names:
        print(name)
    print("\n")
    
def new1():
    names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy   "]
    for name in names:
        yield (name.strip().title())
        
        
def main():
    n=new1()
    a=[]
    for i in n:
        a.append(i)
    print(a)

    
if __name__=="__main__":
    main()


# In[ ]:


#3.Write a decorator called printer which causes any decorated function to print their return values. 
#If the return value of a given function is None, printer should do nothing
def Printer(function):
    def inner_code():
        f=function()
        if(f==None):
            print("Nothing")
        else:
            print("1")
    return inner_code
     
@Printer
def numbers():
    a=1
    if a>=1:
        return 1
    else:
        return None
    
def main():
    numbers()
    
if __name__=="__main__":
    main()


# In[ ]:


#4.Imagine you have a list called toys, which several functions in your application interact with. 
#Write a decorator which causes your functions to run only if toys is not empty.
def application(function):
    def inner_code():
        func=function()
        if func==None:
            print("Not Working!!! List is empty")
        else:
            print("Its working")
    return inner_code

@application
def Toy():
    toys=['Train','Panda','Truck','Car','Doll']
    if len(toys)==0:
        return None
    else:
        return 1

def main():
    Toy()
    
if __name__=="__main__":
    main()


# In[ ]:


#5.Write a method addNumbers which adds 2 numbers and create a decorator absoluteSum which utilises the arguments to addNumbers 
#and returns the sum of the absolute values of the numbers.
def absoluteSum(function):
    def inner_code():
        func=function()
        if func==None:
            print(abs(sum1))
        else:
            print(sum1)
    return inner_code

@absoluteSum
def addNumbers():
    sum1=2+3
    if sum1>0:
        return None
    else:
        print(0)

def main():
    addNumbers()
    
if __name__=="__main__":
    main()


# # Practise 11/03/2023

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Practise 13/03/2023

# In[ ]:


#1.Create a Python Program that serialises and deserialises a dictionary of dictionaries using JSON and pickle
import json
import pickle

def main():
    person={"dict1":{"name":'Harshal','age':22},"dict2":{"name":'Vaibhav','age':25}}
    
    json_data=json.dumps(person)
    print("JSON Serialization: ",json_data)
    
    json_dict=json.loads(json_data)
    print('JSON Deserilization: ',json_dict)
    
    pickle_data=pickle.dumps(person)
    print("PICKELE Serialization: ",pickle_data)
    
    pickle_dict=pickle.loads(pickle_data)
    print('PICKLE Deserilization: ',pickle_dict)

if __name__=='__main__':
    main()


# In[ ]:


#2.Create a Python Program that serialises and deserialises a class VideoGameCharacter using JSON and pickle. 
#Create 4 parameters for VideoGameCharacter
import json
import pickle

class VideoGameCharacter:
    def __init__(self,char_name,level,game_name,rating):
        self.char_name=char_name
        self.level=level
        self.game_name=game_name
        self.rating=rating
        
    def print_attributes(self):
        print('VideoGameCharacter attributes are: ',self.char_name,'\t',self.level,'\t',self.game_name,'\t',self.rating)
        
def main():
    v1=VideoGameCharacter('Pokemon','2','PokemonGO',4)
    print(v1.__dict__)
    v1_ser=json.dumps(v1.__dict__)
    print("\nJSON Serialization: ",v1_ser)
    v1_deser=json.loads(v1_ser)
    print("JSON Deserialization: ",v1_deser)
    
    v2=VideoGameCharacter('Player1','10','Temple Run',5)
    v2_ser=pickle.dumps(v2.__dict__)
    print("\nPICKLE Serialization: ",v2_ser)
    v2_deser=pickle.loads(v2_ser)
    print("Pickle Deserialization: ",v2_deser)
    
if __name__=='__main__':
    main()


# In[ ]:


#3.Create a Python Program that serialises and deserialises a class VideoGame using JSON and pickle. 
#Create 1 parameter for VideoGame which is a list of VideoGameCharacters [give min 2 characters]
import json
import pickle

class VideoGameCharacter:
    def __init__(self,char_name,level,game_name,rating):
        self.char_name=char_name
        self.level=level
        self.game_name=game_name
        self.rating=rating
        
    def print_attributes(self):
        print('VideoGameCharacter attributes are: ',self.char_name,'\t',self.level,'\t',self.game_name,'\t',self.rating)
        
class VideoGame:
    def __init__(self,characters=[]):
        self.characters=characters
        
    def print_attributes(self):
        for i in self.characters:
            i.print_attributes()
        
def main():
    v1=VideoGameCharacter('Pokemon','2','PokemonGO',4)
    print(v1.__dict__)
    v1_ser=json.dumps(v1.__dict__)
    print("\nJSON Serialization: ",v1_ser)
    v1_deser=json.loads(v1_ser)
    print("JSON Deserialization: ",v1_deser)
    
    v2=VideoGameCharacter('Player1','10','Temple Run',5)
    v2_ser=pickle.dumps(v2.__dict__)
    print("\nPICKLE Serialization: ",v2_ser)
    v2_deser=pickle.loads(v2_ser)
    print("Pickle Deserialization: ",v2_deser)
    
    vg=VideoGame([v1,v2])
    vg.print_attributes()
    vg_ser=pickle.dumps(vg)
    print("\nPICKLE Serialization: ",vg_ser)
    vg_deser=pickle.loads(vg_ser)
    vg_deser.print_attributes()
    print("Pickle Deserialization: ",vg_deser)
    
    vg_ser=json.dumps(vg.__dict__,default=lambda o:o.__dict__)
    print("\nJSON Serialization: ",vg_ser)
    vg_deser=json.loads(vg_ser)
    vg_deser.print_attributes()
    print("JSON Deserialization: ",vg_deser)
    
if __name__=='__main__':
    main()

