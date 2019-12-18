class Animal:

     def __init__(self, name):
          self.name = name

     def showinfo(self):
          print("I am " + self.name)

     def move(self):
          print("moving")

class Mouse(Animal):

     def __init__(self, name, age, wight):
          super().__init__(name)
          self.age = age
          self.wight = wight

     def move(self):
          print("moving mouse")
     
Cat = Animal("Myrka")
Cat.move()
Cat.showinfo()
jerry = Mouse("Jerry", 2, 50)
print(jerry.move())
