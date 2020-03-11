import math
import random

def getEmptyIndex(board):
  for i in range(9):
    for j in range(9):
      if board[i][j] == 0:
        return (i, j)
  return None

def solveBoard(board):
  pos = getEmptyIndex(board)
  if pos == None:
    return True
  
  for i in range(9):
    if validate(board, pos[0], pos[1], i + 1):
      board[pos[0]][pos[1]] = i + 1

      if solveBoard(board):
        return True

      board[pos[0]][pos[1]] = 0

  return False


def validate(board, x, y, n):
  
  # validate column
  for i in range(9):
    if board[i][y] == n and i != x:
      return False
  
  # validate row
  for i in range(9):
    if board[x][i] == n and i != y:
      return False

  # validate box
  xmin = math.floor(x // 3)
  ymin = math.floor(y // 3)

  for i in range(xmin*3, xmin*3 + 3):
    for j in range(ymin*3, ymin*3 + 3):
      if board[i][j] == n and i != x and j != y:
        return False

  return True

if __name__ == "__main__":
  """
  board=[
    [6, 0, 8, 7, 0, 2, 1, 0, 0],
    [4, 0, 0, 0, 1, 0, 0, 0, 2],
    [0, 2, 5, 4, 0, 0, 0, 0, 0],
    [7, 0, 1, 0, 8, 0, 4, 0, 5],
    [0, 8, 0, 0, 0, 0, 0, 7, 0],
    [5, 0, 9, 0, 6, 0, 3, 0, 1],
    [0, 0, 0, 0, 0, 6, 7, 5, 0],
    [2, 0, 0, 0, 9, 0, 0, 0, 8],
    [0, 0, 6, 8, 0, 5, 2, 0, 3]
  ]
  """
  board = [
    [0,7,0,0,4,2,0,0,0],
    [0,0,0,0,0,8,6,1,0],
    [3,9,0,0,0,0,0,0,7],
    [0,0,0,0,0,4,0,0,9],
    [0,0,3,0,0,0,7,0,0],
    [5,0,0,1,0,0,0,0,0],
    [8,0,0,0,0,0,0,7,6],
    [0,5,4,8,0,0,0,0,0],
    [0,0,0,6,1,0,0,5,0]
  ]
  """
  board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
  ]
  """
  solveBoard(board)
  for row in board:
    print(row)
