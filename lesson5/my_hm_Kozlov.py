class Box:
    def __init__(self, hight, dlina, shirina):
        self.hight = hight
        self.dlina = dlina
        self.shirina = shirina

    def print_all(self):
     v = self.hight * self.shirina * self.dlina
     print(v)
     print(v//8)
kube = Box (15, 16, 6)
kube.print_all()
