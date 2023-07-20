"""This class will hold the necessary functions and class properties for criterias"""
import math

import itertools
import brand
class Criteria:
    id_iter = itertools.count() #this will be used to give a unique id for each brand in the database
    criteria_db = []
    def __init__(self, text, choices=[], current_value=None, is_numeric=False) -> None:
        self.id = next(Criteria.id_iter) # here we increment the id by 1
        self.text = text #this should be in string
        self.is_numeric = is_numeric # this should be True or False
        self.choices = choices #this is a List of choices
        self.current_value = current_value #numeric
        Criteria.criteria_db.append(self)
        #print(self.choices)

    def initialize_program_criterias():
        """this function creates all the neccessary criterias for the program"""
        """You need to create brand list with initialize_program_brands() function before using this function"""
        
        criteria_list = []
        criteria_list.append(Criteria("Gender",["Male", "Female"], None))
        criteria_list.append(Criteria("Brand",brand.Brand.branddb_to_string(brand.Brand.brand_db),None))
        criteria_list.append(Criteria("Terrain",["Road", "Trail"], None))
        criteria_list.append(Criteria("Pace",["Daily", "Tempo", "Competition"], None))
        criteria_list.append(Criteria("Arch Support",["Neutral", "Stability"], None))
        criteria_list.append(Criteria("Max Weight", [], None, True))
        criteria_list.append(Criteria("Max Price", [], None, True))
        return criteria_list        


