import os
import Backend.GameLogic.menu as menu
import Backend.GameLogic.gamePlay as gamePlay
import Backend.GameLogic.playerInfo as playerInfo


class GameTypes():

  def __createPlayers(name1, name2):
    global player1
    global player2
    player1 = playerInfo.Player()
    player1.name = name1
    player2 = playerInfo.Player()
    player2.name = name2
    menu.placeBoatsMenu(player1)
    os.system('clear')
    # if the second player is the computer then it automatically places the ships, else calls the same user place ships function
    if player2.name == "Computer":
      playerInfo.Player.placeBoats(player2)
    else:
      menu.placeBoatsMenu(player2)
    input("\nPress enter to continue")

  
  def playerVsCom():
    GameTypes.__createPlayers("Player", "Computer")
    os.system('clear')
    gamePlay.GameLogic.game(1, False)
  
  
  def playerVsPlayer():
    GameTypes.__createPlayers("Player 1", "Player 2")
    os.system('clear')
    gamePlay.GameLogic.game(2, False)
  
  
  def salvoPlayerVsCom():
    GameTypes.__createPlayers("Player", "Computer")
    os.system('clear')
    gamePlay.GameLogic.game(1, True)
    
  
  def salvoPlayerVsPlayer():
    GameTypes.__createPlayers("Player 1", "Player 2")
    os.system('clear')
    gamePlay.GameLogic.game(2, True)