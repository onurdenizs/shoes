"""This class will hold the necessary functions and class properties for shes"""

import itertools

import brand
class Shoe:
    id_iter = itertools.count() #this will be used to give a unique id for each shoe in the database

    def __init__(self, brand, model_name, gender, terrain_type, pace, arch_support, weight, price) -> None:
        
        self.id = next(Shoe.id_iter) # here we increment the id by 1
        self.brand = brand #this should be in brand class
        self.model_name = model_name.lower() #this should be in string
        self.gender = gender.lower() #this should be in string "male" or "female" 
        self.terrain_type =terrain_type.lower() #this should be in string
        self.pace = pace #this should be in string
        self.arch_support = arch_support #this should be in string
        self.weight= weight #this should be numeric
        self.price = price  #this should be numeric
    
    def __repr__(self) -> str:
        return "{0} {1}".format(self.brand.name, self.model_name) 

