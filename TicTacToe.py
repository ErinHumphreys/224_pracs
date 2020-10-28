#Tic Tac Toe
#Importing
import os
import sys
import time
import random

menu = True
vs_player = False
vs_computer = False

#Define the board:
#Using a List to define the Grid of the TIC TAC TOE game. To keep track of the positions
grid = [" "," "," "," "," "," "," "," "," "]
## Layout of the TIC TAC TOE BOARD and its positions
##       7|8|9
##       4|5|6
##       1|2|3
## The TIC TAC TOE BOARD will be in the following formation shown above

#Print the TIC TAC TOE  board:
def p_grid():
    print (grid[6],'|' ,grid[7], '|' ,grid[8])
    print ('-----------')
    print (grid[3], '|' ,grid[4], '|' ,grid[5])
    print ('----------')
    print (grid[0], '|' ,grid[1], '|' ,grid[2])

#Defining the format of the grid that the user of the program will see
def gformat():
    os.system("CLS")
    print("  7|8|9  " )
    print("  4|5|6  " )
    print("  1|2|3  " )
    print("The TIC TAC TOE BOARD ")
    print("Number of times Player X has won: ",x_count,"     Number of times Player 0 has won:",o_count)
    p_grid()

##Function to exit the game.
def quite(string):
    if (string == "q") or (string == "Q") :
        return True
    else:
        return False
##Function used to clear the grid List of its contents by overriding the contents with empty spaces
def to_clean():
    for x in range(0,9):
        grid[x] = " "

##Function defined to test whether the users input is within range
def is_inrange(num):
    if (num in range(1,10)) or (quite(num) == True)  :
        return True
    else:
        return False
##Function defined to check for a winner following the winning criteria or sequence
def isWinner_check(player, pgrid):
    if (pgrid[0] == player and pgrid[1] == player and pgrid[2] == player) or \
       (pgrid[3] == player and pgrid[4] == player and pgrid[5] == player) or \
       (pgrid[6] == player and pgrid[7] == player and pgrid[8] == player) or \
       (pgrid[0] == player and pgrid[3] == player and pgrid[6] == player) or \
       (pgrid[1] == player and pgrid[4] == player and pgrid[7] == player) or \
       (pgrid[2] == player and pgrid[5] == player and pgrid[8] == player) or \
       (pgrid[0] == player and pgrid[4] == player and pgrid[8] == player) or \
       (pgrid[2] == player and pgrid[4] == player and pgrid[6] == player):
        return True
    else:
        return False
##Function defined to determine whether the tic tac toe grid is full or not
def isGrid_full(grid):
    if " " in grid:
        return False
    else:
        return True
##Function defined to move back from the game to the 'menu'
def back(indicate):
    if (indicate == "B") or (indicate == "b"):
        return True
    else:
        return False
##Artificial Intelligence for the computers move against the user
def com_move(player,grid):
    for num in range(0,9):
        if grid[num] == " ":
            grid[num] = player
            if isWinner_check(player, grid):
                return num
            else:
                grid[num] = " "
## This checks the middle block of the grid to see whether its open and then if it is places the computers move there.
    if grid[4] == " ":
        return 4
    while True:
        move = random.randint(0,9)
        if grid[move] == " ":
            return move
            break
    return 4

##Main Loop
while menu:
    x_count = 0
    o_count = 0

    os.system("CLS")
    print("-------------------MENU-------------------")
    print("Welcome to TIC TAC TOE, would your like to play against another player or against the computer?")
    user_option = input(print("Enter, 'P' to play against a player and Enter, 'C' to play against the computer: "))
    quite(user_option)

## Type of game selection. Player vs. Player or Player vs Computer
    if(user_option == "P") or(user_option == "p"):
##      Only allows the Player vs Player code to run
        vs_player = True
        menu = False
    elif (user_option == "C") or (user_option == "c"):
##      Only allows the Player vs Computer code to run
        vs_computer = True
        vs_player = False
        menu = False
    else:
        print("Incorrect input. Please try again.")

