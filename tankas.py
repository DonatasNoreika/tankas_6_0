
import random

class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = "Šiaurė"
        self.suviai = {"Šiaurė": 0, "Pietūs": 0, "Vakarai": 0, "Rytai": 0}
        self.prieso_x = random.randint(-10, 10)
        self.prieso_y = random.randint(-10, 10)
        self.nusauta = 0
        self.taskai = 100

    def pirmyn(self):
        self.y += + 1
        self.kryptis = "Šiaurė"
        self.taskai -= 10

    def atgal(self):
        self.y -= 1
        self.kryptis = "Pietūs"
        self.taskai -= 10

    def kairen(self):
        self.x -= 1
        self.kryptis = "Vakarai"
        self.taskai -= 10

    def desinen(self):
        self.x += 1
        self.kryptis = "Rytai"
        self.taskai -= 10

    def sauti(self):
        self.suviai[self.kryptis] += 1
        if self.ar_pataike():
            print("Pataikei!")
            self.nusauta += 1
            self.taskai += 50
            self.prieso_x = random.randint(-10, 10)
            self.prieso_y = random.randint(-10, 10)
        else:
            print("Nepataikei :(")

    def ar_pataike(self):
        if self.x == self.prieso_x and self.kryptis == "Šiaurė" and self.prieso_y > self.y:
            return True
        if self.x == self.prieso_x and self.kryptis == "Pietūs" and self.prieso_y < self.y:
            return True
        if self.y == self.prieso_y and self.kryptis == "Vakarai" and self.prieso_x < self.x:
            return True
        if self.y == self.prieso_y and self.kryptis == "Rytai" and self.prieso_x > self.x:
            return True
        return False

    def rodyti_musio_lauka(self):
        for y in range(10, -11, -1):
            for x in range(-10, 11):
                if x == self.x and y == self.y:
                    print("X ", end="")
                elif x == self.prieso_x and y == self.prieso_y:
                    print("O ", end="")
                elif x == 0 or y == 0:
                    print("| ", end="")
                else:
                    print("_ ", end="")
            print()


    def info(self):
        print(f"Tankas: x: {self.x}, y: {self.y}, kryptis: {self.kryptis}")
        print(f"Priešas x: {self.prieso_x}, y: {self.prieso_y}")
        print(f"Šūviai: {self.suviai}, bendrai: {sum(self.suviai.values())}")
        print(f"Nušauta: {self.nusauta}, taškai: {self.taskai}")
