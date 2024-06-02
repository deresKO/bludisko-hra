import keyboard
from obraz import Obraz
import time
import os

class Ovladanie():
    def __init__(self,tvar,velkost):

        self.tvar = tvar
        self.velkost = velkost
        self.hodnota = True
    def ovladanie(self):
        c = True

        while True:
            key = keyboard.read_key()
            if key == "enter" and c == True:
                Obraz(self.tvar).bludisko()
                c = False
                time.sleep(0.5)
            if self.hodnota == True:
                if key == "w" or key == "up":
                    Obraz(self.tvar).clear_lines(self.velkost)
                    self.posun(-1,0)
                    Obraz(self.tvar).bludisko()
                    time.sleep(0.3)
                                
                if key == "s" or key == "down":
                    Obraz(self.tvar).clear_lines(self.velkost)
                    self.posun(1,0)
                    Obraz(self.tvar).bludisko()
                    time.sleep(0.3) 

                if key == "d"or key == "right":
                    Obraz(self.tvar).clear_lines(self.velkost)
                    self.posun(0,1)
                    Obraz(self.tvar).bludisko()
                    time.sleep(0.3)

                if key == "a"or key == "left":
                    Obraz(self.tvar).clear_lines(self.velkost)
                    self.posun(0,-1)
                    Obraz(self.tvar).bludisko()
                    time.sleep(0.3)
                
            if key == "r" : 
                print("reset")
                return True
            elif key == "esc":
                os._exit(0)

    def hlada(self):
        for i in range(len(self.tvar)):
            for j in range(len(self.tvar[i])):
                if self.tvar[i][j] == 2:
                    self.hrac_x = i
                    self.hrac_y = j
                if self.tvar[i][j] == 3:
                    self.ciel_x = i
                    self.ciel_y = j
    def vypis(self):
        print("--------------------------------------------------------------------")
        print("-------------------------Gratulujeme k vyhre------------------------")
        print("--------------------------------------------------------------------")
        self.hodnota = False
    def posun(self,x,y):
        self.hlada()
        if x == 1 and y == 0:
            if self.tvar[self.hrac_x+1][self.hrac_y] == 0:
                self.tvar[self.hrac_x][self.hrac_y] = 0
                self.tvar[self.hrac_x+1][self.hrac_y] = 2
            elif self.tvar[self.hrac_x+1][self.hrac_y] == 3:
                self.tvar[self.hrac_x][self.hrac_y] = 0
                self.tvar[self.hrac_x+1][self.hrac_y] = 2
                self.vypis()
        if x == -1 and y == 0:
            if self.tvar[self.hrac_x-1][self.hrac_y] == 0:
                self.tvar[self.hrac_x][self.hrac_y] = 0
                self.tvar[self.hrac_x-1][self.hrac_y] = 2
            elif self.tvar[self.hrac_x-1][self.hrac_y] == 3:
                self.tvar[self.hrac_x][self.hrac_y] = 0
                self.tvar[self.hrac_x-1][self.hrac_y] = 2
                self.vypis()

        if x == 0 and y == 1:
            if self.tvar[self.hrac_x][self.hrac_y+1] == 0:
                self.tvar[self.hrac_x][self.hrac_y] = 0
                self.tvar[self.hrac_x][self.hrac_y+1] = 2
            elif self.tvar[self.hrac_x][self.hrac_y+1] == 3:
                self.tvar[self.hrac_x][self.hrac_y] = 0
                self.tvar[self.hrac_x][self.hrac_y+1] = 2
                self.vypis()

        if x == 0 and y == -1:
            if self.tvar[self.hrac_x][self.hrac_y-1] == 0:
                self.tvar[self.hrac_x][self.hrac_y] = 0
                self.tvar[self.hrac_x][self.hrac_y-1] = 2
            elif self.tvar[self.hrac_x][self.hrac_y-1] == 3:
                self.tvar[self.hrac_x][self.hrac_y] = 0
                self.tvar[self.hrac_x][self.hrac_y-1] = 2
                self.vypis()
    def reset(self):
        return False