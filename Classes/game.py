class Game:
    def __init__(self):
        self.grid = [[0] * 7 for i in range(6)]
        self.columns = 7
        self.rows = 6
        #directions -> diagonales, ligne, colonne
        self.pos = [(1, 0), (0, 1), (1, 1), (1, -1)]

    def fullGrid(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j] == 0:
                    return False
        return True
            
        return not 0 in self.grid
    
    def fullColumn(self, col):
        return self.grid[0][col] != 0

    def resetGrid(self):
        self.grid = [[0] * 7 for i in range(6)]

    def checkWin(self,x, y, dx, dy):
        player = self.grid[x][y]
        for i in range(3):
            x += dx
            y += dy
            if (not 0 <= x < 6 or not 0 <= y < 7) or self.grid[x][y] != player:
                return 0
        return player
    
    def win(self):
        for x in range(self.rows):
            for y in range(self.columns):
                if self.grid[x][y] != 0:
                    for dx,dy in self.pos:
                        player = self.checkWin(x, y, dx, dy)
                        if player != 0:
                            return player
        return 0
    
    def play(self, col, player):
        for i in range(1,self.rows):
            if self.grid[i][col] != 0:
                self.grid[i - 1][col] = player
                return True
            elif i == 5:
                self.grid[i][col] = player
                return True
        return False
    
    def freePos(self,x,y):
        return self.grid[x][y] == 0

    def display(self):
        for i in self.grid:
            print(i)
        
