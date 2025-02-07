#using oop create a class called cars that have the following attributes model, color , YOM implement constructor method
# and a method function that prints my fav car is ....., it is this in color..... and YOM IN ....years. Create 5 instances of that clas.

class car:
    def __init__(self, model,color, year):
        self.model = model
        self.color = color
        self.year = year
    def myfunction(self):
        print(f"My favourite car is  {self.model} and  I love the black color{self.color} Manfuctured in  {self.year}")

myobject = car(model="Audi", color = "blue", year = 2021)
myobject.myfunction()

myobject2 = car(model="Toureg", color = "red", year = 2024)
myobject2.myfunction()

myobject3 = car(model="Mercedes", color = "red", year = 2019)
myobject3.myfunction()

myobject4 = car(model="Golf", color = "red", year = 2022)
myobject4.myfunction()

myobject5 = car(model="Tiguan", color = "red", year = 2020)
myobject5.myfunction()






