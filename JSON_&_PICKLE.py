#!/usr/bin/env python
# coding: utf-8

# In[15]:


import json
import codecs

person={}
person['Name']='Shantanu'
person['Address']='123,Janpath,East Andheri'
person['Age']=21
person['Height']='170 cm'
person['Weight']='55 kgs'


#Javascript Object Notation
#Serialization
with open('person.json','w') as f:
    json.dump(person,f)


#Deserialization
with open('person.json','r') as f:
    person_dict=json.load(f)
    
print(person_dict)
print(person_dict['Name'])

person_list=[person_dict,person_dict]
with open('person_list.json','w') as f:
    json.dump(person_list,f)
    
with open('person_list.json','r') as f:
    person_list_from_file=json.load(f)
    
print(person_list_from_file)

class Animal:
    def __init__(self,name,animal_type):
        self.name=name
        self.animal_type=animal_type
        
        def print_attr(self):
            print("Animal attributes are: ",self.name,self.animal_type)
            
class Zoo:
    def __init__(self,animals):
        self.animals=animals
        
        def print_attr(self):
            print("Zoo attributes are: ",self.animals)
            for _animal in self.animals:
                _animal.print_attr()
                
        @statismethod
        def from_json(zoo_json):
            zoo_dict=json.loads(zoo_json)
            zoo_obj_new=Zoo(**zoo_dict)
            animal_lst=[]
            for _animal in zoo_obj_new.animals:
                animal_lst.append(Animal(**_animal))
            zoo_obj_new.animals=animal_lst
            return zoo_obj_new
        
animal=Animal("Ceaser","Dog")
print(animal.__dict__)
#In a memory Serialization
animal_obj_ser=json.dumps(animal.__dict__)
print("Json dumps: ",animal_obj_ser,type(animal_obj_ser))

#Deserialization
animal_obj_deser=json.loads(animal_obj_ser)
print(animal_obj_deser,type(animal_obj_deser))
new_animal_obj=Animal(**animal_obj_deser)
new_animal_obj.print_attr()

animal_dog=Animal("Ceaser","Dog")
animal_cat=Animal("Mandu","Cat")

animal_list=[animal_cat,animal_dog]
zoo=Zoo(animal_list)
zoo.print_attr()

zoo_json=json.dumps(zoo.__dict__,default=lambda o:o.__dict__)
print(zoo_json)

"""
zoo_dict=json.loads(zoo_json)
print(zoo_dict)
zoo_obj_new=Zoo(**zoo_dict)
zoo_obj_new.print_attr()
"""

zoo_obj_new=Zoo.from_json(zoo_json)
zoo_obj_new.print_attr()

if __name__=='__main__':
    main()


# In[19]:


import pickle

person={}
person['Name']='Shantanu'
person['Address']='123,Janpath,East Andheri'
person['Age']=21
person['Height']='170 cm'
person['Weight']='55 kgs'

person_list=[person,person]

with open('dict.pkl','w') as f:
    json.dump(person,f)


with open("dict.pkl","r") as f:
    person_dict=pickle.load(f)
    
print(person_dict,type(person_dict))

class Animal:
    def __init__(self,name,animal_type):
        self.name=name
        self.animal_type=animal_type
        
        def print_attr(self):
            print("Animal attributes are: ",self.name,self.animal_type)
            
animal=Animal("Caeser","Dog")
with open("animal.pkl","wb") as f:
    pickle.dump(animal,f)
    
with open("animal.pkl","rb") as f:
    animal_obj=pickle.load(f)
    animal_obj.print_attr()
    
list_mem_ser=pickle.dumps(person_list)
print(type(list_mem_ser))
new_lst=pickle.loads(list_mem_ser)
print(new_lst)
print(new_lst==person_list)

if __name__=='__main__':
    pass


# # Practise 

# In[ ]:


#1.Create a short program that prompts the user for a list of grades separated by commas. Split the string into individual 
#grades and use a list comprehension to convert each string to an integer. You should use a try statement to inform the 
#user when the values they entered cannot be converted.




# In[ ]:


#2.Investigate what happens when there is a return statement in both the try clause and finally clause of a try statement.


# In[ ]:


#3.Ask the user for an integer between 1 and 10 (inclusive). If the number they give is outside of the specified range, 
#raise a ValueError and inform them that their choice was invalid.


# In[ ]:


#4.Write a function division() that accepts two arguments. The function should be able to catch an exception such as 
#ZeroDivisionError, ValueError, or any unknown error you might come across when you are doing a division operation.


# In[ ]:


#5.Modify the earlier division function in such a way that the function division() has a clean-up action using finally

