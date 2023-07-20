

import itertools
import model
import brand
import csv
class Shoe:
    """
    This class represents the shoes

     Attributes:
        id_iter:     this will be used to give a unique id for each shoe in the database
        shoe_db:     every instance of shoe class will be added to this list after creation
    """
    id_iter = itertools.count() 
    shoe_db = [] 
    def __init__(self, brand_name, model_name, gender, terrain_type, pace, arch_support, weight, price) -> None:
        """
        param:
        brand_name: Name of the shoe brand (i.e. Asics, Nike etc.) Data type is str
        model_name: Model of the shoe. Data type is str
        gender: Gender is etiher "Male" or "Female" Data type str
        terrain_type: Can be "road" or "trail" Data type str
        pace: can be "daily" , "tempo" or "competition" data type is str
        arch_support: can be "neutral" or "stability" data type is str
        weight: weight of the shoe should be in gram data type is str
        price: price of the shoe in US Dollars data type is str
        """
        self.id = next(Shoe.id_iter) # here we increment the id by 1

        """Here we check if the given brand_name is used before
        if the given brand name is used for the first time we first create a new Brand Class instance with this brand name
        and assign it to this shoe's brand_name
        
        else the brand name is used before it means that brand is already created.
        so this already created brand is assigned as this shoe's brand_name"""
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


    def initialize_program_shoes(filen_name):
        """
        initializes shoe database. Gets shoe infos from a csv file 
        and creates the shoedb list 

        param:
        filen_name: name of the csv file which holds the shoe information data type is str      
        """
        with open(filen_name, 'r') as file:
            reader = csv.DictReader(file)
            for shoe in reader:
                
                Shoe(shoe["brand_name"],shoe["model_name"],shoe["gender"],shoe["terrain_type"],shoe["pace"],shoe["arch_support"],int(shoe["weight"]),int(shoe["price"]))
