import csv

class Item:

    #calss attributes(can be accessed from the instance level as well)
    pay_rate = 0.8 #20% discount
    all_items = [] #all items that are added to the store should be added to this list

    def __init__(self,name:str,price:float,quantity=0):
        #running the validations to the recieved arguments
        assert price >=0, f"price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"quantity {quantity} is not greater than or equal to zero!"

        #assign to the self object(instance attributes)
        #here adding __ infornt of the name indicates that it cannot be accessed using __ ,directly use name
        self.__name = name
        self.__price = price
        self.quantity = quantity

        #we need to add the item to the list
        Item.all_items.append(self) #here we are not just appending the name here we are appending the entire instance 


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if value>0:self.__price=value
        else:raise Exception("the value you entered is negative")    


    @property
    #property=read-only attribute
    def name(self):
        return self.__name
    
    #setter method to change the name
    @name.setter
    def name(self,name):
        if len(name)>10:raise Exception("The length pf the name is too long")
        else:
           self.__name=name

    def calculated_total(self):
        return self.__price * self.quantity
    
    def discount_on_item(self):
        self.__price = self.__price * self.pay_rate# if here if it is Item.pay_rate then it would be alwasy using same pay_rate

    #we will add a decorater to convert the behaivour of the function
    @classmethod    
    def instantiate_from_csv(cls):#class method ,here the class object itself is accepted as a parameter(cls)
        with open("items.csv",'+r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
        #loading the items 
        for item in items:
            #instantiating the objects form the csv file
            Item(name=item.get('name'),price=float(item.get('price')),quantity=int(item.get('quantity')))

    #static method
    @staticmethod
    def is_integer(num):#it doesnot recieve object as a first and automatic param as class methods 
        #we will count out the floats that are point zero
        if isinstance(num,float):
            #count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
    
    #here the connect_to_server,prepare_body are private methods(abstarction)
    #to private a method it is accessable by adding __ infront of the method
    
    def __connect_to_server(self,smtp_server):
        return f"connecting to {smtp_server}"
    
    def __prepare_body(self):
        return f'''
         hello shaun
         we have {self.__name} {self.quantity} times
         regards , preetham 
         '''
    def send_email(self):
        self.__connect_to_server("smtp")
        self.__prepare_body()
  