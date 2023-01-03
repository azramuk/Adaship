import Backend.GameLogic.menu as menu
import Backend.GameLogic.validation as validation
import UI.showInfo as showInfo
import os
import Backend.GameLogic.utils as utils
import UI.headers as headers


class Attack():

  def displayTurn(currentPlayer):
    os.system('clear')
    print(f"{headers.TextColours.YELLOW}".format(currentPlayer.name.strip()+"'s turn\n\n"),  f"{headers.TextColours.BOLD}".format(ind) + f"{headers.TextColours.BOLD}".format(" out of ") + f"{headers.TextColours.BOLD}".format(tries))
    showInfo.DisplayInfo.getBoard(currentPlayer, "both")
    showInfo.DisplayInfo.getBoatInfo(currentPlayer)
  
  def takeTurn(currentPlayer, nextPlayer, comTurn, salvo):
    global tries
    global ind
    ind = 1
    tries = 1 # default shots is 1 if not salvo mode
    if (salvo == True):
      tries = Attack.getTurns(currentPlayer)
    for i in range(1, tries+1):   
      Attack.displayTurn(currentPlayer)
      if (comTurn): # automatically takes shot for computer
        Attack.takeShot(True, currentPlayer, nextPlayer)
      else:
        menu.turnMenu(currentPlayer, nextPlayer) # calls menu for user taking shots
      if (Attack.checkGameOver(nextPlayer) == True):
        return True
        
      os.system('clear')
      ind+= 1
    input(f"{headers.TextColours.MAGENTA}".format("Press enter to continue to next player"))
    return False
  
  
  def takeShot(auto, player1, player2):      
    state = False
    while (state == False):
      if auto: # if the shot is automatic then it will randomly generate coordinates to guess
        x, y = utils.Utils.getRandomCoordinates(player1.gameBoard)
      else:
        x, y = utils.Utils.getCoordinates(player1.gameBoard) 
      state = validation.Validation.checkState(player1.targetBoard, x, y)
    Attack.checkShot(x, y, player1, player2)
    input(f"{headers.TextColours.MAGENTA}".format("Press enter to continue"))
  
  
  def checkShot(x, y, player1, player2):
    # checks whether shot was a hit or miss
    y = int(y)
    x = utils.Utils.getXIndex(player1.gameBoard, x)
    if (player2.gameBoard[y][x] == "0"):
      player1.miss += 1
      player1.targetBoard[y][x] = "X"
      Attack.displayTurn(player1)
      print("\nShot was a " + f"{headers.TextColours.RED}".format("MISS\n"))
    else:
      player1.targetBoard[y][x] = "H"
      Attack.displayTurn(player1)
      print("\nShot was a " + f"{headers.TextColours.GREEN}".format("HIT\n"))
      player1.hit += 1
      id = player2.gameBoard[y][x]
      for i in range(len(player2.boats)):
        if (player2.boats[i].ID == id):
          player2.boats[i].damage += 1
          # if damage is the same as length then the boat has sunk
          if (player2.boats[i].damage == player2.boats[i].length):
            name = player2.boats[i].name
            print(f"{headers.TextColours.YELLOW}".format(name.upper() + " SUNK\n"))
            player2.boats[i].status = "SUNK"

  
  def getTurns(currentPlayer):
    # calculates how many ships are not sunk for salvo mode
    tries = 0
    for i in range(len(currentPlayer.boats)):
        if (currentPlayer.boats[i].status == "DEPLOYED"):
          tries += 1
    return tries
  
  
  def checkGameOver(opp):
    #checks if any boat status is not sunk
    gameover = True
    for i in range(len(opp.boats)):
      if (opp.boats[i].status != "SUNK"):
        gameover = False
    return gameover