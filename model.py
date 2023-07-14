"""This is the class for shoe models"""
import itertools

class ShoeModel:
    id_iter = itertools.count() #this will be used to give a unique id for each model in the database
    shoe_model_db = []

    def __init__(self, model_name, model_brand) -> None:
        self.id = next(ShoeModel.id_iter) # here we increment the id by 1
        self.model_name = model_name #this should be in string
        self.brand = model_brand
        model_brand.model_list.append(self)
        ShoeModel.shoe_model_db.append(self)
        

