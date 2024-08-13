from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Item("myitem",1000)
item2 = Keyboard('jsvkeyboard',1000,1)
item3 = Phone("iphone14",1000,1)
#settinga an attribute
item1.name = 'Otheritem'

#getting an attribute
print(item1.name)

#checking the working of discount function
item1.discount_on_item()
print(item1.price)
item2.discount_on_item()
print(item2.price)
item3.discount_on_item()
print(item3.price)




 #four pillars of the object oriented programming
 #encapsulation-mechanism of restricting the direct access to some of our attributes in a program(using getters and setters)
 #abstraction-that only shows the neccessary attributes and hides the unnecessary information from the instances
 #inheritance-mechanism that helps us io reuse the code across our classes(child class,parent class etc.,)
 #polymorphism-it refers to use of a single type entity to represent different types in different scenarios
 #example of polymorphism
name = 'Jim'
print(len(name))
random_list= ["random","list"]
print(len(random_list))
#that's polymorphism in action,a single function does now
#how to handle different kinds of objects as expected