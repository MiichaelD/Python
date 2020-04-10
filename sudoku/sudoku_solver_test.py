import sudoku_solver


def test_get_quadrant_():
  assert solver.get_quadrant_start_index(1) == 0, "row/column 1 is in quadrant with row/column 0"
  assert solver.get_quadrant_start_index(4) == 3, "row/column 1 is in quadrant with row/column 0"
  assert solver.get_quadrant_start_index(7) == 6, "row/column 1 is in quadrant with row/column 0"

def test_finds_number_in_row():
  solver.board[4][8] = 4
  assert solver.is_valid(4, 4, 4) == False, "Number is not valid, found in same row" 
  solver.board[4][8] = 0

def test_finds_number_in_col():
  solver.board[8][4] = 4
  assert solver.is_valid(4, 4, 4) == False, "Number is not valid, found in same col" 
  solver.board[8][4] = 0

def test_finds_number_in_quadrant():
  solver.board[5][5] = 4
  assert solver.is_valid(4, 4, 4) == False, "Number is not valid, found in same quadrant" 
  solver.board[5][5] = 0


if __name__ == "__main__":
  global solver
  solver = sudoku_solver.SudokuSolver()
  test_get_quadrant_()
  test_finds_number_in_row()
  test_finds_number_in_col()
  test_finds_number_in_quadrant()
  print("Finished")

