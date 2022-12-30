import autoFunctions, computerConfig, computerLogic, config, menu, placeShips, playerConfig, readConfigFile, validation, adaship
import os


def checkState(board, x, y):
  #if targetboard[coords] = 0 return true
  y = int(y)
  x = placeShips.PlaceShips.getXIndex(board, x)
  if(board[y][x] == "0" or board[y][x] == 0): #might need speech marks
    return True
  return False


def manualLaunch(player, computer):
  os.system('clear')
  player.getBoard("both")
  state = False
  while (state == False):
    x, y = placeShips.PlaceShips.getCoordinates(player.gameBoard) # change x to index
    state = checkState(player.targetBoard, x, y)
  y = int(y)
  x = placeShips.PlaceShips.getXIndex(player.gameBoard, x)
  if (computer.gameBoard[y][x] == "0" or computer.gameBoard[y][x] == 0):
    player.miss += 1
    player.targetBoard[y][x] = "X"
    print("\nShot was a MISS\n")
  else:
    print("\nShot was a HIT\n")
    player.targetBoard[y][x] = "H"
    player.hit += 1
    id = computer.gameBoard[y][x]
    for i in range(len(computer.boats)):
      if (computer.boats[i][0] == id):
        computer.boats[i][3] += 1
        if (computer.boats[i][3] == computer.boats[i][2]):
          print("SHIP SUNK\n")
          computer.boats[i][4] = 2
  input("Press enter to continue")

  #get user coords, check target board 0, if all valid check opponent game board - if not 0 increment hit else increment miss
  #using ID add one to damage in com boat info, check if damage = length, if yes change status to sunk and print boat sunk
  #check if all staus is sunk, if yes say they won else 1 to continue or 0 to quit
  #player.getBoard("target")
  #manual

def userTurn(player, computer): # change target board
  
  #reference user target board and com game board
  #print both user boards
  player.getBoard("both")
  player.getBoatInfo()
  menu.turnMenu(player, computer)
  # # computer.getBoard("game")
  # print("\nTurn menu:\n1. Torpedo (manual launch)\n2. Torpedo (auto launch)")
  # choice = input()


  


  
  # if (choice == "1"):
  #   state = False
  #   while (state == False):
  #     x, y = placeShips.PlaceShips.getCoordinates(player.gameBoard) # change x to index
  #     state = checkState(player.targetBoard, x, y)
  #   y = int(y)
  #   x = placeShips.PlaceShips.getXIndex(player.gameBoard, x)
  #   if (computer.gameBoard[y][x] == "0" or computer.gameBoard[y][x] == 0):
  #     player.miss += 1
  #     player.targetBoard[y][x] = "X"
  #     print("miss")
  #   else:
  #     print("hit")
  #     player.targetBoard[y][x] = "H"
  #     player.hit += 1
  #     id = computer.gameBoard[y][x]
  #     for i in range(len(computer.boats)):
  #       if (computer.boats[i][0] == id):
  #         computer.boats[i][3] += 1
  #         if (computer.boats[i][3] == computer.boats[i][2]):
  #           print("ship sunk")
  #           computer.boats[i][4] = 2
  #   gameover = True
  #   for i in range(1, len(computer.boats)):
  #     if (computer.boats[i][4] != 2):
  #       gameover = False
  #   if (gameover):
  #     print("Player wins")
  #     state = True
  #   else:
  #     input("Press enter to continue to next players turn")
  #     state = True
  #   #get user coords, check target board 0, if all valid check opponent game board - if not 0 increment hit else increment miss
  #   #using ID add one to damage in com boat info, check if damage = length, if yes change status to sunk and print boat sunk
  #   #check if all staus is sunk, if yes say they won else 1 to continue or 0 to quit
  #   player.getBoard("target")
  #   #manual
  # elif (choice == "2"):
  #   #auto gen coords and same as above
  #   autoFunctions.autoLaunch(player, computer)
  # #turn = False
  #   #auto

def comTurn(com, player):
  com.getBoard("both")
  com.getBoatInfo()
  autoFunctions.autoLaunch(com, player)
  #same as autogen above