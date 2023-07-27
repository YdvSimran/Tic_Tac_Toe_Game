board=['-', '-', '-',
       '-', '-', '-',
       '-', '-', '-']
currentplayer='X'
winner=None
gamerunning=True



# printing the game board
def printboard(board):
       print(board[0] + ' | ' + board[1] + ' | ' + board[2])
       print("----------")
       print(board[3] + ' | ' + board[4] + ' | ' + board[5])
       print("----------")
       print(board[6] + ' | ' + board[7] + ' | ' + board[8])
       print("----------")




# for talking user input
def playerinput(board):
       chance=int(input("enter your chance . range from 1-9:  "))
       if chance>=1 and chance<=9 and board[chance-1]=='-':
              board[chance-1]=currentplayer
       else:
              print("this place has already been taken by player!")


              
#check for win or tie
def checkhorizontal(board):
       global winner
       if board[0]==board[1]==board[2] and board[0]!='-':
              winner = board[0]
              return True
       elif board[3]==board[4]==board[5] and board[3]!='-':
              winner = board[3]
              return True
       elif board[6]==board[7]==board[8] and board[6]!='-':
              winner = board[6]
              return True      
def checkrow(board):
       global winner
       if board[0]==board[3]==board[6] and board[0]!='-':
              winner = board[0]
              return True
       elif board[1]==board[4]==board[7] and board[1]!='-':
              winner = board[1]
              return True
       elif board[2]==board[5]==board[8] and board[2]!='-':
              winner = board[2]
              return True
def checkdiag(board):
       global winner
       if board[0]==board[4]==board[8] and board[0]!='-':
              winner = board[0]
              return True
       elif board[2]==board[4]==board[6] and board[2]!='-':
              winner = board[2]
              return True
def checktie(board):
       global gamerunning
       if '-' not in board:
              printboard(board)
              print("it's a tie!!!!!!!!")
              gamerunning=False
def checkforwin():
       if checkdiag(board) or checkhorizontal(board) or checkrow(board):
              print(f"the winner is {winner}")
              
              


#switch the player
def switchplayer():
       global currentplayer
       if currentplayer == 'X':
              currentplayer ='0'
       else:
              currentplayer ='X'
       
       
              
# check for win or tie again
while gamerunning:
       printboard(board)
       playerinput(board)
       checkforwin()
       checktie(board)
       switchplayer()
