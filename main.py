from utils import Utils as utils
# Define board and player markers
board = [' ' for _ in range(9)]
player = 'X'
computer = 'O'

# Main game loop
while True:
  utils.print_board(board)

  # Player's turn
  while True:
    position = int(input("Enter your move (1-9): ")) - 1
    if utils.is_space_free(position, board):
      break
    else:
      print("Invalid move. Please try again.")
  utils.make_move(position, player, board)

  if utils.is_winner(player, board):
    utils.print_board(board)
    print("You win!")
    break
  elif utils.is_board_full(board):
    utils.print_board(board)
    print("It's a draw!")
    break

  # Computer's turn
  position = utils.get_computer_move(computer, board, player)
  utils.make_move(position, computer, board)
  print(f"Computer plays at position {position + 1}")  # Show computer's move

  if utils.is_winner(computer, board):
    utils.print_board(board)
    print("You lose!")
    break
  elif utils.is_board_full(board):
    utils.print_board(board)
    print("It's a draw!")
    break
