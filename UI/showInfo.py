import sys

class DisplayInfo():

  def getBoard(player, boardType):
    if boardType == "target":
      print("\nTarget Board: \n")
      s = [[str(e) for e in row] for row in player.targetBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))
    elif boardType == "game":
      print("\nGame Board: \n")
      s = [[str(e) for e in row] for row in player.gameBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))
    elif boardType == "both":
      print("\nTarget Board: \n")
      s = [[str(e) for e in row] for row in player.targetBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))
  
      print("\nGame Board: \n")
      s = [[str(e) for e in row] for row in player.gameBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))

  
  def getBoatInfo(player):
    print("\nBoat Info: \n")
    DisplayInfo.prt_width("ID", 3)
    DisplayInfo.prt_width("Name", 13)
    DisplayInfo.prt_width("Length", 7)
    DisplayInfo.prt_width("Damage", 7)
    DisplayInfo.prt_width("Status", 7)
    DisplayInfo.prt_width('\n', 0)
    for boat in player.boats:
      DisplayInfo.prt_width(boat.ID, 3)
      DisplayInfo.prt_width(boat.name, 13)
      DisplayInfo.prt_width(str(boat.length), 7)
      DisplayInfo.prt_width(str(boat.damage), 7)
      DisplayInfo.prt_width(str(boat.status), 7)
      DisplayInfo.prt_width('\n', 0)
    
  def prt_width(str, width):
      sys.stdout.write('| ' + str + ' '*(width-len(str)))
      sys.stdout.flush()