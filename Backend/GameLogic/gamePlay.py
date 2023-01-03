import os
import Backend.GameConfig.playerConfig as playerConfig
import Backend.GameLogic.attackFunctions as attackFunctions
import UI.headers as headers


class GameLogic():
  
  def game(oneOrTwo, salvo):
    #Each game uses this method with settings for whether it is one or two player or salvo mode or not
    gameOver = False
    turn = playerConfig.player1
    comTurn = False
    while gameOver == False:
      os.system('clear')
      if turn == playerConfig.player1: # if statements works out which player's turn it is in order to decide how to pass the player order
        gameOver = attackFunctions.Attack.takeTurn(playerConfig.player1, playerConfig.player2, comTurn, salvo)
      else:
        gameOver =  attackFunctions.Attack.takeTurn(playerConfig.player2, playerConfig.player1, comTurn, salvo)
        
      turn = GameLogic.__getTurn(turn) 
      if (oneOrTwo == 1):
        comTurn = GameLogic.__switchCom(comTurn) 
  
      if (gameOver == True):
        if (turn == playerConfig.player1):
          print(f"{headers.TextColours.GREEN}".format(playerConfig.player2.name + " wins"))
        else:
          print(f"{headers.TextColours.GREEN}".format(playerConfig.player1.name + " wins"))

  
  def __switchCom(comTurn):
    # if one player game, switches comTurn to decide whether it is the computer's turn or not
    if comTurn == True:
      comTurn = False
    else:
      comTurn = True
    return comTurn

  
  def __getTurn(turn):
    # swaps player turns
    if turn == playerConfig.player1:
      turn = playerConfig.player2
    else:
      turn = playerConfig.player1
    return turn
  
  
