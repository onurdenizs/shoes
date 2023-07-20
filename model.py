
import itertools

class ShoeModel:
    """This is the class for shoe models
    
     Attributes:
        id_iter:     this will be used to give a unique id for each shoe in the database
        shoe_model_db:     every instance of brand class will be added to this list after creation
    """
    id_iter = itertools.count() #this will be used to give a unique id for each model in the database
    shoe_model_db = []

    def __init__(self, model_name, model_brand) -> None:
        """
        gets model_name and brand_name from the user and 
        creates a model for given brand
        adds this model to brand's model list attribute
        param: 
        model_name: name of the model in str
        model_brand: brand of this model (brand class)


        """
        self.id = next(ShoeModel.id_iter) # here we increment the id by 1
        self.model_name = model_name 
        self.brand = model_brand
        model_brand.model_list.append(self)
        ShoeModel.shoe_model_db.append(self)
        

