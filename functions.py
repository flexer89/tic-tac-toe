
logo = '''
  _______         __                __           
 /_  __(_)____   / /_____ ______   / /_____  ___ 
  / / / / ___/  / __/ __ `/ ___/  / __/ __ \/ _ \\
 / / / / /__   / /_/ /_/ / /__   / /_/ /_/ /  __/
/_/ /_/\___/   \__/\____/\___/   \__/\____/\___/ 
                                              
                                        '''

def clear():
  print("\033[H\033[J", end="")

def board_count(board,sign):
  counter = 0
  for i in range(0,3):
    counter += board[i].count(sign)
  return counter
      
def draw_board(board):    
  print(" %c | %c | %c " % (board[0][0],board[0][1],board[0][2]))    
  print("___|___|___")    
  print(" %c | %c | %c " % (board[1][0],board[1][1],board[1][2]))    
  print("___|___|___")    
  print(" %c | %c | %c " % (board[2][0],board[2][1],board[2][2]))    
  print("   |   |   ")   
  
def check_win(board):
  if (board[0][0] is board[0][1] is board[0][2]) and board[0][0] != " ":
    return True
  elif board[1][0] is board[1][1] is board[1][2] and board[1][0] != " ":
    return True
  elif board[2][0] is board[2][1] is board[2][2] and board[2][2] != " ":
    return True
  elif board[0][0] is board[1][0] is board[2][0] and board[0][0] != " ":
    return True
  elif board[0][1] is board[1][1] is board[2][1] and board[1][1] != " ":
    return True
  elif board[0][2] is board[1][2] is board[2][2] and board[2][2] != " ":
    return True
  elif board[0][0] is board[1][1] is board[2][2] and board[1][1] != " ":
    return True
  elif board[0][2] is board[1][1] is board[2][0] and board[1][1] != " ":
    return True
  else:
    return False
    