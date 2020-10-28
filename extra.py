
##        user_input = int(input("Your input is out of range.Type in the position of your next move, Player X. (1-9): "))
##    
####    if board[user_input - 1] != "X" and board[user_input - 1] != "0":
####        board[user_input - 1] = "X"
####        p_board()
####        switch = False
####    else:
####        print ("This spot is taken")
####        p_board()
##        
#### while switch == True:
##        while switch:
##            user_input2 = int(input("Type in the position of your next move,Player 0. (1-9): "))
####        
####        while is_inrange(user_input2):
####            continue
####        else:
####            user_input2 = int(input("Your input is out of range.Type in the position of your next move, Player 0. (1-9): "))
##        
##            if board[user_input2 - 1] != "X" and board[user_input2 - 1] != "0":
##                board[user_input2 - 1] = "0"
####                switch = True
##                p_board()
##                switch = False 
##            else:
##                print("This spot is taken")
##                p_board()    
##    else:
##        print("This spot is taken")
##        p_board()
####                switch = False
        



#ai
##def com_move(player,board):
##    for i in range(0,9):
##        if board[i] == " ":
##            board[i] = player
##            if iswinner_check(player, board):
##                return i
##            else:
##                board[i] = " "
##    if board[5] = " ":
##        return 5
##    while True:
##        move = random.randint(0,9)
##        if board[move] = " ":
##            return move
##            break
##    return 5    

##com_play = com_move("0",board)
##if board[com_play] = " ":
##    board[com_play] = "0"
##            













##from tkinter import *
##
##class App(tk.frame):
##    def _init_(self, master):
##        tk.Frame._init_(self,master)
##        self.pack()
##        self.master.title("hello world")
##
##        tk.Label(self,tesxt = "This is your first GUI. (highfive)").pack
##
##if name == '_main_':
##    root = tk.Tk()
##    app = App(root)
##    app.mainloop()
