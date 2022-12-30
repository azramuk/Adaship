import computerConfig, computerLogic, config, menu, placeShips, playerConfig, playGame, readConfigFile, validation, adaship

def autoLaunch(player, computer): # change target board
    state = False
    while (state == False):
      x, y = placeShips.PlaceShips.getRandomCoordinates(player.gameBoard) # get auto coords
      state = playGame.checkState(player.targetBoard, x, y)
    y = int(y)
    x = placeShips.PlaceShips.getXIndex(player.gameBoard, x)
    if (computer.gameBoard[y][x] == "0" or computer.gameBoard[y][x] == 0):
      player.targetBoard[y][x] = "X"
      player.miss += 1
      print("\nShot was a MISS\n")
    else:
      print("\nShot was a HIT\n")
      player.hit += 1
      player.targetBoard[y][x] = "H"
      id = computer.gameBoard[y][x]
      for i in range(len(computer.boats)):
        if (computer.boats[i][0] == id):
          computer.boats[i][3] += 1
          if (computer.boats[i][3] == computer.boats[i][2]):
            print("SHIP SUNK\n")
            computer.boats[i][4] = 2
    gameover = True
    for i in range(len(computer.boats)):
      if (computer.boats[i][4] != 2):
        gameover = False
    if (gameover):
      print("\nPlayer wins\n")
    else:
      input("Press enter to continue to next players turn")