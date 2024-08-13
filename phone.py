from item import Item

class Phone(Item):

    pay_rate = 0.7

    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
        #call the super function to have access to all the attributes/methods of the parent class
        super().__init__(name,price,quantity)
        #running the validations to the recieved arguments
        assert broken_phones>=0 ,f"broken phones {broken_phones} is not greater than zero!"

        #assign to the self object(instance attributes)
        self.broken_phones=broken_phones