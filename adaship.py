
import os
import autoFunctions, computerConfig, computerLogic, config, menu, placeShips, playerConfig, playGame, readConfigFile, validation

# read config file, option for user input, config everything

# import configFile class - run adaship = ConfigFile() this sets all the default configs, ask if user wants to choose own board dimension? if yes then run set dimensions and pass their input
# create 4 empty boards and 2 place ships array
# automatically place computer ships and get user to place ships - call place ships()
# PLAY GAME

def Adaship():
  global adashipp
  global player1
  global computer
  gameOver = False
  adashipp = readConfigFile.ConfigFile()
  os.system('clear')
  print("Do you want to choose your own board size? y/n: ")
  valid = False
  while (not valid):
    answer = input().lower()
    if (answer == "y"):
      valid = True
      os.system('clear')
      width, height = config.GameConfig.ownBoardSize()
    elif (answer != "n"):
      print("Enter a valid choice: ")
    else:
      valid = True
      width, height = readConfigFile.ConfigFile.getDimensions(adashipp)
  adashipp.setUserDimensions(width, height)

  #playGame()
  
  player1 = playerConfig.Player()
  # player1.getBoard("target")
  # player1.getBoard("game")
  # while not all boats placed
  menu.placeBoatsMenu(player1)
  computer = computerConfig.Computer()
  os.system('clear')
  computerConfig.Computer.placeBoats(computer)
  input("\nPress enter to continue")
  os.system('clear')

  turn = player1
  while gameOver == False:
    os.system('clear')
    if turn == player1:
      print("\nPlayer 1's turn\n")
      playGame.userTurn(player1, computer)
    else:
      print("\nPlayer 2's turn\n")
      playGame.comTurn(computer, player1)
    turn = getTurn(turn)
    gameOver = checkGameOver(turn)
    #if gameover = true , if turn = player 1 then com wins else player wins
    if (gameOver == True):
      if (turn == player1):
        print("Computer wins")
      else:
        print("Player wins")
    
    
  # playGame.userTurn(player1, computer)
  # playGame.comTurn(computer, player1)
  #while not game over get turn, depending on turn pass functions

def getTurn(turn):
  if turn == player1:
    turn = computer
  else:
    turn = player1
  return turn


def checkGameOver(opp):
  gameover = True
  for i in range(1, len(opp.boats)):
    if (opp.boats[i][4] != 2):
      gameover = False
  return gameover
    