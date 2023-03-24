#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Class method class variable
class Student:
    school_name='Ganesh Vidya Mandir'
    
    def __init__(self,name):
        self.name=name
        
    @classmethod
    def change_school_name(cls,school_name):
        cls.school_name=school_name
        
    @classmethod
    def fetch_school_name(cls):
        return cls.school_name
    
    def get_name(self):
        return self.name
        
def main():
    s1=Student('Ram')
    s2=Student('Shyam')
    print(s1.get_name())
    print(s2.get_name())
    print('\n',s1.school_name)
    print(s2.school_name)
    print(Student.school_name)
    s1.school_name='Vighnahar Vidyalaya'
    print('\n',s1.school_name)
    print(s2.school_name)
    print(Student.school_name)
    s2.school_name='Saraswati Vidyalaya'
    print('\n',s1.school_name)
    print(s2.school_name)
    print(Student.school_name)
    
if __name__=='__main__':
    main()


# In[ ]:


#Class methot classmethod internal
class Student:
    school_name='Ganesh Vidya Mandir'
    
    def __init__(self,name):
        self.name=name
        
    def change_school_name(cls,school_name):
        cls.school_name=school_name
        
def main():
    s1=Student('Ram')
    print(s1.name,'\t',s1.school_name)
    s2=Student('Shyam')
    print(s2.name,'\t',s2.school_name)
    Student.change_school_name(s1,'Vighnahar Vidyalaya')
    print(s1.school_name)
    Student.change_school_name=classmethod(Student.change_school_name)
    Student.change_school_name('Saraswati Vidyalaya')
    print(Student.school_name)
    
if __name__=='__main__':
    main()


# In[ ]:





# In[ ]:


#Class method classmethod external
class Student:
    school_name='Ganesh Vidya Mandir'
    
    def __init__(self,name):
        self.name=name
        
def another_change_school_name(cls,school_name):
    cls.school_name=school_name
    
def main():
    s1=Student('Ram')
    Student.another_change_school_name=classmethod(another_change_school_name)
    Student.another_change_school_name('Saraswati Vidyalaya')
    print(Student.school_name)
    
if __name__=='__main__':
    main()


# In[ ]:


#Class method delattr
class Student:
    school_name='Ganesh Vidya Mandir'
    
    def __init__(self,name):
        self.name=name
        
    @classmethod
    def change_school_name(cls,school_name):
        cls.school_name=school_name
        
def main():
    #del Student.change_school_name
    delattr(Student,'change_school_name')
    Student.change_school_name('Vighnahar Vidyalaya')
    
if __name__=='__main__':
    main()


# # Practise

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


# In[ ]:


#4.Create a class Stack and implement the push() and pop() and size() methods. 
#Example stack: 
#stack = []
#push(1)-->[1]
#push(2)-->[1,2]
#push(4)-->[1,2,4]
#push(10)-->[1,2,4,10]
#pop()-->[1,2,4]
#pop()-->[1,2]

