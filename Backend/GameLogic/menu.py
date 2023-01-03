import Backend.GameConfig.adaship as adaship
import Backend.GameConfig.playerConfig as playerConfig
import Backend.GameLogic.placeShips as placeShips
import UI.showInfo as showInfo
import sys
import os
import Backend.GameLogic.attackFunctions as attackFunctions
import UI.headers as headers


def menu(): #call this first
  validChoice = False
  print(f"{headers.TextColours.YELLOW}".format("Adaship\n\n"), f"{headers.TextColours.BLACK}".format("Adaship is a battleship-like game where a each user places their own ships on a grid and then guesses their opponents placement.\n If a player guesses a coordinate of the opponent’s ship, it counts as a ‘hit’. The end goal is to sink all of the opponent's ships by correctly guessing all of the coordinates on which the ships are placed. Adaship has four game modes, including a basic version where each player only gets one attack per turn, and a salvo version where each player can attack as many times as they have remaining ships per turn. Both versions can be played by one player against the computer or by two players against each other. \n\n"))
  print(f"{headers.TextColours.YELLOW}".format("Menu:\n"), "1. Player vs Computer \n 2. Two player game \n 3. Player vs Computer (Salvo version) \n 4. Two player game (Salvo version) \n 0. Quit \n\n", f"{headers.TextColours.MAGENTA}".format("Enter choice: "))
  while (validChoice == False):
    try:
      choice=int(input())
    except ValueError:
      print(f"{headers.TextColours.BG_RED}".format("\nEnter a valid choice\n"))
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
      print(f"{headers.TextColours.BOLD}".format("Exiting... goodbye!"))
      sys.exit()
    else:
      print(f"{headers.TextColours.BG_RED}".format("\nEnter a valid choice\n"))


def placeBoatsMenu(player):
  cont = False # 6 not chosen
  while not(placeShips.PlaceShips.allBoatsPlaced(player) and cont):
    os.system('clear')
    nameTitle = player.name + " Game Board Configuration"
    print(f"{headers.TextColours.YELLOW}".format(nameTitle))
    showInfo.DisplayInfo.getBoard(player, "game")
    showInfo.DisplayInfo.getBoatInfo(player)
    if not(placeShips.PlaceShips.allBoatsPlaced(player)):
      print(f"{headers.TextColours.YELLOW}".format("\nBoard Setup Menu:\n"), "1. Select and Place a Ship\n 2. Select and Auto-Place a Ship\n 3. Auto-Place All Available Ships\n 4. Auto-place All Ships\n 5. Reset Board\n", f"{headers.TextColours.BLACK}".format("6. Ship Deloyments Confirmed - Select to Continue..."), "\n\n 0. Exit Setup\n\n", f"{headers.TextColours.MAGENTA}".format("Enter choice:") )
    else:
      print(f"{headers.TextColours.YELLOW}".format("\nBoard Setup Menu:\n"), "1. Select and Place a Ship\n 2. Select and Auto-Place a Ship\n 3. Auto-Place All Available Ships\n 4. Auto-place All Ships\n 5. Reset Board\n", f"{headers.TextColours.GREEN}".format("6. Ship Deloyments Confirmed - Select to Continue..."), "\n\n 0. Exit Setup\n\n", f"{headers.TextColours.MAGENTA}".format("Enter choice:") )

    validChoice = False
    while (validChoice == False):
      try:
        choice = int(input())
      except ValueError:
        print(f"{headers.TextColours.BG_RED}".format("\nEnter a valid choice\n"))
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
        print(f"{headers.TextColours.BG_RED}".format("\nPlace all ships before continuing\n"))
      else:
        print(f"{headers.TextColours.BG_RED}".format("\nEnter a valid choice\n"))


def turnMenu(player, computer):
  print(f"{headers.TextColours.YELLOW}".format("\nTurn menu:\n"), "1. Torpedo (manual launch)\n 2. Torpedo (auto launch)\n\n 0. Quit\n\n", f"{headers.TextColours.MAGENTA}".format("Enter choice:"))
  validChoice = False
  while (validChoice == False):
    try:
      choice = int(input())
    except ValueError:
      print(f"{headers.TextColours.BG_RED}".format("\nEnter a valid choice\n"))
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
      print(f"{headers.TextColours.BG_RED}".format("\nEnter a valid choice\n"))
