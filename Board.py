#Tic Tac Toe
import os
import time

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player = 1

Win = 1
Draw = -1
Running = 0
Stop = 1

Game = Running
Mark = 'X'

#This Function Draws Game Board
def DrawBoard():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))
    print(" ___|___|___")
    print("  %c | %c | %c " % (board[4],board[5],board[6]))
    print(" ___|___|___")
    print("  %c | %c | %c " % (board[7],board[8],board[9]))
    print("    |   |   ")

#filled or not
def CheckPosition(x):
    if(board[x] == ' '):
        return True
    else:
        return False

print("Player 1 [X] --- Player 2 [O]\n")
while(Game == Running):
    os.system('cls')
    DrawBoard()
    if(player % 2 != 0):
        print("Player 1 GO")
        Mark = 'X'
    else:
        print("Player 2 GO")
        Mark = 'O'
    choice = int(input("Enter number between [1-9] : "))
    if(CheckPosition(choice)):
        board[choice] = Mark
        player+=1

os.system('cls')
DrawBoard()
if(Game==Draw):
    print("Game Draw")
elif(Game==Win):
    player-=1
    if(player%2!=0):
        print("Player 1 Wins")
    else:
        print("Player 2 Wins")
