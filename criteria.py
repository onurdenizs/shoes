"""This class will hold the necessary functions and class properties for criterias"""
import math

import itertools

class Criteria:
    id_iter = itertools.count() #this will be used to give a unique id for each brand in the database

    def __init__(self, text, choices, value=None, is_numeric=False) -> None:
        self.id = next(Criteria.id_iter) # here we increment the id by 1
        self.text = text #this should be in string
        self.is_numeric = is_numeric # this should be True or False
        self.choices = choices
        self.value = value


