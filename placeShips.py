import random
import os
import autoFunctions, computerConfig, computerLogic, config, menu, playerConfig, playGame, readConfigFile, validation, adaship


def userPlaceShip(player):
  os.system('clear')
  player.getBoard("game")
  boat = getUserBoat(player)
  boatLen = boat[2]
  boatID = boat[0]
  boatStatus = boat[4]
  if (boatStatus == 1):
    PlaceShips.removeShip(player.gameBoard, boatID)
  validRange = False
  validState = False
  while (validRange == False or validState == False):
    orientation = PlaceShips.getOrientation()
    x, y = PlaceShips.getCoordinates(player.gameBoard)
    validRange = PlaceShips.checkBoardRange(player.gameBoard, x, y, orientation, boatLen)    
    #print(validRange)
    if (validRange):
        validState = PlaceShips.checkBoardState(player.gameBoard, x, y, orientation, boatLen)
        if (validState):
          player.gameBoard = PlaceShips.place(player.gameBoard, x, y, orientation, boatLen, boatID)
          boat[4] = 1
          #  RETURN BOARD, BOATS

def userAutoPlace(player):
  os.system('clear')
  player.getBoard("game")
  boat = getUserBoat(player)
  #run automatic placing function passing chosen parameters
  boatLen = boat[2]
  boatID = boat[0]
  boatStatus = boat[4]
  if (boatStatus == 1):
    PlaceShips.removeShip(player.gameBoard, boatID)
  #checkBoardSpace, if false then notify user and return to menu
  validRange = False
  validState = False
  while (validRange == False or validState == False):
    orientation = PlaceShips.getRandomOrientation()
    x, y = PlaceShips.getRandomCoordinates(player.gameBoard)
    validRange = PlaceShips.checkBoardRange(player.gameBoard, x, y, orientation, boatLen)
    #print(validRange)
    if (validRange):
        validState = PlaceShips.checkBoardState(player.gameBoard, x, y, orientation, boatLen)
        if (validState):
          player.gameBoard = PlaceShips.place(player.gameBoard, x, y, orientation, boatLen, boatID)
          boat[4] = 1
          #  RETURN BOARD, BOATS
  

def autoPlaceAvailable(player):
  for i in range(1, len(player.boats)):
    boat = player.boats[i]
    if (boat[4] == 0):
      boatLen = boat[2]
      boatID = boat[0]
      #checkBoardSpace, if == false then notify user that not all boats could be placed, return to menu
      validRange = False
      validState = False
      while (validRange == False or validState == False):
        orientation = PlaceShips.getRandomOrientation()
        x, y = PlaceShips.getRandomCoordinates(player.gameBoard)
        validRange = PlaceShips.checkBoardRange(player.gameBoard, x, y, orientation, boatLen)
        
        #print(validRange)
        if (validRange):
          validState = PlaceShips.checkBoardState(player.gameBoard, x, y, orientation, boatLen)
          if (validState):
            player.gameBoard = PlaceShips.place(player.gameBoard, x, y, orientation, boatLen, boatID)
            boat[4] = 1
  #check for not placed, for loop, call autoplace for each non placed
            #  RETURN BOARD, BOATS

def autoPlaceAll(player):
  resetBoard(player)
  for i in range(1, len(player.boats)):
    changedBoard = player.gameBoard
    boatStatus = player.boats[i][4]
    boat = player.boats[i]
    boatLen = boat[2]
    boatID = boat[0]
    #checkBoardSpace, if == false then reset board, i = 1
    space = checkBoardSpace(changedBoard, boatLen)
   
    if (space == False):
      print("resetting")
      resetBoard(player)
      #break for and start again
    else:
      if (boatStatus == 1):
        PlaceShips.removeShip(changedBoard, boatID)
      validRange = False
      validState = False
      while (validRange == False or validState == False):
        orientation = PlaceShips.getRandomOrientation()
        if (orientation == "V"):
          #check if v space
          space = VerSpace(changedBoard, boatLen)
          if space == False:
            orientation = "H"
        else:
          space = HorSpace(changedBoard, boatLen)
          if space == False:
            orientation = "V"
        x, y = PlaceShips.getRandomCoordinates(changedBoard)
        validRange = PlaceShips.checkBoardRange(changedBoard, x, y, orientation, boatLen)
        
        #print(validRange)
        if (validRange):
          validState = PlaceShips.checkBoardState(changedBoard, x, y, orientation, boatLen)
          if (validState):
            changedBoard = PlaceShips.place(changedBoard, x, y, orientation, boatLen, boatID)
            boat[4] = 1
    player.gameBoard = changedBoard
  # for every ship call autoplace
          #  RETURN BOARD, BOATS

def resetBoard(player):
  for i in range(1, len(player.gameBoard)):
    for j in range (1, len(player.gameBoard[i])):
      player.gameBoard[i][j] = 0
  for i in range(1, len(player.boats)):
    player.boats[i][4] = 0
  #for each ship change status to not placed, go through board and make it back to 0
      #  RETURN BOARD, BOATS

