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



class persona:
     def __init__(self, indian, African,European):
        self.indian = indian
        self.African = African
        self.European = European
     def myfunction(self):
        print(f"He is {self.indian} and this is an {self.African} while {self.European}")


mypersona1 = persona(indian="omar", European="Maya", African="Omosh")
mypersona1.myfunction()


class software_engineer:
      def __init__(self, PHP,PYTHON,JAVA,JS):
          self.PHP = PHP
          self.PYTHON = PYTHON
          self.JAVA = JAVA
          self.JS = JS

      def myfunction(self):
          print(f"We learn {self.PHP}  on monday {self.PYTHON} on tuesday  {self.JAVA} and on wednesday we learn {self.JS}")

mysoftware= software_engineer(PHP="syntax" , PYTHON="functions" , JAVA="Modules", JS="parametes")
mysoftware.myfunction()


