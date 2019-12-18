class Animal:

     def __init__(self, name):
          self.name = name

     def showinfo(self):
          print("I am " + self.name)

     def move(self):
          print("moving")

class Cat(Animal):

     def __init__(self, name, age, weight, pol ,typee):
          super().__init__(name)
          self.age = age
          self.weight = weight
          self.pol = pol
          self.typee = typee
          
     def move(self):
          print("moving cat")

     def print_all(self):
          print(self.name, self.age, self.weight, self.pol, self.typee)

Tom = Cat("Tom", 2, 50, "female", "jjvjnvcf")
Tom.move()
Tom.print_all()
Myrka = Cat("Myrka", 4, 100, "male", "adsfsadfa")
Myrka.print_all()
