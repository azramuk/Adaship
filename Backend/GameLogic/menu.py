import Backend.GameConfig.adaship as adaship
import Backend.GameConfig.playerConfig as playerConfig
import Backend.GameLogic.placeShips as placeShips
import UI.showInfo as showInfo
import sys
import os
import Backend.GameLogic.attackFunctions as attackFunctions


def menu(): #call this first
  validChoice = False
  print ("Menu: \n 1. Player vs Computer \n 2. Two player game \n 3. Player vs Computer (Salvo version) \n 4. Two player game (Salvo version) \n 0. Quit \n\nEnter choice: ")
  while (validChoice == False):
    try:
      choice=int(input())
    except ValueError:
      print("\nEnter a valid choice\n")
      continue
  
    if (choice == 1):
      validChoice = True
      adaship.AdashipSettings()
      playerConfig.GameTypes.playerVsCom()
    elif (choice == 2):
      validChoice = True
      adaship.AdashipSettings()
      playerConfig.GameTypes.playerVsPlayer()
    elif (choice == 3):
      validChoice = True
      adaship.AdashipSettings()
      playerConfig.GameTypes.salvoPlayerVsCom()
    elif (choice == 4):
      validChoice = True
      adaship.AdashipSettings()
      playerConfig.GameTypes.salvoPlayerVsPlayer()
    elif (choice == 0):
      validChoice = True
      print("Exiting... goodbye!")
      sys.exit()
    else:
      print("\nEnter a valid choice\n")


def placeBoatsMenu(player):
  cont = False # 6 not chosen
  while not(placeShips.PlaceShips.allBoatsPlaced(player) and cont):
    os.system('clear')
    print(player.name, "Game Board Configuration")
    showInfo.DisplayInfo.getBoard(player, "game")
    showInfo.DisplayInfo.getBoatInfo(player)
    print("\nBoard Setup Menu\n")
    print("1. Select and Place a Ship\n2. Select and Auto-Place a Ship\n3. Auto-Place All Available Ships\n4. Auto-place All Ships\n5. Reset Board\n6. Ship Deloyments Confirmed - Select to Continue...\n\n0. Exit Setup\n\nEnter choice:")

    validChoice = False
    while (validChoice == False):
      try:
        choice = int(input())
      except ValueError:
        print("\nEnter a valid choice\n")
        continue

      if (choice == 1):
        validChoice = True
        placeShips.PlaceShips.oneShip(False, player)
      elif (choice == 2):
        validChoice = True
        placeShips.PlaceShips.oneShip(True, player)
      elif (choice == 3):
        validChoice = True
        placeShips.PlaceShips.autoPlaceAvailable(player)
      elif (choice == 4):
        validChoice = True
        placeShips.PlaceShips.autoPlaceAll(player)
      elif (choice == 5):
        validChoice = True
        placeShips.PlaceShips.resetBoard(player)
      elif (choice == 6 and placeShips.PlaceShips.allBoatsPlaced(player)):
        validChoice = True
        cont = True
      elif (choice == 0):
        validChoice = True
        sys.exit()
      elif (choice == 6 and not placeShips.PlaceShips.allBoatsPlaced(player)):
        print("\nPlace all ships before continuing\n")
      else:
        print("\nEnter a valid choice\n")


def turnMenu(player, computer):
  print("\nTurn menu:\n1. Torpedo (manual launch)\n2. Torpedo (auto launch)\n\n0. Quit\n\nEnter choice: ")
  validChoice = False
  while (validChoice == False):
    try:
      choice = int(input())
    except ValueError:
      print("\nEnter a valid choice\n")
      continue

    if (choice == 1):
      validChoice = True
      attackFunctions.Attack.takeShot(False, player, computer)
    elif (choice == 2):
      validChoice = True
      attackFunctions.Attack.takeShot(True, player, computer)
    elif (choice == 0):
      validChoice = True
      sys.exit()
    else:
      print("\nEnter a valid choice\n")
