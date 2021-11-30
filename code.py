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



print_board(initialise())