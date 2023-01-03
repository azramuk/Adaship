import Backend.GameConfig.adaship as adaship
import Backend.GameConfig.readConfigFile as readConfigFile
import Backend.GameLogic.validation as validation
import Backend.GameLogic.boatInfo as boatInfo
import UI.headers as headers


class GameConfig():
  def __init__(self):
    self.board = []
    self.boats = []

  
  def ownBoardSize(): # function to get user input for board size
    num = False
    while (not num):
      width = input(f"{headers.TextColours.MAGENTA}".format("Enter width between 5 and 80: "))
      height = input(f"{headers.TextColours.MAGENTA}".format("Enter height between 5 and 80: "))
      try:
        width=int(width)
        height = int(height)
        size = validation.Validation.boardSize(width, height)
        if (size):
          num = True
          return (width, height)
        else:
          print(f"{headers.TextColours.BG_RED}".format("\nBoard size not in range\n"))
      except ValueError:
        print(f"{headers.TextColours.BG_RED}".format("\nInput is not an integer\n"))
        continue

  
  def createBoard(): # can be called multiple times to create seperate boards
    width, height = readConfigFile.ConfigFile.getDimensions(adaship.adaship)
  
    if validation.Validation.boardSize(width, height): # validation check that board size is in range of 5 - 80
      
      board = []
      for i in range(height):
        row = []
        for i in range(width):
          row.append('0')
        board.append(row)

      # create column letters
      ascii = 65
      columns = [''] # start with empty space for the numbers column
      loop = 0 # counter to know whether the columns have reached the end of the alphabet in which case it will become AA, AB.. etc
      
      for i in range(width):
        if (i % 25 == 0 and i != 0): # checks whether index is divisible by 25 with no remainders to check whether it has done a full alphabet iteration
          loop += 1
          ascii = 65
          
        if loop == 0:
          columns.append(chr(ascii))
          ascii += 1
        elif loop == 1:
          columns.append("A"+chr(ascii))
          ascii += 1
        elif loop == 2:
          columns.append("B"+chr(ascii))
          ascii += 1
        elif loop == 3:
          columns.append("C"+chr(ascii))
          ascii += 1
    
      # create row numbers
      num = 1
      for i in range(height):
        board[i].insert(0, num)
        num += 1
     
      board.insert(0, columns)
      
      return board

  
  def boatsArray():
    boats = readConfigFile.ConfigFile.getBoats(adaship.adaship)
    boatsList = []
    
    for i in range(len(boats)):
      boatsList.append(boatInfo.Boat(boats[i][0][0],boats[i][0],boats[i][1])) # array of boat objects
      
    return boatsList

