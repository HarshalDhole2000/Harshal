#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#constructor overloading
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __init__(self):
        self.name='Name'
        
def main():
    s1=Student()
    print('Object Created')
    
if __name__=='__main__':
    main()


# In[ ]:


#delete object
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def get_age(self):
        return self.age
    
def main():
    s1=Student('Ram',24)
    s2=Student('Shyam',25)
    print(s1.age)
    del s1.age
    print(s1.name)
    print(s2.name,s2.age)
    
if __name__=='__main__':
    main()


# In[ ]:


#encapsulation
class Student:
    def __init__(self,name,age=22):
        self.name=name
        self.age=age
        
    def print_student_info(self):
        print('Name:-',self.name,'\tAge:-',self.age)
        
def main():
    s1=Student('Ram',24)
    s2=Student('Shyam')
    s1.print_student_info()
    s2.print_student_info()
    
if __name__=='__main__':
    main()


# In[ ]:


#protected variable
class Animal:
    def __init__(self,name,species,nickname):
        self.name=name
        self._species=species
        self.__nickname=nickname
        
    def get_species(self):
        return self._species
    
class Dog(Animal):
    def __init__(self,name,species,nickname):
        super(Dog,self).__init__(name,species,nickname)
        
    def get_dog_species(self):
        
        return self.__nickname
    
def main():
    a1=Animal('Ceaser','Cat','Cathy')
    print(a1.name,a1._species,a1.get_species())
    d1=Dog('Tiger','Dog','Jimmy')
    print(d1.name,d1._species,d1.get_dog_species())
    
if __name__=='__main__':
    main()


# In[ ]:


#polymorphism
class ShoppingBag:
    def __init__(self,shoes,clothes,socks):
        self.shoes=shoes
        self.clothes=clothes
        self.socks=socks
        
    def __len__(self):
        return self.shoes*2+self.clothes+self.socks*2
        
    def __add__(self,other):
        return (self.shoes*2+self.clothes+self.socks*2) + (other.shoes*2+other.clothes+other.socks*2)
    
    def __mul__(self,other):
        return (self.shoes*2+self.clothes+self.socks*2) * (other.shoes*2+other.clothes+other.socks*2)
    
def main():
    bag1=ShoppingBag(4,4,4)
    bag2=ShoppingBag(5,5,5)
    print(len(bag1))
    print(len(bag2))
    print(bag1+bag2)
    print(bag1*bag2)
    
if __name__=='__main__':
    main()


# # Practise 

# In[53]:


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


# In[52]:


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


# In[65]:


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


# In[67]:


l1=[[5,6],[2,3],[7,5],[1,1],[4,3],[9,1],[2,1]]
l1.sort(key=lambda x: (x[-1],x[0]))
print(l1)

