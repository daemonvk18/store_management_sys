from item import Item

class Keyboard(Item):

    pay_rate = 0.9

    def __init__(self,name:str,price:float,quantity=0):
        #call the super function to have access to all the attributes/methods of the parent class
        super().__init__(name,price,quantity)