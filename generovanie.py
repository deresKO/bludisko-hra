import random

class Generuje():
    def __init__(self, sirka, vyska):
        self.sirka = sirka
        self.vyska = vyska
        self.bludisko = self.logika()

    def logika(self):
        bludisko = [[1 for i in range(self.sirka)] for j in range(self.vyska)]

        hrac_x = 1
        hrac_y = 1
        bludisko[hrac_x][hrac_y] = 0

        def neplatny_tah(x, y):
            return 1 <= x < self.sirka - 1 and 1 <= y < self.vyska - 1 and bludisko[y][x] == 1

        
        smer= [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def vzhlad(x, y):
            random.shuffle(smer)
            for dx, dy in smer:
                nx, ny = x + 2*dx, y + 2*dy
                if neplatny_tah(nx, ny):
                    bludisko[ny][nx] = 0
                    bludisko[y + dy][x + dx] = 0
                    vzhlad(nx, ny)

        vzhlad(hrac_x, hrac_y)

        bludisko[hrac_x][hrac_y] = 2
        bludisko[self.vyska - 2][self.sirka - 2] = 3

        return bludisko
