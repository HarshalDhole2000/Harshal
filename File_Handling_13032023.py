#!/usr/bin/env python
# coding: utf-8

# In[53]:


#File Handling
import json 
import csv

def main():
    #file syntax
    #Reading from a file
    """
    f=open("test_file.txt","w")
    print(f)
    
    txt=f.read()
    print(type(txt))
    print(txt)
    
    #read partially
    txt=f.read(7)
    print(type(txt))
    print(txt)
    f.close()
    
    #read file line by line
    line=f.readline()
    print(type(line))
    print(line)
    line2=f.readline()
    print(type(line2))
    print(line2)
    
    lines=f.readlines()
    print(type(lines))
    print(lines)
    print(lines[1])
    f.close()
    """
    
    with open('test_file.txt','w') as f:
        f.write("This is test file.\n")
    
    with open("test_file.txt","r") as f:
        txt=f.read()
    print(txt.splitlines())
    
    #writing to a file
    with open('test_file.txt','w') as f:
        f.write("This is some other random text for a new file.\n")
        
    #appending to a file
    with open('test_file.txt','a') as f:
        f.write("This is some other random text for a new file at the end.\n")
        
    #deleting a file
    import os
    if os.path.exists("./test_file_2.txt"):
        os.remove("./test_file_2.txt")
    else:
        print("Please check if the file exists")
        
    #JSON Files
    person={}
    person['Name']="Shantanu"
    person['Address']='123,Janpath,East Andheri'
    person['Age']=21
    person['Height']='170 cm'
    person['Weight']='55 kgs'
    
    json_str=json.dumps(person)
    print(type(json_str),json_str)
    
    with open("person.json",'w') as f:
        json.dump(person,f)
        
    #csv files
    with open('test_csv.csv','r') as f:
        csv_file=csv.reader(f)
        print(type(csv_file))
        print(csv_file)
        for idx,row in enumerate(csv_file):
            if idx==0:
                #This is the first row which contains the col names
                pass
        else:
            #Do the processing that is required
            print(row)
            row_add=sum(map(int,row))
            print(row_add)
            
if __name__=='__main__':
    main()


# In[42]:


#Debugging
import pdb

def perform_division(a,b):
    return a/b

def perform_mul(a,b):
    return a*b

def main():
    a=1
    b=1
    perform_division(a,b)
    perform_mul(a,b)
    for i in range(5):
        print(i)
    #list, list(1,5), continue, next/n, step/s, break <line_num>, pp <var_name>, <var_name>, quit/exit, whatis <var_name>,help
    
if __name__=='__main__':
    main()


# # Practise

# In[19]:


#1.Create a Python Program that serialises and deserialises a dictionary of dictionaries using JSON and pickle
import json
import pickle

def main():
    person={"dict1":{"name":'Tushar','age':24},"dict2":{"name":'Vaibhav','age':25}}
    
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


# In[28]:


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


# In[2]:


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
    ''''''
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

