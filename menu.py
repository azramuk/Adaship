import autoFunctions, computerConfig, computerLogic, config, placeShips, playerConfig, playGame, readConfigFile, validation, adaship
import sys
import os

def menu(): #call this first
  validChoice = False
  print ("Menu: \n 1. Player vs Computer \n 2. Two player game \n 3. Player vs Computer (Salvo version) \n 4. Two player game (Salvo version) \n 0. Quit \n\nEnter choice: ")
  while (validChoice == False):
    #choice = input()
    try:
      choice=int(input())
    except ValueError:
      print("\nEnter a valid choice\n")
      continue
  
    if (choice == 1):
      validChoice = True
      adaship.Adaship()
      adaship.playerVsCom()
    elif (choice == 2):
      validChoice = True
      adaship.Adaship()
      adaship.playerVsPlayer()
    elif (choice == 3):
      print("one player salvo")
    elif (choice == 4):
      print("two player salvo")
    elif (choice == 0):
      validChoice = True
      print("Exiting... goodbye!")
      sys.exit()
    else:
      print("\nEnter a valid choice\n")






def placeBoatsMenu(player):
  #while not all boats placed and 6 hasn't been pressed
  cont = False#??
  while not(placeShips.allBoatsPlaced(player) and cont):
    # Clearing the Screen
    os.system('clear')
    cont = False
    player.getBoard("game")
    player.getBoatInfo()
    print("\nBoard Setup Menu\n")
    print("1. Select and Place a Ship\n2. Select and Auto-Place a Ship\n3. Auto-Place All Available Ships\n4. Auto-place All Ships\n5. Reset Board\n6. Ship Deloyments Confirmed - Select to Continue...\n\n0. Exit Setup\n\nEnter choice:")

    validChoice = False
    while (validChoice == False):
      try:
        choice = int(input())
      except ValueError:
        print("\nEnter a valid choice\n")
        continue

    #player.getBoard("game")
     # error catch no input
      if (choice == 1):
        validChoice = True
        placeShips.userPlaceShip(player)
      elif (choice == 2):
        validChoice = True
        placeShips.userAutoPlace(player)
      elif (choice == 3):
        validChoice = True
        placeShips.autoPlaceAvailable(player)
      elif (choice == 4):
        validChoice = True
        placeShips.autoPlaceAll(player)
      elif (choice == 5):
        validChoice = True
        placeShips.resetBoard(player)
      elif (choice == 6 and placeShips.allBoatsPlaced(player)):
        validChoice = True
        cont = True
      elif (choice == 0):
        validChoice = True
        sys.exit()
      elif (choice == 6 and not placeShips.allBoatsPlaced(player)):
        print("\nPlace all ships before continuing\n")
      else:
        print("\nEnter a valid choice\n")



def turnMenu(player, computer):
  print("\nTurn menu:\n1. Torpedo (manual launch)\n2. Torpedo (auto launch)\n\nEnter choice: ")
  validChoice = False
  while (validChoice == False):
    try:
      choice = int(input())
    except ValueError:
      print("\nEnter a valid choice\n")
      continue

    if (choice == 1):
      validChoice = True
      playGame.manualLaunch(player, computer)
    elif (choice == 2):
      #auto gen coords and same as above
      validChoice = True
      autoFunctions.autoLaunch(player, computer)
    #turn = False
      #auto
    else:
      print("\nEnter a valid choice\n")
