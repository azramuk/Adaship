from copy import deepcopy


class ConfigFile():
  def __init__(self):
    self.__file = None
    self.__width=0  # private instance attribute
    self.__height=0 # private instance attribute - can only be changed from class function 'setUserDimensions'
    self.__boats=[]
    self.readConfigFile() #automatically sets based on file

  
  def setUserDimensions(self, w,h):
    self.__width = w
    self.__height = h

    
  #only opens and reads file once as controlled by None check making this a singleton function
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
        # add each identification of a boat to an array
        boat = line[i+1:].strip().split(",")
        boat[-1] = int(boat[-1])
        self.__boats.append(boat)

  
  def getDimensions(self):
    return (self.__width, self.__height)

    
  def getBoats(self):
    return deepcopy(self.__boats)