## Player vs Player game play code.
    while vs_player:
        gformat()
##     The start of the second players code
        user_input = input("Type in the position of your next move, Player X. (1-9) or 'b' for menu: ")
        if quite(str(user_input)):
            break;
        if is_inrange(int(user_input)):
            if grid[int(user_input) - 1] != "X" and grid[int(user_input) - 1] != "0":
                grid[int(user_input) - 1] = "X"
                gformat()
                can_continue = True
                if isWinner_check("X",grid):
                    print("CONGRATULATIONS !!!! Player X has Won. Player X gets to go first.")
                    x_count = x_count +1 #Counts the number of times Player X wins
                    time.sleep(2)# Lets the program lag for 2 seconds before continuing
                    can_continue = False
                    to_clean()
                if isGrid_full(grid):
                    print("It is a Tie")
                    to_clean()
##            The start of the second players code
                while can_continue == True:
                    gformat()
                    user_input2 = input("Type in the position of your next move,Player 0. (1-9) or 'b' for menu:: ")
                    if quite(str(user_input2)):
                        break;
                    if is_inrange(int(user_input2)):
                        if grid[int(user_input2) - 1] != "X" and grid[int(user_input2) - 1] != "0":
                            grid[int(user_input2) - 1] = "0"
                            gformat()
                            can_continue = False
                            if isWinner_check("0",grid):
                                print("CONGRATULATIONS !!!!Player 0 has Won. Player 0 gets to go first.")
                                o_count = o_count + 1 #Counts the number of times Player 0 won
                                time.sleep(2)# Lets the program lag for 2 seconds before continuing
                                can_continue = False
                                to_clean() #Over-rides the grid
                            if isGrid_full(grid):
                                print("It is a Tie")
                                to_clean() #Over-rides the grid
                        else:
                            print("This spot is taken")
                            gformat()
                    else:
                        print("Your position is out of range or is invalid. Please try again.")
                        time.sleep(2)
            else:
                print("This spot is taken")
                gformat() #reprints the format
        else:
            print("Your position is out of range or is invalid. Please try again.")
            time.sleep(1)
        if isGrid_full(grid):
            print("It is a Tie")
            to_clean() #Over-rides the grid

## Player vs Computer game play code.
    while vs_computer:
        gformat()
##   The start of the Players code
        user_input = input("Type in the position of your next move, Player X. (1-9) or 'b' for menu: ")
        if quite(str(user_input)):
            break;
        if is_inrange(int(user_input)):
            if grid[int(user_input) - 1] != "X" and grid[int(user_input) - 1] != "0":
                grid[int(user_input) - 1] = "X"
                gformat()
                can_continue = True # Boolean allows for the AI code to be run instead of skipping it until player X enters a valid input
                if isWinner_check("X",grid):
                    print("CONGRATULATIONS !!!! Player X has Won. Player X gets to go first.")
                    x_count = x_count +1 #Counts the number of times Player X won
                    time.sleep(2)# Lets the program lag for 2 seconds before continuing
                    can_continue = False
                    to_clean() #Over-rides the grid
                if isGrid_full(grid):
                    print("It is a Tie")
                    to_clean() #Over-rides the grid

## Computer move. Start of the AI code
                while can_continue == True:
                    com_play = com_move("0",grid)
                    grid[com_play] = "0"
                    gformat()
                    can_continue = False
                    if isWinner_check("0",grid):
                        print("CONGRATULATIONS !!!!Player 0 has Won. Player 0 gets to go first.")
                        o_count = o_count + 1 #Counts the number of times Player 0 won
                        time.sleep(2)# Lets the program lag for 2 seconds before continuing
                        can_continue = True
                        to_clean()
                    if isGrid_full(grid):
                        print("It is a Tie")
                        to_clean() #Over-rides the grid
                        can_continue = False
            else:
                print("This spot is taken")
                gformat()
        else:
            print("Your position is out of range or is invalid. Please try again.")
            time.sleep(1)
        if isGrid_full(grid):
            print("It is a Tie")
            to_clean()  #Over-rides the grid
