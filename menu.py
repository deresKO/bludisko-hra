from generovanie import Generuje
from ovladanie import Ovladanie
import os
from colorama import init, Back, Style

class Menu():
    def __init__(self):
        init()
        self.startovanie()

    def startovanie(self):
        init()
        self.velkost = self.osetrenie()
        if self.velkost is not None and self.velkost % 2 != 0 and 5 <= self.velkost <= 25:
            generuje = Generuje(self.velkost,self.velkost).logika()
            s = Ovladanie(generuje,self.velkost)
            hodnota = s.ovladanie()
            if hodnota == True:
                os.system('cls' if os.name == 'nt' else 'clear')
                hra = Menu()
                hra.startovanie()
        else:
            for _ in range(3):
                os.system('cls' if os.name == 'nt' else 'clear')
            self.startovanie()
        print(Ovladanie.reset())

    def osetrenie(self):
        print("--------------------------------------------------------------------")
        print("-----------------------Vitajte v hre BLUDISKO-----------------------")
        print("--------------------------------------------------------------------")
        print("-----------------------------Vysvetlenie----------------------------")
        print("--------------------------------------------------------------------")
        print("------------------Farba: " + Back.CYAN + "  " + Style.RESET_ALL + " -------Steny v bludisku-----------------")
        print("------------------Farba: " + Back.WHITE+ "  " + Style.RESET_ALL + " -------Cesta v bludisku-----------------")
        print("------------------Farba: " + Back.YELLOW+ "  " + Style.RESET_ALL + " -------------Hrac-----------------------")
        print("------------------Farba: " + Back.RED+ "  " + Style.RESET_ALL + " --------Ciel bludiska-------------------")
        print("-------------------Tlacidlo R resetujete bludisko-------------------")
        print("------------------Tlacidlo ESC resetujete bludisko------------------")
        print("--V bludisku sa pohybujete pomocou tlacidiel W,A,S,D alebo sipkami--")
        print("--------------------------------------------------------------------")
        cislo = input("-------Zadajte velkost bludiska (od 5 do 25 ale len neparne cisla) :")
        print("--------------------------------------------------------------------")
        print("------------Pre zobrazenie bludiska musite stlacit ENTER------------")
        if cislo.isdigit():
            if 5 <= int(cislo) <= 25 and int(cislo) % 2 != 0:
                return int(cislo)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.osetrenie()
