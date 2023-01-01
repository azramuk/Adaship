import Backend.GameConfig.boardBoatConfig as boardBoatConfig
import Backend.GameLogic.placeShips as placeShips
import UI.showInfo as showInfo

class Player():
  def __init__(self):
    self.name = ""
    self.targetBoard = boardBoatConfig.GameConfig.createBoard()
    self.gameBoard = boardBoatConfig.GameConfig.createBoard()
    self.hit = 0
    self.miss = 0
    self.boats = boardBoatConfig.GameConfig.boatsArray()

  
  def placeBoats(self):
    # method for computer placing ships
    placeShips.PlaceShips.autoPlaceAll(self)
    print("Computer Game Board Configuration")
    showInfo.DisplayInfo.getBoard(self, "game")
    showInfo.DisplayInfo.getBoatInfo(self)
