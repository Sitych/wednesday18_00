class Person:

     def __init__(self, name, age, rost):
          self.age = age
          self.name = name
          self.rost = rost

     def print_all(self):
          print(self.age, self.name, self.rost)

man = Person("Egor", 16, 182)
woman = Person("Masha", 36, 170)
man.print_all()
woman.print_all()
