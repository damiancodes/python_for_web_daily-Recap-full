#object oriented programming

class person:
    def __init__(self, name, age):
        #this is a constructor method
        #it takes two parameter an initialize as attributes
        self.name = name
        self.age = age

    def myfunction(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")
        #this is a method function
#create an object or an instance of a class.
myobject= person("John", 36)
myobject.myfunction()
myobject2 = person("Mary", 10)
myobject2.myfunction()
myobject3 = person("Erick", 30)
myobject3.myfunction()
myobject4 = person("Mike", 16)
myobject4.myfunction()