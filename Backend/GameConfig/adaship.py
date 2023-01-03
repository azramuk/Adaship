import os
import Backend.GameConfig.boardBoatConfig as boardBoatConfig
import Backend.GameConfig.readConfigFile as readConfigFile
import UI.headers as headers


# Configures the settings of the game which will be the same no matter what game version
def AdashipSettings():
  global adaship # a global variable is used as the settings need to be accessed to configure the game play
  adaship = readConfigFile.ConfigFile()
  os.system('clear')
  print(f"{headers.TextColours.MAGENTA}".format("Do you want to choose your own board size? y/n: "))
  valid = False
  while (not valid):
    answer = input().lower()
    if (answer == "y"):
      valid = True
      os.system('clear')
      width, height = boardBoatConfig.GameConfig.ownBoardSize() # this gets user input as the board dimensions
    elif (answer != "n"):
      print(f"{headers.TextColours.BG_RED}".format("\nEnter a valid choice\n"))
    else:
      valid = True
      width, height = readConfigFile.ConfigFile.getDimensions(adaship) # if the user chooses not to use own dimensions, it sets to the dimensions that has been retrieved from the file
  adaship.setUserDimensions(width, height) # sets the dimensions to the config file