def getUserBoat(player):
  valid = False
  while (valid == False):
    player.getBoatInfo()
    print("\nEnter ID of boat: ")
    id = input().upper()
    for i in range(1, len(player.boats)):
      if (id == player.boats[i][0]):
        valid = True
        return player.boats[i]

def allBoatsPlaced(player):
  for i in range(1, len(player.boats)):
    boat = player.boats[i]
    if (boat[4] == 0):
      return False
  return True





class PlaceShips():
  def getOrientation():
    orientation = input("Place ship veritcally or horizontally? (V/H): ").upper()
    while (orientation != "V" and orientation !="H"):
      orientation = input("Please enter valid choice: ").upper()
    return orientation

  def getCoordinates(board):
    coordsValid = False
    while (coordsValid == False):
      inputValid = False
      while (inputValid == False):
        x = input("\nEnter the x coordinate (e.g B): ")
        y = input("Enter the y coordinate (e.g 2): ")
        try:
          x = x.upper()
          y = int(y)
          inputValid = True
        except ValueError:
          print("\nx coordinate must be a letter(s) and y coordinate must be an integer\n")
          
      coordsValid = PlaceShips.checkCoordinates(board, x, y)
    return x,y

  def checkCoordinates(board, x, y): #get x index check if less than len check if y less than len?
    if (x in board[0]):
      for i in range(len(board)):
        if (board[i][0] == y):
          return True
        i += 1
    return False

  def getXIndex(board, x):
    index = board[0].index(x)
    return index

  def checkBoardRange(board, x, y, orientation, boatLen):
    # y already int, find position of x
    x = PlaceShips.getXIndex(board, x)
    if (orientation == "H"):
      end = x + boatLen - 1
      if (end < len(board[0])):
        return True
    else:
      end = y + boatLen - 1
      if (end < len(board)):
        return True
    return False

  def place(board, x, y, orientation, boatLen, ID):
    x = PlaceShips.getXIndex(board, x)
    if (orientation == "H"):
      for i in range(x, x+boatLen):
        board[y][x] = ID
        x +=1
    else:
      for i in range(y, y+boatLen):
        board[y][x] = ID
        y +=1
    return board

  def getRandomOrientation():
    ori = random.randint(1,2)
    if (ori == 1):
      return "H"
    else:
      return "V"

  def getRandomCoordinates(board):
    x = random.randint(1, len(board[0])-1)
    x = board[0][x]
    y = random.randint(1, len(board)-1)
    y = board[y][0]
    return x, y

  def checkBoardState(board, x, y, orientation, boatLen):
    x = PlaceShips.getXIndex(board, x)
    if (orientation == "H"):
      for i in range(x, x+boatLen):
        if (board[y][x] != "0" and board[y][x] != 0):
          return False
        x +=1
    else:
      for i in range(y, y+boatLen):
        if (board[y][x] != "0" and board[y][x] != 0 ):
          return False
        y +=1
    return True

  def removeShip(board, id):
    for i in range(1, len(board)):
      for j in range (1, len(board[i])):
        if (board[i][j] == id):
          board[i][j] = 0


#check if place on board for ship:
#using orientation check whether there are 0's in a row for length of ship, if there isn't swap orientation and do the same, if there isn't then reset board and start autoplace, if chosen autoplace specific and there isn't then give user a message that there is no space, ask to reset or not so they can move on their own

def checkBoardSpace(board, shiplen):
  space = False
  space = HorSpace(board, shiplen)
  if space == True:
    return space
  else: 
    space = VerSpace(board, shiplen)
  return space
  #return true
  
  # if (ori == "H"):
  #   space = HorSpace(board, shiplen)
  #   if (space == False):
  #     space = VerSpace(board, shiplen)
  #     if (space == False):
  #       print("Ship won't fit")
  #     else:
  #       ori = "V"
  # else:
  #   space = VerSpace(board, shiplen)
  #   if (space == False):
  #     space = HorSpace(board, shiplen)
  #     if (space == False):
  #       print("Ship won't fit")
  #     else:
  #       ori = "H"
  # return space, ori


  # if space is returned false then print ("won't fit, would you like to reset board or do it yourself?") or clear board and start autoplace all again
      




def HorSpace(board, shiplen):
  space = False
  empty = 0
  for i in range(1, len(board)):
    empty = 0
    for j in range (1, len(board[i])):
      if (board[i][j] == "0" or board[i][j] == 0):
        empty += 1
      else:
        empty = 0
      if (empty >= shiplen):
        return True
  return False




def VerSpace(board, shiplen):
  space = False
  empty = 0
  for i in range(1, len(board[0])):
    empty = 0
    for j in range (1, len(board)):
      if board[j][i] == "0" or board[j][i] == 0:
        empty += 1
      else:
        empty = 0
      if (empty >= shiplen):
        return True
  return False
  
    
  