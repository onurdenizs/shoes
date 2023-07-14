"""This class will hold the necessary functions and class properties for Brands"""

import itertools

class Brand:
    id_iter = itertools.count() #this will be used to give a unique id for each brand in the database
    brand_db = []
    
    def __init__(self, brand_name) -> None:
        self.id = next(Brand.id_iter) # here we increment the id by 1
        self.brand_name = brand_name #this hould be in string
        Brand.brand_db.append(self)
        self.model_list = []
    
    def get_brand_by_brand_name(brand_name):
        """This functions gets a name as string and returns the brand with that name
        if no brand exists with that name it returns None"""
        brand = None
        for item in Brand.brand_db:
            if item.brand_name.lower() == brand_name.lower():
                brand = item
                break
        return brand