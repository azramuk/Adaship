
import os
import autoFunctions, computerConfig, computerLogic, config, menu, placeShips, playerConfig, playGame, readConfigFile, validation

# Configures everything together 
def Adaship():
  global adashipp
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
  #stop here
  
    
  

def getTurn(turn):
  if turn == player1:
    turn = player2
  else:
    turn = player1
  return turn


def checkGameOver(opp):
  gameover = True
  for i in range(1, len(opp.boats)):
    if (opp.boats[i][4] != 2):
      gameover = False
  return gameover




def playerVsCom():
  global player1
  global computer
  gameOver = False
  player1 = playerConfig.Player()
  computer = computerConfig.Computer()
  
  menu.placeBoatsMenu(player1)
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
    if (gameOver == True):
      if (turn == player1):
        print("Computer wins")
      else:
        print("Player wins")



def playerVsPlayer():
  global player1
  global player2
  gameOver = False
  player1 = playerConfig.Player()
  player2 = playerConfig.Player()
  
  menu.placeBoatsMenu(player1)
  os.system('clear')
  menu.placeBoatsMenu(player2)

  input("\nPress enter to continue")
  os.system('clear')
  
  turn = player1
  while gameOver == False:
    os.system('clear')
    if turn == player1:
      print("\nPlayer 1's turn\n")
      playGame.userTurn(player1, player2)
    else:
      print("\nPlayer 2's turn\n")
      playGame.userTurn(player2, player1)
      
    turn = getTurn(turn)
    gameOver = checkGameOver(turn)
    if (gameOver == True):
      if (turn == player1):
        print("Player 2 wins")
      else:
        print("Player 1 wins")