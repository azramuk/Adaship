import autoFunctions, computerConfig, computerLogic, menu, placeShips, playerConfig, playGame, readConfigFile, validation, adaship

class GameConfig():
  def __init__(self):
    self.board = []
    self.boats = []

  def ownBoardSize():
    num = False
    while (not num):
      width = input("Enter width between 5 and 80: ")
      height = input("Enter height between 5 and 80: ")
      try:
        width=int(width)
        height = int(height)
        size = validation.Validation.boardSize(width, height)
        if (size):
          num = True
          return (width, height)
        else:
          print("\nBoard size not in range\n")
      except ValueError:
        print("\nInput is not an integer\n")
        continue
  
  def createBoard(): #4 boards need to be created
    width, height = readConfigFile.ConfigFile.getDimensions(adaship.adashipp)
  
    # board = [[0]*height]*width - wasn't working bc copies so couldn't individually change 
    if validation.Validation.boardSize(width, height): #call validation
      
      board = []
      for i in range(height):
        row = []
        for i in range(width):
          row.append('0')
        board.append(row)
     
      ascii = 65
      columns = [''] # start with empty space for the numbers column
      loop = 0
      # create column names
      for i in range(width):
        if (i % 25 == 0 and i != 0):
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
      
      # print (columns)
      board.insert(0, columns)
      

      
      return board
      #print (board)
      #print(np.matrix(board))

  def boatsArray():
    NOT_DEPLOYED = 0;
    boats = readConfigFile.ConfigFile.getBoats(adaship.adashipp)
    
    for i in range(len(boats)):
      boats[i].insert(0, boats[i][0][0])
      boats[i].append(0)
      boats[i].append(NOT_DEPLOYED)
    boats.insert(0, ["ID", "Name", "Length", "Damage", "Status"])
    # test = boats.copy()
    # print(boats)
    # print(test)
    return boats
    #print(boats)
    #create 2D array with first letter and length
