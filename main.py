from utils import Utils as utils
from utils import State

def main():
    # game state object for holding current state
    game_state = State(3, 'X', 'O')

    while True:
      utils.display_board(game_state._board)

      # player 
      while True:
        position = int(input("Enter your move (1-9): ")) - 1
        if utils.check_if_space_free(position, game_state._board):
          break
        else:
          print("Invalid move. Please try again.")
      utils.make_move(position, game_state._player, game_state._board)

      if utils.check_is_winner(game_state._player, game_state._board):
        utils.display_board(game_state._board)
        print("You win!")
        break
      elif utils.is_board_full(game_state._board):
        utils.display_board(game_state._board)
        print("It's a draw!")
        break

      # computer 
      position = utils.get_computer_move(game_state._computer, game_state._board, game_state._player)
      utils.make_move(position, game_state._computer, game_state._board)
      print(f"Computer plays at position {position + 1}")  # Show computer's move

      if utils.check_is_winner(game_state._computer, game_state._board):
        utils.display_board(game_state._board)
        print("You lose!")
        break
      elif utils.is_board_full(game_state._board):
        utils.display_board(game_state._board)
        print("It's a draw!")
        break

if __name__ == '__main__':
    main()
