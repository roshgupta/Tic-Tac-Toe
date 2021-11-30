import random

def initialise():
  board = []
  for i in range(0,3):
    board.append(["-","-","-"])
  return board

def print_board(board):
  for i in range(0,3):
    for j in range(0,3):
      print(board[i][j], end=" ")
    print("\n")
  print("\n")

def check_board_full(board):
  for i in range(0,3):
    for j in range(0,3):
      if board[i][j] == "-":
        return False
  return True

def check_win(board, player):
  for i in range(0,3):
    if board[i][0] == player and board[i][1] == player and board[i][2] == player:
      return True
  for i in range(0,3):
    if board[0][i] == player and board[1][i] == player and board[2][i] == player:
      return True
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  return False

def check_win_ai(board, player):
  for i in range(0,3):
    if board[i][0] == player and board[i][1] == player and board[i][2] == player:
      return True
  for i in range(0,3):
    if board[0][i] == player and board[1][i] == player and board[2][i] == player:
      return True
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:

def get_random():
  return random.randint(0, 1)

def swap_player():
  if player_current == player_1:
    player_current=player_2
  else:
    player_current=player_1

def turn():
  if player_current == player_1 :
    print("Player 1's turn : ")
  else :
    print("Player 2's turn : ")
def start_game():
  game_board = initialise()
  not_win = True
  if get_random==0:
    player_1 = "X"
    player_2 = "O"
  else:
    player_1= "O"
    player_2= "X"
  print("Let's start the game !")
  print("Player 1 has '{player_1}' and Player 2 has '{player_2}' ")
  player_current = player_1
  while not_win:
    print(game_board)
    print()

