import sys
from colorama import init, Back,Style

class Obraz():
    def __init__(self,tvar):
        self.tvar = tvar
    def bludisko(self):
        init()
        for i in range(len(self.tvar)):
            for j in range(len(self.tvar[1])):
                if self.tvar[i][j] == 1:
                        
                    sys.stdout.write(Back.CYAN + "  ")
                if self.tvar[i][j] == 0:
                        
                    sys.stdout.write(Back.WHITE + "  ")
                if self.tvar[i][j] == 2:
                        
                    sys.stdout.write(Back.YELLOW + "  ")
                        
                if self.tvar[i][j] == 3:
                        
                    sys.stdout.write(Back.RED + "  ")
            print("" + Style.RESET_ALL)
    def vymaz(self,n):
        for i in range(n):
        # Presunutie kurzora na začiatok predchádzajúceho riadku
            sys.stdout.write(Style.RESET_ALL + '\033[F')
        # Vymazanie riadku
            sys.stdout.write(Style.RESET_ALL +'\033[K')

        