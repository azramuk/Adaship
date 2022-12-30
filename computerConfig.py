import autoFunctions, computerLogic, config, menu, placeShips, playerConfig, playGame, readConfigFile, validation, adaship

class Computer():
  def __init__(self):
    self.targetBoard = config.GameConfig.createBoard()
    self.gameBoard = config.GameConfig.createBoard()
    self.hit = 0
    self.miss = 0
    self.boats = config.GameConfig.boatsArray()

  def placeBoats(self):
    placeShips.autoPlaceAll(self)
    print("\nComputer Game Board: \n")
    s = [[str(e) for e in row] for row in self.gameBoard]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))
    Computer.getBoatInfo(self)

  def getBoard(self, boardType):
    if boardType == "target":
      print("\nTarget Board: \n")
      s = [[str(e) for e in row] for row in self.targetBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))
      #print(np.matrix(self.targetBoard))
    elif boardType == "game":
      print("\nGame Board: \n")
      s = [[str(e) for e in row] for row in self.gameBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))
      #print(np.matrix(self.gameBoard))
    elif boardType == "both":
      print("\nTarget Board: \n")
      s = [[str(e) for e in row] for row in self.targetBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))
  
      print("\nGame Board: \n")
      s = [[str(e) for e in row] for row in self.gameBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))

  def getBoatInfo(self):
    print("\nBoat Info: \n")
    s = [[str(e) for e in row] for row in self.boats]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))