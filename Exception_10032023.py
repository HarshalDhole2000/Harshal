#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exceptions
#Types of exceptions

def main():
    #SyntaxError
    #print 'Hello World' -> print("Hello World")
    
    #NameError
    #print(name)
    name='Ram'
    print(name)
    
    #IndexError
    my_list=[1,2,3,4,5]
    #print(my_list[7])
    print(my_list[0],my_list[2])
    
    #ModuleNotFoundError
    #import maths -> import math
    
    #AttributeError
    import math
    #print(math.PI)
    print(math.pi)
    
    #KeyError
    person_data={'name':'Ram','country':'India'}
    #print(person_data['county'])
    print(person_data['country'])
    
    #TypeError
    num=4
    my_str='3'
    #print(num+my_str)
    print(str(num)+my_str)
    
    #ImportError
    #from math import power
    from math import pow
    
    #ValueError
    #print(int('12z'))
    print(int(12))
    
    #ZeroDivisionError
    my_list=[1,0]
    #print(1/0)
    #print(num/my_list[1])
    
if __name__=="__main__":
    main()


# In[3]:


#Exception handling

def input_func(idx):
    try:
        #print("Index is: ",idx)
        my_list=[1,2,3]
        return my_list[idx]
    except Exception as e:
        print(e)
        return -1
    
def main():
    var1=2
    var2=4
    if var1>3:
        raise Exception("The var value is more than 3, Value provided: {}".format(var1))
        
    #AssertionError
    assert (var2>3), "The variable var is less than 3"
    
    #try except
    try:
        assert (var2>3),"The variable var is less than 3"
        zero_val=12/0
    except AssertionError as ae:
        print("Error caught: ",ae)
    except ZeroDivisionError as ze:
        print("Error caught: ",ze)
    else:
        print("Reached here because there were no exceptions")
        try:
            a=4
            b=5
            c=a+b
        except Exception as ex:
            print(ex)
    finally:
        print("This block will be called at the end.")
        
    try:
        my_list=[1,2,3]
        print(my_list[100])
    except IndexError as ie:
        print(ie)
    except LookupError as le:
        print(le)
    except Exception as e:
        print(e)
        
    """
    except AssertionError as ae:
        print("Error caught: ",ae)
    except ZeroDivisionError as ze:
        print("Error caught: ",ze)
    except Exception as e:
        print("Error caught: ",e)
    """
    
    while True:
        idx=input("Enter a value: ")
        idx=int(idx)
        ret_val=input_func(idx)
        print("Ret_val is: ",ret_val)
        if ret_val==-1:
            print("Index was out of bounds, Please enter proper value")
        else:
            break
            
if __name__=="__main__":
    main()


# # Practise

# In[50]:


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


# In[58]:


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


# In[69]:


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


# In[87]:


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


# In[107]:


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

