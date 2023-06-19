def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False            # Out-of-bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False            # O.o.b. column
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False            # Out-of-bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False            # O.o.b. column
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # A mismatch!
            return False
    return True                 # All offsets succeeded, so we return

def inabox(ch, row, col, A):
    """Starting from (row, col), will check if there is a 2x2 of ch
    east, south, and southeast of (row, col)
    """
    H = len(A)
    W = len(A[0])
    for row in range(H):
        for col in range(W):
            if inarow_Neast(ch, row, col, A, 2) == True and inarow_Nsouth(ch, row, col, A, 2) == True and inarow_Nsoutheast(ch, row, col, A, 2) == True:
                return True

def menu():
    """Prints the menu of options that the user can choose."""
    print()
    print("(0) Player vs Player mode") #done
    print("(1) Player vs AI mode") #done
    print("(2) AI vs AI mode")
    print("(9) Quit") #done
    print()

import random

class TicTacToe:
    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar,rowChar in moveString:
            col = int(colChar)
            row = int(rowChar)
            if 0 <= col <= self.width and 0<=row<=self.height:
                self.addMove(row,col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def __init__(self):
        """Construct objects of type Board, with the given width and height."""
        self.data = [[' ']*4 for row in range(4)]
        self.width = 4
        self.height = 4
    
    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # The string to return
        for row in range(0, self.height):
            s+=str(row)
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'
        s += " "
        s += (2*self.width + 1) * '-'   # Bottom of the board
        s+='\n'
        s+='  '
        for col in range(0,self.width):
            s+=str(col%10)
            s+=' '
        return s       # The board is complete; return it

    def addMove(self, r, c, player): 
        """
        adds character to board that user specifies
        """
        if self.data[r][c] == ' ':
            self.data[r][c] = player
    
    def delMove(self, r,c):
        """
        This method should do the opposite of addMove. It should remove the
        top checker from the column c. If the column is empty, then delMove
        should do nothing. 
        """
        self.data[r][c] = ' '
        return
    
    def clear(self):
        """clears board"""
        for r in range(len(self.data)):
            for c in range(len(self.data[0])):
                self.data[r][c]=' '

    def winsFor(self, player): 
        """This method's argument ox is a 1-character checker: either 'X' or 'O'.
            It should return True if there are four checkers of type ox in a 
            row on the board. It should return False otherwise
        """
    
        # Check to see if ox wins, starting from any checker:
        for row in range(self.height):
            for col in range(self.width):
                if inarow_Neast(player, row, col, self.data, 4) == True:
                    return True
                elif inarow_Nsouth(player, row, col, self.data, 4) == True:
                    return True
                elif inarow_Nsoutheast(player, row, col, self.data, 4) == True:
                    return True
                elif inarow_Nnortheast(player, row, col, self.data, 4) == True:
                    return True 
        if self.data[3][0] == player and self.data[3][3] == player and self.data[0][3] == player and self.data[0][0] == player:
            return True
        if inabox(player, row, col, self.data) == True:
            return True
    
    def spacesToWin(self, player):
        """spacesToWin returns a list of spaces that player can move to win in the next turn
        """
        w = self.width
        h = self.height
        L = []
        for row in range(h):
            for col in range(w):
                if self.allowsMove(row,col) == True:
                    self.addMove(row,col, player)
                    if self.winsFor(player) == True:
                        L += [(row, col)]
                    self.delMove(row, col)
        return L
        

        # but, if it looks at EACH row and col and never finds a win...
    
    def allowsMove(self,r,c):
        """Checks if the move is within the range in the board and not in a spot that is taken.
        """
        if c not in range(self.height) or r not in range(self.width):
            return False
        if self.data[r][c] != " ":
            return False
        return True

    def isFull(self):
        """Checks if the board is full, returns boolean.
        """
        t=[]
        for r in range(self.height):
            for c in range(self.width):
                t+=[self.allowsMove(r,c)]
        if sum(t) == 0: return True
        return False

    def clear(self):
        """clears board"""
        for r in range(len(self.data)):
            for c in range(len(self.data[0])):
                self.data[r][c]=' '

    def aiMove(self, player):
        """aiMove returns a random move.
        """
        r = -1
        c = -1
        while self.allowsMove(r, c) == False:
            r = random.choice(range(0,4))
            c = random.choice(range(0,4))
        return r,c

    def ai2Move(self, player):
        """aiMove returns the move that allows player to win, or that stops the opponent from winning.
        Otherwise it returns a random move.
        """
        L = self.posToWin(player)
        if self.posToWin(player) != []:
            return L
        if player == "O":
            other = "X" 
        elif player == "X":
            other = "O"
        P = self.posToWin(other)
        if self.posToWin(other):
            return P
        w = self.width
        h = self.height
        col = -1
        row = -1
        while self.allowsMove(row, col) == False: 
            col = random.choice(range(w))
            row = random.choice(range(h))
        
        return [(row,col)]
    
    def posToWin(self,ox):
        """
        This method should be within the Board class and should take one
        argument, ox, which will be either the string 'X' or the string 'O'
        (the two possible checkers in the game). It returns the list of possible wins for the inputted ox.
        """
        rL = []
        
        for col in range(self.width):
            for row in range(self.height):
                if self.allowsMove(row,col) == True:
                    self.addMove(row,col,ox)
                    if self.winsFor(ox) == True:
                        rL += [(row,col)]
                    self.delMove(row,col)
    
        return rL
        
    def deleteMove(self,r,c):
        """Deletes the move at specified row and column.
        """
        self.data[r][c] = " "
        return

    def hostGame(self):
        """
        This method brings everything together into the familiar game.
        It should host a game of Connect Four
        """
        self.clear()
        print("Welcome to Tic Tac Toe!")
        print("\n")
        print(self)
        while not(self.winsFor("X")) and not(self.winsFor("O")) and not(self.isFull()):
            users_col = -1    # Note! This -1 is _intentionally_ not valid!
            users_row = -1
            while self.allowsMove(users_row,users_col) == False:  # _while_ not valid
                try:
                    users_row = int(input("Choose a row: "))  # ask for a column
                except ValueError:
                    print("Please enter a valid row 0-3")
                try:
                    users_col = int(input("Choose a column: "))  # ask for a column
                except ValueError:
                    print("Please enter a valid column 0-3")
            self.addMove(users_row,users_col,"X")
            print(self)
            if self.winsFor("X"):
                print("X Wins!!!")
                x = 1
                o = 0
                return x,o
            
            
            users_col2 = -1    # Note! This -1 is _intentionally_ not valid!
            users_row2 = -1
            while self.allowsMove(users_row2,users_col2) == False:  # _while_ not valid
                try:
                    users_row2 = int(input("Choose a row: "))  # ask for a column
                except ValueError:
                    print("Please enter a valid row 0-3")
                try:
                    users_col2 = int(input("Choose a column: "))  # ask for a column
                except ValueError:
                    print("Please enter a valid column 0-3")
            self.addMove(users_row2,users_col2,"O")
            print(self)
            if self.winsFor("O"):
                print("O Wins!!!")
                x = 0
                o = 1
                return x,o
                break
        if self.isFull() == True:
            print("It's a tie!")

    def hostAIAIGame(self):
        self.clear()
        print("Welcome to Tic Tac Toe!")
        print("\n")
        print(self)
        while not(self.winsFor("X")) and not(self.winsFor("X")) and not(self.isFull()):

            rL = self.ai2Move("X")
            r,c= rL[0][0], rL[0][1]
            self.addMove(r,c,"X")
            print(self)
            if self.winsFor("X"):
                print("X Wins!!!")
                x = 1
                o = 0
                return x,o
                break

            rL2 = self.ai2Move("O")
            r,c= rL2[0][0], rL2[0][1]
            self.addMove(r,c,"O"); print("336")
            print(self)
            if self.winsFor("O"):
                print("O Wins!!!")
                x = 0
                o = 1
                return x,o
                break
        if self.isFull() == True:
            print("It's a tie!")

    def hostAIGame(self):
        """
        hostAIGame hosts a game that alternates between player inputting moves and an AI randomly playing against them that tries to win if it can win in one move, or blocks the opponent if they can win in the next move.
        """
        self.clear()
        print("Welcome to Tic Tac Toe!")
        print("\n")
        print(self)
        while not(self.winsFor("X")) and not(self.winsFor("O")) and not(self.isFull()):
            users_col = -1    # Note! This -1 is _intentionally_ not valid!
            users_row = -1
            while self.allowsMove(users_row,users_col) == False:  # _while_ not valid
                try:
                    users_row = int(input("Choose a row: "))  # ask for a column
                except ValueError:
                    print("Please enter a valid row 0-3")
                try:
                    users_col = int(input("Choose a column: "))  # ask for a column
                except ValueError:
                    print("Please enter a valid column 0-3")
            self.addMove(users_row,users_col,"X")
            print(self)
            if self.winsFor("X"):
                print("X Wins!!!")
                x = 1
                o = 0
                return x,o
            
            users_col2 = -1    # Note! This -1 is _intentionally_ not valid!
            users_row2 = -1
            # while self.allowsMove(users_row2,users_col2) == False:  # _while_ not valid
            #     users_row2 = int(input("Choose a row: "))  # ask for a column
            #     users_col2 = int(input("Choose a column: "))  # ask for a column
            # self.addMove(users_row2,users_col2,"O")
            # print(self)
            # if self.winsFor("O"):
            #     print("O Wins!!!")
            #     break
            rL = self.ai2Move("O")
            r,c= rL[0][0], rL[0][1]
            self.addMove(r,c,"O")
            print(self)
            if self.winsFor("O"):
                print("O Wins!!!")
                x = 0
                o = 1
                return x,o
                break
        if self.isFull() == True:
            print("It's a tie!")
    
    
def main():
    x = 0
    o = 0
    while True:
        menu()
        choice = int(input("Choose your mode: "))

        if choice == 0:
            ttt = TicTacToe() 
            w,y = ttt.hostGame()
            x += w
            o += y
            print("X has won ", x, "times")
            print("O has won ", o, "times")

        if choice == 1:
            ttt = TicTacToe()
            w, y = ttt.hostAIGame()
            x += w
            o += y
            print("X has won ", x, "times")
            print("O has won ", o, "times")


        if choice == 2:
            ttt = TicTacToe()
            w, y = ttt.hostAIAIGame()
            x += w
            o += y
            print("X has won ", x, "times")
            print("O has won ", o, "times")


        if choice == 9:
            break


# print("To play against another player type ttt.hostGame()")
# print("To play against an AI type ttt.hostAIGame()")
main()
# print("To play an AI against an AI type ttt.hostAIAIGame()")