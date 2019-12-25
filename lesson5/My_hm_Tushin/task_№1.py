class Box:
    def __init__(self, dl, vys, sh):
        self.dl = dl
        self.vys = vys
        self.sh = sh

    def print_all(self):
     v = self.dl * self.vys * self.sh
     print(v)
     print(v//8)
kub = Box (15, 16, 6)
kub.print_all()
