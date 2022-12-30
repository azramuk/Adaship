import autoFunctions, computerConfig, computerLogic, config, menu, placeShips, playerConfig, playGame, readConfigFile, adaship

class Validation():
  def boardSize(w:int, h:int):
    if ((w<5 or w>80) or (h<5 or h>80)):
      return False
    else:
      return True