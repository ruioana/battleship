from random import randint

board = []
"""we are now creating a 5x5 board"""
for i in range(5):
  board.append(['O'] * 5)

  """created a function so swe can print the board like a grid,
  for clarity reasons"""
def print_board(board):
  for row in board:
    print (" ".join(row))

"""hiding the battleship in a random location"""
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#showing the location of our ship (if we want)
#print ship_row
#print ship_col

for turn in range(4): #created a loop so we can let the user guess 4 times
  print ("Turn", turn + 1)
  #asking the user to guess/seek the ship
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  #checking user guess vs ships location"""
  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations!You sank my battleship!")
    break # if user wins, no more guesses
  else:
    #checking to see if user guessed outside the range
    if guess_row not in range(5) or guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
      #checking to see if user guessed the same location twice
    elif [board[guess_row][guess_col]] == 'X':
      print ("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    print_board(board)
    #telling the user the game is over after his guesses
  if turn == 3:
    print("Game Over!")



