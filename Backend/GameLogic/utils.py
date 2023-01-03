import Backend.GameLogic.validation as validation
import random
import UI.headers as headers

class Utils():
  
  def getCoordinates(board):
    coordsValid = False
    while (coordsValid == False):
      inputValid = False
      while (inputValid == False):
        x = input(f"{headers.TextColours.MAGENTA}".format("\nEnter the x coordinate (e.g B): "))
        y = input(f"{headers.TextColours.MAGENTA}".format("Enter the y coordinate (e.g 2): "))
        try:
          x = x.upper()
          y = int(y)
          inputValid = True
        except ValueError:
          print(f"{headers.TextColours.BG_RED}".format("\nx coordinate must be a letter(s) and y coordinate must be an integer\n"))
          
      coordsValid = validation.Validation.checkCoordinates(board, x, y)
    return x,y

  
  def getXIndex(board, x):
    #gets the index of the X coordinate instead of using the letter
    index = board[0].index(x)
    return index


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


  def getOrientation():
    orientation = input(f"{headers.TextColours.MAGENTA}".format("Place ship veritcally or horizontally? (V/H): ")).upper()
    while (orientation != "V" and orientation !="H"):
      orientation = input(f"{headers.TextColours.BG_RED}".format("Please enter valid choice: ")).upper()
    return orientation