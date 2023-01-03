import Backend.GameLogic.menu as menu
import UI.headers as headers
import os
# Game starts by calling menu

again = True
while again == True:
  menu.menu()
  valid = False
  answer = input(f"{headers.TextColours.MAGENTA}".format("Would you like to play again? (y/n): ")).upper()
  while valid == False:
    if answer == "Y":
      valid = True
      os.system('clear')
    elif answer == "N":
      valid = True
      again = False
      print("Goodbye...")
    else: 
      answer = input(f"{headers.TextColours.BG_RED}".format("Please enter valid choice: ")).upper()