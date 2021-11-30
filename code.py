import random

class TicTacToe:
  def initialise(self):
    self.game_board = []
    for i in range(0,3):
      self.game_board.append(["-","-","-"])


  def print_board(self):
    for i in range(0,3):
      for j in range(0,3):
        print(self.game_board[i][j], end=" ")
      print("\n")
    print("\n")

  def check_board_full(self):
    for i in range(0,3):
      for j in range(0,3):
        if self.game_board[i][j] == "-":
          return False
    return True

  def check_win( self):
    for i in range(0,3):
      if self.game_board[i][0] == self.player_current and self.game_board[i][1] == self.player_current and self.game_board[i][2] == self.player_current:
        return True
    for i in range(0,3):
      if self.game_board[0][i] == self.player_current and self.game_board[1][i] == self.player_current and self.game_board[2][i] ==self.player_current:
        return True
    if self.game_board[0][0] == self.player_current and self.game_board[1][1] == self.player_current and self.game_board[2][2] == self.player_current:
      return True
    if self.game_board[0][2] == self.player_current and self.game_board[1][1] == self.player_current and self.game_board[2][0] == self.player_current:
      return True
    return False


  def get_random(self):
    return random.randint(0, 1)

  def swap_player(self):
    if self.player_current == self.player_1:
      self.player_current=self.player_2
    else:
      self.player_current=self.player_1

  def turn(self):
    if self.player_current == self.player_1 :
      print("Player 1's turn : ")
    else :
      print("Player 2's turn : ")

  def start_game(self):
    self.initialise()
    self.not_win = True
    random = self.get_random()
    if random == 0:
      self.player_1 = "X"
      self.player_2 = "O"
    else:
      self.player_1= "O"
      self.player_2= "X"
    print("Let's start the game !")
    print("Player 1 has '"+ self.player_1 + "' and Player 2 has '" + self.player_2 +"' ")
    self.player_current = self.player_1
    while self.not_win:
      self.print_board()
      self.turn()
      row = int(input("Enter the row number : ")) - 1
      col = int(input("Enter the column number : ")) - 1
      self.game_board[row][col] = self.player_current
      if self.check_win():
        if self.player_current == self.player_1 :
          print("Player 1 is winner ")
        else :
          print("Player 1 is winner ")
        break
      elif self.check_board_full():
        print("DRAW !!")
        break
      self.swap_player()


Tic_Tac = TicTacToe()
Tic_Tac.start_game()
