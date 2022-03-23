"""class to define the game"""
class Game:
    """init a game"""
    def __init__(self):
        self.grid = [[0] * 7 for i in range(6)]
        self.columns = 7
        self.rows = 6
        #directions -> diagonales, ligne, colonne
        self.pos = [(1, 0), (0, 1), (1, 1), (1, -1)]
        self.last_pawn = []

    def full_grid(self):
        """return boolean for fullgrid or not"""
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j] == 0:
                    return False
        return True

    def full_column(self, col):
        """return boolean for full col or not"""
        return self.grid[0][col] != 0

    def reset_grid(self):
        """reset the array of the game"""
        self.grid = [[0] * 7 for i in range(6)]

    def check_win(self,i, j, direction_i, direction_j):
        """return true if won on this pos"""
        player = self.grid[i][j]
        for k in range(3):
            i += direction_i + k - k
            j += direction_j
            if (not 0 <= i < 6 or not 0 <= j < 7) or self.grid[i][j] != player:
                return 0
        return player

    def win(self):
        """check each pos of the array"""
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j] != 0:
                    for direction_i,direction_j in self.pos:
                        player = self.check_win(i, j, direction_i, direction_j)
                        if player != 0:
                            return player
        return 0

    def play(self, col, player):
        """place a pawn in the"""
        for i in range(1,self.rows):
            if self.grid[i][col] != 0:
                self.grid[i - 1][col] = player
                self.last_pawn.append((i-1,col))
                return i - 1
            if i == 5:
                self.grid[i][col] = player
                self.last_pawn.append((i, col))
                return i
        return False

    def remove_last_pawn(self):
        """remove the last pawn played"""
        i,j = self.last_pawn[len(self.last_pawn)-1]
        self.grid[i][j] = 0
        self.last_pawn = self.last_pawn[0:len(self.last_pawn)-1]

    def free_pos(self,i,j):
        """check if the pos is free"""
        return self.grid[i][j] == 0

    def display(self):
        """display the array in terminal"""
        for i in self.grid:
            print(i)

    def is_empty(self):
        """check if array is empty"""
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j] != 0:
                    return False
        return True