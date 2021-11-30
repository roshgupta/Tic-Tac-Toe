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

print_board(initialise())