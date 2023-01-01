import os
import UI.showInfo as showInfo
import Backend.GameLogic.validation as validation
import Backend.GameLogic.utils as utils


class PlaceShips():

  def placeShip(auto, player, boatLen, boatID):
    validRange = False
    validState = False
    while (validRange == False or validState == False):
      if auto:
        # if automatically placing ship gets random coordinates and orientation
        orientation = utils.Utils.getRandomOrientation()
        if (orientation == "V"):
          #check if space to place vertically
          space = validation.Validation.VerSpace(player.gameBoard, boatLen)
          if space == False:
            orientation = "H"
        else:
          #check if space to place horizontally
          space = validation.Validation.HorSpace(player.gameBoard, boatLen)
          if space == False:
            orientation = "V"
        x, y = utils.Utils.getRandomCoordinates(player.gameBoard)
      else:
        # get user inputs
        orientation = utils.Utils.getOrientation()
        x, y = utils.Utils.getCoordinates(player.gameBoard)
      validRange = validation.Validation.checkBoardRange(player.gameBoard, x, y, orientation, boatLen)    
      
      if (validRange):
          validState = validation.Validation.checkBoardState(player.gameBoard, x, y, orientation, boatLen)
          if (validState):
            #if everything is valid then place the ship
            player.gameBoard = PlaceShips.place(player.gameBoard, x, y, orientation, boatLen, boatID)
            

  def oneShip(auto, player):
    #if only one ship being placed, don't need a for loop
    os.system('clear')
    showInfo.DisplayInfo.getBoard(player, "game")
    boat = PlaceShips.getUserBoat(player)
    boatLen = boat.length
    boatID = boat.ID
    boatStatus = boat.status
    if (boatStatus == 1):
      PlaceShips.removeShip(player.gameBoard, boatID)
    PlaceShips.placeShip(auto, player, boatLen, boatID)
    boat.status = 1
    
    
  def autoPlaceAvailable(player):
    for i in range(len(player.boats)):
      boat = player.boats[i]
      if (boat.status == 0):
        # checks whether ship is not already placed
        boatLen = boat.length
        boatID = boat.ID
        PlaceShips.placeShip(True, player, boatLen, boatID)
        boat.status = 1

  
  def autoPlaceAll(player):
    # places all ships regardless of already placed so clears board and status
    PlaceShips.resetBoard(player)
    for i in range(len(player.boats)):
      boat = player.boats[i]
      boatLen = boat.length
      boatID = boat.ID
      
      PlaceShips.placeShip(True, player, boatLen, boatID)
      boat.status = 1
      
  
  def resetBoard(player):
    for i in range(1, len(player.gameBoard)):
      for j in range (1, len(player.gameBoard[i])):
        player.gameBoard[i][j] = 0
    for i in range(len(player.boats)):
      player.boats[i].status = 0
    #for each ship change status to not placed, go through board and make it back to 0
  
  def getUserBoat(player):
    # gets the boat of the ID the user enters
    valid = False
    while (valid == False):
      showInfo.DisplayInfo.getBoatInfo(player)
      print("\nEnter ID of boat: ")
      id = input().upper()
      for i in range(len(player.boats)):
        if (id == player.boats[i].ID):
          valid = True
          return player.boats[i]

  
  def allBoatsPlaced(player):
    # checks whether all boats have been placed
    for i in range(len(player.boats)):
      boat = player.boats[i]
      if (boat.status == 0):
        return False
    return True

  def place(board, x, y, orientation, boatLen, ID):
    # places boat on board
    x = utils.Utils.getXIndex(board, x)
    if (orientation == "H"):
      for i in range(x, x+boatLen):
        board[y][x] = ID
        x +=1
    else:
      for i in range(y, y+boatLen):
        board[y][x] = ID
        y +=1
    return board

  
  def removeShip(board, id):
    # removes a ship from the board and resets ship status
    for i in range(1, len(board)):
      for j in range (1, len(board[i])):
        if (board[i][j] == id):
          board[i][j] = 0

  