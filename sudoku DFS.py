import numpy as np

filename = "input.txt"

f = open(filename, "r")
grid = f.readlines()

board = np.zeros((9, 9)).astype(int)

for i in range(9):
    for j in range(9):
        board[i, j] = int(grid[i][j])


class Sudoku:

    def __init__(self, b):
        self.board = b.copy()
        self.p = np.zeros((9, 9, 9)).astype(int)

    def show(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("—————————————————————")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                print(self.board[i, j], end=" ")
            print()
        print()
    
    def setP(self):
        for i in range(9):
            for j in range(9):
                self.p[i, j] = np.arange(1, 10)
                
        for i in range(9):
            for j in range(9):
                if self.board[i, j] == 0:
                    for x in range(1, 10):
                        if x in self.board[i, :]:
                            self.p[i, j, x - 1] = 0

                        if x in self.board[:, j]:
                            self.p[i, j, x - 1] = 0

                        if x in self.board[(i // 3) * 3 : 3 * (i // 3) + 3,
                                           (j // 3) * 3 : 3 * (j // 3) + 3]:
                            self.p[i, j, x - 1] = 0

                else:
                    self.p[i, j] = 0

    def prob(self):
        
        self.setP()

        changed = True
        while changed:
            
            changed = False
            
            for i in range(9):
                for j in range(9):
                    
                    a = list(self.p[i, j])
                    while 0 in a:
                        a.remove(0)

                    if len(a) == 1:
                        self.board[i, j] = a[0]
                        self.setP()
                        changed = True

                    for x in self.p[i, j]:
                        if x != 0:
                            if x == self.p[i, :, x - 1].sum():
                                self.board[i, j] = x
                                self.setP()
                                changed = True

                            if x == self.p[:, j, x - 1].sum():
                                self.board[i, j] = x
                                self.setP()
                                changed = True

                            if x == self.p[(i // 3) * 3 : 3 * (i // 3) + 3,
                                           (j // 3) * 3 : 3 * (j // 3) + 3, x - 1].sum():
                                self.board[i, j] = x
                                self.setP()
                                changed = True

        if 0 in self.board:
            for i in range(9):
                for j in range(9):
                    moves = list(self.p[i, j].astype(int))
                    while 0 in moves:
                        moves.remove(0)
                    if len(moves) > 1:
                        break
                if len(moves) > 1:
                        break

            for move in moves:
                self.board[i, j] = move
                new_s = Sudoku(self.board)
                output = new_s.prob()
                if output[0]:
                    return output
                if 0 not in new_s.board:
                    return True, new_s

                self.board[i, j] = 0
                    
        return False, self


s = Sudoku(np.array(board).reshape(9, 9))
s = s.prob()[1]
s.show()