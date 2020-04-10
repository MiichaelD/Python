import numpy as np

class SudokuSolver(object):
  
  def __init__(self):
    self.board = [[0,0,0,0,0,0,0,0,0],  # Row 0
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],] # Row 8

  def is_valid(self, row, col, num):
    # Check if number is found in same column
    for r in range(9):
      if self.board[r][col] == num:
        return False
    
    # Check if number is found in same row
    for c in range(9):  
      if self.board[row][c] == num:
        return False
    
    # Check if number is foind in same quadrant
    quadrant_row_ind = self._get_quadrant_start_index(row)
    quadrant_col_ind = self._get_quadrant_start_index(col)
    for r in range(quadrant_row_ind, quadrant_row_ind + 3):
      for c in range(quadrant_col_ind, quadrant_col_ind + 3):
        if self.board[r][c] == num:
          return False
    return True

  def solve(self, stop_at_first=True):
    for r in range(9):
      for c in range(9):
        if self.board[r][c] == 0:
          # Try every number (in-order, no optimization).
          for num in range(1, 10):
            if self.is_valid(r, c, num):
              self.board[r][c] = num
              if self.solve():
                return True
              self.board[r][c] = 0
          return False # Exhausted positibilities, stop.

    # If we reached this point it means ther were no more empty squares
    print(np.matrix(self.board))
    if stop_at_first:
      return True

    input("More? y/n")
    return False

  def _get_quadrant_start_index(self, axis):
    return axis // 3 * 3

if __name__ == "__main__":
  solver = SudokuSolver()
  solver.solve()

