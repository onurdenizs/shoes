"""This class will hold the necessary functions and class properties for shes"""

import itertools
import model
import brand
import csv
class Shoe:
    id_iter = itertools.count() #this will be used to give a unique id for each shoe in the database
    shoe_db = []
    def __init__(self, brand_name, model_name, gender, terrain_type, pace, arch_support, weight, price) -> None:
        
        self.id = next(Shoe.id_iter) # here we increment the id by 1
        if brand.Brand.get_brand_by_brand_name(brand_name) == None:
            self.brand = brand.Brand(brand_name)
        else:
            self.brand = brand.Brand.get_brand_by_brand_name(brand_name)
        
        self.model = model.ShoeModel(model_name,self.brand)
        
        self.gender = gender.lower() #this should be in string "male" or "female" 
        self.terrain_type =terrain_type.lower() #this should be in string
        self.pace = pace #this should be in string
        self.arch_support = arch_support #this should be in string
        self.weight= weight #this should be numeric
        self.price = price  #this should be numeric
        self.shoe_db.append(self)
    def __repr__(self) -> str:
        return "{0} {1}".format(self.brand.brand_name, self.model.model_name) 


    def initialize_program_shoes():
        print("Initializing Shoe Database")
        with open('shoe_db.csv', 'r') as file:
            reader = csv.DictReader(file)
            for shoe in reader:
                
                Shoe(shoe["brand_name"],shoe["model_name"],shoe["gender"],shoe["terrain_type"],shoe["pace"],shoe["arch_support"],int(shoe["weight"]),int(shoe["price"]))
