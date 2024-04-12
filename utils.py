class Utils:
    # Define board and player markers
    board = [' ' for _ in range(9)]
    player = 'X'
    computer = 'O'

    # Function to print the board
    def print_board(board):
      for i in range(3):
        print(' | '.join(board[i*3:(i*3)+3]))
        if i != 2:
          print('-' * 9)

    # Function to check if a space is empty
    def is_space_free(position, board):
      return board[position] == ' '


    # Function to check if a player has won
    def is_winner(mark, board):
      win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
      for condition in win_conditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
          return True
      return False

    # Function to check for a draw
    def is_board_full(board):
      for space in board:
        if space == ' ':
          return False
      return True

    # Function to place a move on the board
    def make_move(position, mark, board):
      board[position] = mark

    # Function to get available positions on the board
    def get_available_positions(board):
      return [i for i, space in enumerate(board) if space == ' ']

    # Minimax algorithm function with Alpha-Beta Pruning
    def minimax(board, depth, is_maximizing, alpha, beta, player, computer):
      # Check if the game is over
      if Utils.is_winner(player, board):
        return -10
      if Utils.is_winner(computer, board):
        return 10
      if Utils.is_board_full(board):
        return 0

      # Evaluate score for maximizing player
      if is_maximizing:
        best_score = -float('inf')
        for position in Utils.get_available_positions(board):
          Utils.make_move(position, computer, board)
          score = Utils.minimax(board, depth + 1, False, alpha, beta, player, computer)
          Utils.make_move(position, ' ', board)  # Undo the move
          best_score = max(best_score, score)
          alpha = max(alpha, best_score)
          if beta <= alpha:
            break  # Prune unnecessary branches
      else:
        best_score = float('inf')
        for position in Utils.get_available_positions(board):
          Utils.make_move(position, player, board)
          score = Utils.minimax(board, depth + 1, True, alpha, beta, player, computer)
          Utils.make_move(position, ' ', board)  # Undo the move
          best_score = min(best_score, score)
          beta = min(beta, best_score)
          if beta <= alpha:
            break  # Prune unnecessary branches

      # Return score based on maximizing or minimizing player
      return best_score

    # Function to get the computer's best move
    def get_computer_move(computer, board, player):
      best_score = -float('inf')
      best_move = None
      alpha = -float('inf')
      beta = float('inf')
      for position in Utils.get_available_positions(board):
        Utils.make_move(position, computer, board)
        score = Utils.minimax(board, 0, False, alpha, beta, player, computer)
        Utils.make_move(position, ' ', board)  # Undo the move
        if score > best_score:
          best_score = score
          best_move = position
      return best_move

