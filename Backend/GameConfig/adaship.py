
import os
import Backend.GameConfig.boardBoatConfig as boardBoatConfig
import Backend.GameConfig.readConfigFile as readConfigFile


# Configures the settings of the game which will be the same no matter what game version
def AdashipSettings():
  global adaship # a global variable is used as the settings need to be accessed to configure the game play
  adaship = readConfigFile.ConfigFile()
  os.system('clear')
  print("Do you want to choose your own board size? y/n: ")
  valid = False
  while (not valid):
    answer = input().lower()
    if (answer == "y"):
      valid = True
      os.system('clear')
      width, height = boardBoatConfig.GameConfig.ownBoardSize() # this gets user input as the board dimensions
    elif (answer != "n"):
      print("Enter a valid choice: ")
    else:
      valid = True
      width, height = readConfigFile.ConfigFile.getDimensions(adaship) # if the user chooses not to use own dimensions, it sets to the dimensions that has been retrieved from the file
  adaship.setUserDimensions(width, height) # sets the dimensions to the config file