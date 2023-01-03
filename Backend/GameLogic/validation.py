import Backend.GameLogic.utils as utils

class Validation():
  def boardSize(w:int, h:int):
    if ((w<5 or w>80) or (h<5 or h>80)):
      return False
    else:
      return True

  
  def checkState(board, x, y):
    # checks if a tile is empty
    y = int(y)
    x = utils.Utils.getXIndex(board, x)
    if(board[y][x] == "0"):
      return True
    return False

  
  def checkCoordinates(board, x, y):
    # check coordinates in board range
    if (x in board[0]):
      for i in range(len(board)):
        if (board[i][0] == y):
          return True
        i += 1
    return False

  
  def checkBoardRange(board, x, y, orientation, boatLen):
    # check that the whole boat is inside the board
    x = utils.Utils.getXIndex(board, x)
    if (orientation == "H"):
      end = x + boatLen - 1
      if (end < len(board[0])):
        return True
    else:
      end = y + boatLen - 1
      if (end < len(board)):
        return True
    return False

  
  def checkBoardState(board, x, y, orientation, boatLen):
    # check that every tile the ship will be placed on is empty
    x = utils.Utils.getXIndex(board, x)
    if (orientation == "H"):
      for i in range(x, x+boatLen):
        if (board[y][x] != "0"):
          return False
        x +=1
    else:
      for i in range(y, y+boatLen):
        if (board[y][x] != "0"):
          return False
        y +=1
    return True


  def HorSpace(board, shiplen):
    # checks if enough horizontal space for a ship to be placed anywhere on board
    empty = 0
    for i in range(1, len(board)):
      empty = 0
      for j in range (1, len(board[i])):
        if (board[i][j] == "0"):
          empty += 1
        else:
          empty = 0
        if (empty >= shiplen):
          return True
    return False

  
  def VerSpace(board, shiplen):    
    # checks if enough vertical space for a ship to be placed anywhere on board
    empty = 0
    for i in range(1, len(board[0])):
      empty = 0
      for j in range (1, len(board)):
        if board[j][i] == "0":
          empty += 1
        else:
          empty = 0
        if (empty >= shiplen):
          return True
    return False