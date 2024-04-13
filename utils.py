class Utils:
    # display board 
    def display_board(game_state):
      for i in range(game_state._grid):
        print(' | '.join(game_state._board[i*game_state._grid:(i*game_state._grid)+game_state._grid]))
        if i != game_state._grid-1:
          print('-' * (game_state._grid * game_state._grid))

    # check if space empty 
    def check_if_space_free(position, board):
      return board[position] == ' '


    # check if player or computer has won 
    def check_is_winner(mark, board, grid):
        width = grid
        arr = []
        x = 0
        while width <= grid * grid:
            arr.append([i for i in range(x, width)])
            x += grid
            width += grid

        grouped_array = [[] for _ in range(grid)]
        for i in range(grid):
            for j in range(grid):
                grouped_array[j].append(arr[i][j])  # Append elements to groups

        all_conditions = arr + grouped_array

        diagonal_conditions = [[],[]]
        for i in range(grid):
            diagonal_conditions[0].append(arr[i][i])
        x = grid - 1
        for i in range(grid):
            diagonal_conditions[1].append(arr[i][i+x])
            x -= 2
        all_conditions = arr + grouped_array + diagonal_conditions

        win_conditions = all_conditions
        count = 0
        for condition in win_conditions:
            for i in range(grid):
                if board[condition[i]] == mark:
                    count += 1
                if count == grid:
                    return True
            count = 0
        return False

    # check if a draw
    def is_board_full(board):
      for space in board:
        if space == ' ':
          return False
      return True

    # make a move on the board
    def make_move(position, mark, board):
      board[position] = mark

    # get available positions on the board
    def get_available_positions(board, grid):
      return [i for i, space in enumerate(board) if space == ' ']

    # Minimax algorithm with Alpha-Beta Pruning
    def minimax(board, depth, is_maximizing, alpha, beta, player, computer, grid):
      # Check if the game is over
        if Utils.check_is_winner(player, board, grid):
            return -10
        if Utils.check_is_winner(computer, board, grid):
            return 10
        if Utils.is_board_full(board):
            return 0

      # Evaluate score for maximizing player
        if is_maximizing:
            best_score = -float('inf')
            for position in Utils.get_available_positions(board, grid):
                Utils.make_move(position, computer, board)
                score = Utils.minimax(board, depth + 1, False, alpha, beta, player, computer, grid)
                Utils.make_move(position, ' ', board)  # Undo the move
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # Prune unnecessary branches
        else:
            best_score = float('inf')
            for position in Utils.get_available_positions(board, grid):
                Utils.make_move(position, player, board)
                score = Utils.minimax(board, depth + 1, True, alpha, beta, player, computer, grid)
                Utils.make_move(position, ' ', board)  # Undo the move
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break  # Prune unnecessary branches

          # Return score based on maximizing or minimizing player
        return best_score

    # get the computer's best move
    def get_computer_move(computer, board, player, grid):
      best_score = -float('inf')
      best_move = None
      alpha = -float('inf')
      beta = float('inf')
      for position in Utils.get_available_positions(board, grid):
        Utils.make_move(position, computer, board)
        score = Utils.minimax(board, 0, False, alpha, beta, player, computer, grid)
        Utils.make_move(position, ' ', board)  # Undo the move
        if score > best_score:
          best_score = score
          best_move = position
      return best_move

# holds game state information
class State:
    def __init__(self, grid, player, computer):
        self._grid = grid
        self._tiles = State.tiles(self)
        self._board = State.board(self)
        self._player = player
        self._computer = computer

    def board(self):
        return [' ' for _ in range(self._tiles)]

    def tiles(self):
        return self._grid * self._grid

