from copy import deepcopy
import autoFunctions, computerConfig, computerLogic, config, menu, placeShips, playerConfig, playGame, validation, adaship

class ConfigFile():
  def __init__(self):
    self.__file = None
    self.__width=0  # private instance attribute
    self.__height=0 # private instance attribute
    self.__boats=[]
    self.readConfigFile() #automatically sets based on file

  #do you want to use own board measurements? y/n then check input there
  def setUserDimensions(self, w,h):
    self.__width = w
    self.__height = h

  def readConfigFile(self):
    if self.__file is None:
      f = open("adaship_config.ini", "r")
      self.__file = f.readlines()
    count = 0

    for line in self.__file:
      count += 1
      type = ""
      i = 0
      while (i < len(line) and line[i] != ":"):
        type = type + line[i].lower()
        i += 1
    
      if (type == "board"):
        dimensions = line[i+1:].strip()
        width = int(dimensions.split("x")[0])
        height = int(dimensions.split("x")[1])
        # store width and height as attribute
        self.__width = width
        self.__height = height
      elif (type == "boat"):
        # from i to end split at comma and remove white spaces
        boat = line[i+1:].strip().split(",")
        boat[-1] = int(boat[-1])
        # test = line.split(" ")
        # type = test[1].split(",")[0]
        # length = int(test[-1])
        self.__boats.append(boat)
        # store array as attribute

  def getDimensions(self):
    return (self.__width, self.__height)
    
  def getBoats(self):
    return deepcopy(self.__boats)