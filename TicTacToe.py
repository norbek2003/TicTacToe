from os import system, name
from copy import deepcopy
from colorama import Fore, Style, init
class Player:
    def __init__(self,sign,name):
        self.name=name
        self.winner=False
        self.sign=sign
class Grid:    
    def __init__(self):
        self.grid=[["[ ]", "[A]","[B]","[C]"]]
        for i in range(1,4):
            self.grid.append(["["+str(i)+"]","[ ]","[ ]", "[ ]"])

    def printGrid(self):
        for i in self.grid:
            print colorRow(i)
    def hit(self,spot,sign):
        coordinates=self.grid[int(spot[1:])][self.grid[0].index("["+str(spot[0]).upper()+"]")]  
        if coordinates=="[ ]":
            self.grid[int(spot[1:])][self.grid[0].index("["+str(spot[0]).upper()+"]")]="["+sign+"]"
        else:
            raise ValueError
def checkBoardForWin(board,player):
    wins=[["a1","a2","a3"],["b1","b2","b3"],["c1","c2","c3"],["a1","b1","c1"],["a2","b2","c2"],["a3","b3","c3"],["a1","b2","c3"],["a3","b2","c1"]]
    for i in wins:
        spot1=board.grid[int(i[0][1:])][board.grid[0].index("["+str(i[0][0]).upper()+"]")]
        spot2=board.grid[int(i[1][1:])][board.grid[0].index("["+str(i[1][0]).upper()+"]")]
        spot3=board.grid[int(i[2][1:])][board.grid[0].index("["+str(i[2][0]).upper()+"]")]
        if(spot1==spot2==spot3!="[ ]"):
            player.winner=True
            break
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def colorRow(row):
    colorRowList=[]
    for i in row:
        if(i=="x"):
            colorRowList.append(Fore.RED+i+Fore.RESET)
        elif(i=="o"):
            colorRowList.append(Fore.BLUE+i+Fore.RESET)
        else:
            colorRowList.append(Fore.WHITE+i+Fore.RESET)
    return " ".join(colorRowList)
def main():
    board=Grid()
    if name == 'nt':
        init()
    player1=Player("x",raw_input("Please enter your name Player 1!\n->"))
    player2=Player("o",raw_input("Please enter your name Player 2!\n->"))
    board.printGrid()
    while ((player1.winner==False)and(player2.winner==False)):
        takeTurn(player1,board)
        if (player1.winner ==False):
            takeTurn(player2,board)
    if (player1.winner==True):
        print "Congratulations ",player1.name,"!\n You win!"
    else:
        print "Congratulations ",player2.name,"!\n You win!"
    endGame=raw_input("Please press any key to end game!\n->")    
    
def takeTurn(playerA,board):
    clear()
    while True:
        try:
            board.printGrid()
            print " Your turn ",playerA.name           
            board.hit(raw_input("Please input a point!\n(*Example: B2*)\n->"), playerA.sign)
            checkBoardForWin(board, playerA)
        except ValueError:
            clear()
            continue
        else:
            break
    
    clear()

    clear()
main()
