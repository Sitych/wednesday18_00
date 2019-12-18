class Table:
    def __init__(self,long,width, hight):
        self.long = long
        self.width = width
        self.hight = hight
class KitchenTable(Table):
    def chet(self):  
        summ = ((self.long + self.width) * 2) // 50
        return(summ)
class DeskTable(Table):
    def plo(self):
        s = self.long * self.width
        return(s)
        
    


people = KitchenTable(3, 10, 8)
print(people.chet())
plochad = DeskTable(3, 10, 8)
print(plochad.plo())

        
