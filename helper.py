#when to use a class method and when to use a static method?
#static emthod is used when want to do something that should not be unique per instance
#in other words static nethod should do something that has a relationship with the class ,but not something that must be unique per instance

#CLASS METHOD
#the reason to create a class method is for instantiating instances from some structured data that we have.
class Item:

    @staticmethod
    def is_integer():
        pass
    #here the is_integer function has nothing to do with the instances od the item class

    @classmethod
    def read_from_csv():
        pass
    #here this class method is used to read and instantiate data from a particular csv file


#DIFFERENCE BETWEEN STATIC METHOD AND CLASS METHOD
# the static methods are not passing the object reference as the first argument in the background,and class method does that.
# the class method ,staic methods can be called from both class ,instance level .    