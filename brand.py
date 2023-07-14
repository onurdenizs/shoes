"""This class will hold the necessary functions and class properties for Brands"""

import itertools

class Brand:
    id_iter = itertools.count() #this will be used to give a unique id for each brand in the database

    def __init__(self, brand_name) -> None:
        self.id = next(Brand.id_iter) # here we increment the id by 1
        self_name = brand_name #this hould be in string