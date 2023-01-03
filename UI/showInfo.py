import sys
import UI.headers as headers

class DisplayInfo():

  def getColour(cell, text):
    if cell == "0":
      temp = f"{headers.TextColours.BG_BLUE}".format(text)
    elif cell == "H":
      temp = f"{headers.TextColours.BG_GREEN}".format(text)
    elif cell == "X":
      temp = f"{headers.TextColours.BG_RED}".format(text)
    else:
      temp = f"{headers.TextColours.BG_YELLOW}".format(text)
    return temp

  def formatBoard(board):
    s = [[str(e) for e in row] for row in board]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = []
    two = False
    for row in s:
      if two == True:
        for i in range(1, len(row)):
          withWhite = " " + row[i] + " "
          temp = DisplayInfo.getColour(row[i], withWhite)
          if (i == 0):
            temp = withWhite
          row[i] = temp
      else:
        for i in range (1, len(row)):
          withwhite = " " + row[i] + " "
          temp = withwhite
          row[i] = temp
      table += [fmt.format(*row)]
      two = True
    print ('\n'.join(table))

  def getTarget(player):
    print(f"{headers.TextColours.BOLD_UNDERLINE}".format("\nTarget Board:\n"))
    DisplayInfo.formatBoard(player.targetBoard)

  def getGame(player):
    print(f"{headers.TextColours.BOLD_UNDERLINE}".format("\nGame Board:\n"))
    DisplayInfo.formatBoard(player.gameBoard)

  def getBoard(player, boardType):
    if boardType == "target":
      DisplayInfo.getTarget(player)
      
    elif boardType == "game":
      DisplayInfo.getGame(player)
      
    elif boardType == "both":
      DisplayInfo.getTarget(player)
      DisplayInfo.getGame(player)

  
  def getBoatInfo(player):

    idmax = 3
    namemax = 5
    lengthmax = 7
    damagemax = 7
    statusmax = 7

    for boat in player.boats:
      if len(boat.ID) + 1 > idmax:
        idmax = len(boat.ID) + 1
      if len(boat.name) + 1 > namemax:
        namemax = len(boat.name) + 1
      if len(str(boat.length)) + 1 > lengthmax:
        lengthmax = len(boat.length) + 1
      if len(str(boat.damage)) + 1 > damagemax:
        damagemax = len(boat.damage) + 1
      if len(str(boat.status)) + 1 > statusmax:
        statusmax = len(boat.status) + 1

    id = DisplayInfo.addWhiteSpace(idmax, "ID")
    name = DisplayInfo.addWhiteSpace(namemax, "Name")
    length = DisplayInfo.addWhiteSpace(lengthmax, "Length")
    damage = DisplayInfo.addWhiteSpace(damagemax, "Damage")
    status = DisplayInfo.addWhiteSpace(statusmax, "Status")
    
    print(f"{headers.TextColours.BOLD_UNDERLINE}".format("\nBoat Info:\n"))
    DisplayInfo.makeWidth(f"{headers.TextColours.BOLD}".format(id), idmax)
    DisplayInfo.makeWidth(f"{headers.TextColours.BOLD}".format(name), namemax)
    DisplayInfo.makeWidth(f"{headers.TextColours.BOLD}".format(length), lengthmax)
    DisplayInfo.makeWidth(f"{headers.TextColours.BOLD}".format(damage), damagemax)
    DisplayInfo.makeWidth(f"{headers.TextColours.BOLD}".format(status), statusmax)
    DisplayInfo.makeWidth('\n', 0)

    for boat in player.boats:
      DisplayInfo.makeWidth(boat.ID, idmax)
      DisplayInfo.makeWidth(boat.name, namemax)
      DisplayInfo.makeWidth(str(boat.length), lengthmax)
      DisplayInfo.makeWidth(str(boat.damage), damagemax)
      DisplayInfo.makeWidth(str(boat.status), statusmax)
      DisplayInfo.makeWidth('\n', 0)
    
  def makeWidth(str, width):
      sys.stdout.write('| ' + str + ' '*(width-len(str)))
      sys.stdout.flush()
  
  def addWhiteSpace(maxLen, name):
    nameLen = len(name)
    for i in range(maxLen - nameLen):
      name += " "
    return name
