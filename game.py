"""class to define the game"""
import random
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
        try:
            return self.grid[0][col] != 0
        except IndexError:
            return False

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

    def play_ai(self, player):
        """play the game with the computer"""
        best = -2
        best_col = 0
        for i in range(self.columns):
            if self.full_column(i):
                continue
            self.play(i, 1)
            if self.win() == 1:
                self.remove_last_pawn()
                return i
            self.remove_last_pawn()
            self.play(i, player)
            score = self.minmax(2, -player, -2, 2)
            self.remove_last_pawn()
            if score > best:
                best = score
                best_col = i
        if self.last_pawn[len(self.last_pawn)-1][0] == 5:
            return random.randint(0,6)
        return best_col
    #minmax algorithm for the AI to play the game with the computer (not finished)
    def minmax(self, depth, player, alpha, beta):
        """minmax algorithm"""
        if depth == 0 or self.win() != 0:
            return self.win()
        if player == 1:
            best = -2
            for i in range(self.columns):
                if self.full_column(i):
                    continue
                self.play(i, player)
                best = max(best, self.minmax(depth - 1, -player, alpha, beta))
                self.remove_last_pawn()
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
            return best
        best = 2
        for i in range(self.columns):
            if self.full_column(i):
                continue
            self.play(i, player)
            best = min(best, self.minmax(depth - 1, -player, alpha, beta))
            self.remove_last_pawn()
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
