
class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = "Šiaurė"
        self.suviai = {"Šiaurė": 0, "Pietūs": 0, "Vakarai": 0, "Rytai": 0}

    def pirmyn(self):
        self.y += + 1
        self.kryptis = "Šiaurė"

    def atgal(self):
        self.y -= 1
        self.kryptis = "Pietūs"

    def kairen(self):
        self.x -= 1
        self.kryptis = "Vakarai"

    def desinen(self):
        self.x += 1
        self.kryptis = "Rytai"

    def sauti(self):
        self.suviai[self.kryptis] += 1

    def info(self):
        print(f"x: {self.x}, y: {self.y}, kryptis: {self.kryptis}")
        print(f"Šūviai: {self.suviai}, bendrai: {sum(self.suviai.values())}")
