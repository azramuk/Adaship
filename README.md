# Adaship

### To run:

Head to https://replit.com/github to import a repository.
In the 'github url' use: `github.com/azramuk/Adaship` then click on 'import from github'
Once imported, hit 'run' at the top and play Adaship in the console window.

## Challenge Outline
Adaship is a Battleship-like game, which consists two players who each place their ships on their own boards, and then attacks the opponent by guessing coordinates on the opponents board. If they guess a coordinate that the opponent has a ship placed on then they get a 'hit' on the ship. The aim of the game is to sink all of the opponents ships by guessing all coordinates that the ships are placed on.

Adaship had a few variations including the basic game of one attack per turn (1 player vs computer or 2 players), and the salvo variation which is where each player would get as many attacks as their own ships that are not sunk per turn (1 player vs computer or 2 players).

For the overall solution, it has been broken down into the main components of the game:
- Start menu (pick game version)
- Create boards
- Place ships
- Attack opponent
  - Register hit/miss
  - update ship status
- Check game over


#### Overall Solution
![UML1](/UML1.drawio.png "UML1")
<br />

As shown in the diagram above, the main components of this game are the boards, ships and the game play. This was how I broke the game down initially in terms of what to focus development on. My overall approach was therefore a bottom-up design since I focused on building each component and methods before building all the main objects together. However, for each object, I used more of a top-down approach as I took the overall object and slowly broke it down into methods and classes as I went along. In terms of my approach to quality, I refactored code after getting the logic to work, by identifying repeated parts of code and breaking them into reusable functions.

The overall problem was decomposed into singular stages that would happen in a sequence which is how I created my 'epic' style task as listed below.

The most difficult thing about creating 'epic' style tasks was the fact that some tasks overlapped with others if they were too vague. For example user placing boats overlapped with computer placing boats as it could just reuse the auto place all boats function.

### Decomposition of tasks:
- Read and store information from the config file
- Allow user to choose board size
- Create 4 empty boards
- Create array with boat information per player
- Place ships
  - Vertical / horizontal placements of ships
  - Manually choose ship coordinates
  - Automatically place ship
  - Automatically place remaining ships
  - Place all ships
  - Reset board
- Validation
  - Coordinate validation
  - Space on board validation
  - Board state validation (are there boats already on board)
- Guessing coordinates
- Changing board states
- Changing boat states
- Turn style play
- Identifying game over



### Initial object-oriented design ideas and planned phased breakdown into smaller tasks

Initially I decided on having classes for methods that would be related to each stage in the game. For example:

- Having a class for methods to do with placing ships on the board. 
- Having all validation in one class as used in multiple places
- Seperate player and computer class
- Automatic functions
- Encapsulation for reading the configuration file
  - Use setters and getters
- Board and boat classes

To break it into smaller tasks, I decided to work on game methods by versions of the game and then by tasks. I worked on the player workflow first and then the computer workflow, same with working on manual (user input) functions before automatic ones, and adding validation after.



## Development

When developing my code, I tried to adopt some good practices. For example, I used private attributes in classes where the value should not change at all during the game, such as board dimensions,  as it ensures better security so that they use getters and setters to ensure the variables cannot be edited directly which would then skip validation. I also resued lots of my code throughout to avoid repeating code. This means that overall it would be quicker to compile the code and easier to read and understand. I also used good naming conventions so that functions and variables were easily understood as to what they are for.

### Phase 1 - Reading Config File
In phase 1 I read the .ini configuration file, and structured it into board and boat information. It was also in this phase that I decided to code within a single file before splitting into seperate ones.

I decided to use a singleton method so the file can only be read once and information on the boats and board can't be changed as it's important that this is constant when creating the user and computer components. Once this function was fully coded, I did unit testing to ensure that it worked as a singleton method and that attributes couldn't be changed once set.

### Phase 2 - Configuring Classes and Objects
In phase 2, I added in configuration of boards and players. Players inherited the creation of boards as it was used for their attributes of game and target boards. Players also inherited the boats class by having an array of boat objects.
Initially, I was going to have a seperate class for players and computers, however the classes were very similar so I merged them into one which allowed me to use abstraction.

I started by working on creating game boards using 2D arrays. Initially I tried to use `board = [[0]*height]*width`, passing through the values for height and width, but after testing the creation of 4 boards with this method I realised I would need to use `deepcopy` to individually manipulate each board since I would need 4 overall.

### Phase 3 - Placing Ships
In phase 3 I focused on configuring the game boards with ship placement. I focused on the user placement of ships first as I knew I would be able to reuse the code for automatically placing all the ships when configuring for the computer, automatic ship placement. I made a new class with different methods of placing the ships according to the menu options. I also ensured that each method had a single function by breaking out asking for user inputs into multiple functions. It was here that I identified the reusability of some of the functions such as getting user inputs for coordinates.
I also added in validation checks for user input here which was a seperate class too as I would be using this in multiple places and so followed the practice of encapsulation.
I asked for user coordinates of X and Y seperately, however on hindsight I could have used regex to get coordinates as one.

### Phase 4 - Guessing Opponent's Ships
Phase 4 consisted of taking shots and returning whether it was a hit or miss. Again for this, I focused on the user options first as the Computer would be reusing the automatic function. I first focused on the functionality before the concept of taking and switching turns. One thing I found was an obstacle was identifying if the turn was the computers or if it was a player. To overcome this, I added a name attribute to the player class so that it would be easy to identify. I tested each function of placing ships with edge cases and wrong input. I found that for auto placing, there may be only one orientation that would work at times and so I added checks which helped cut down the time to find where the space on the board is instead of continuously generating a new orientation and coordinates.
I was able to reuse validation from placing ships here for the guesses.

### Phase 5 - Major Code Refactor
After having the logistics of the game working, I decided to refactor my code and break it into modules, folders and refine classes and methods. I aimed to make my code better by finding more places to reduce repetition of code which was mainly through breaking functions down even further.

### Phase 6 - Salvo Mode
The main differences that I focused on in this mode was the loop of guesses for the ships that had not been sunk per player but overall it was reusing and calling the same code of attacks from before. 

### Phase 7 - UI changes
The final phase was changing the UI display to make the user experience better through using different colours so results and prompts are clearer on a screen full of text and easier to identify.

### Testing and resolving bugs
In terms of testing, I tested each individual function when completing the code of it and also after every refactor in case it could have broke. This would be considered as unit testing and whenever I tested it, I was testing the functions to try and break them. By doing this testing regularly, it allowed me to catch bugs early on before making big issues. I also used print statements quite a lot throughout code to find where code might break so I could identify the function when using integration testing and testing the project as a whole. I also asked others to play the game and try to break it in case I missed any cases of testing. In order to minimise errors from user input, I used guard clauses for things such as taking input as integers.

### Reflection on key design challenges
- boards not using deepcopy
- boats as array initially
- display of boards when implementing colours - would format each row then print the row but I needed to add white space borders and check each cell to decide on colour
- placing ships - overlapping


## Evaluation

Below is an example of how I refactored my code from having a seperate class for Player and Computer, and how I refactored it to use the same structure. I also seperated out the UI methods which were also reused in each class initially, so that the class methods were more specialised to the object.

```
# COMPUTER CLASS

class Computer():
  def __init__(self):
    self.targetBoard = config.GameConfig.createBoard()
    self.gameBoard = config.GameConfig.createBoard()
    self.hit = 0
    self.miss = 0
    self.boats = config.GameConfig.boatsArray()

  def placeBoats(self):
    placeShips.autoPlaceAll(self)
    print("\nComputer Game Board: \n")
    s = [[str(e) for e in row] for row in self.gameBoard]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))
    Computer.getBoatInfo(self)

  def getBoard(self, boardType):
    if boardType == "target":
      print("\nTarget Board: \n")
      s = [[str(e) for e in row] for row in self.targetBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))
      #print(np.matrix(self.targetBoard))
    elif boardType == "game":
      print("\nGame Board: \n")
      s = [[str(e) for e in row] for row in self.gameBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))
      #print(np.matrix(self.gameBoard))
    elif boardType == "both":
      print("\nTarget Board: \n")
      s = [[str(e) for e in row] for row in self.targetBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))

      print("\nGame Board: \n")
      s = [[str(e) for e in row] for row in self.gameBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))

  def getBoatInfo(self):
    print("\nBoat Info: \n")
    s = [[str(e) for e in row] for row in self.boats]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))


  # USER CLASS
  
  class Player():
  def __init__(self):
    self.targetBoard = config.GameConfig.createBoard()
    self.gameBoard = config.GameConfig.createBoard()
    self.hit = 0
    self.miss = 0
    self.boats = config.GameConfig.boatsArray()

  def getBoard(self, boardType):
    if boardType == "target":
      print("\nTarget Board: \n")
      s = [[str(e) for e in row] for row in self.targetBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))
      #print(np.matrix(self.targetBoard))
    elif boardType == "game":
      print("\nGame Board: \n")
      s = [[str(e) for e in row] for row in self.gameBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))
      #print(np.matrix(self.gameBoard))
    elif boardType == "both":
      print("\nTarget Board: \n")
      s = [[str(e) for e in row] for row in self.targetBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))

      print("\nGame Board: \n")
      s = [[str(e) for e in row] for row in self.gameBoard]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))

  def getBoatInfo(self):
      print("\nBoat Info: \n")
      s = [[str(e) for e in row] for row in self.boats]
      lens = [max(map(len, col)) for col in zip(*s)]
      fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
      table = [fmt.format(*row) for row in s]
      print ('\n'.join(table))
```
Changed to:
```
class Player():
  def __init__(self):
    self.name = ""
    self.targetBoard = boardBoatConfig.GameConfig.createBoard()
    self.gameBoard = boardBoatConfig.GameConfig.createBoard()
    self.hit = 0
    self.miss = 0
    self.boats = boardBoatConfig.GameConfig.boatsArray()

  
  def placeBoats(self):
    # method for computer placing ships
    placeShips.PlaceShips.autoPlaceAll(self)
    print(f"{headers.TextColours.YELLOW}".format("Computer Game Board Configuration"))
    showInfo.DisplayInfo.getBoard(self, "game")
    showInfo.DisplayInfo.getBoatInfo(self)
```

Another bit of code that I heavily refactored, was the fact that I initially was storing boat information in an array of arrays and accessed the informationm through indexing, but instead changed it to an array of boat objects so that I oculd access the attributes with names which made my code clearer as shown below.
```
...
def boatsArray():
    NOT_DEPLOYED = 0;
    boats = readConfigFile.ConfigFile.getBoats(adaship.adashipp)

    for i in range(len(boats)):
      boats[i].insert(0, boats[i][0][0])
      boats[i].append(0)
      boats[i].append(NOT_DEPLOYED)
    boats.insert(0, ["ID", "Name", "Length", "Damage", "Status"])
    return boats
```
Changed to:
```
def boatsArray():
    boats = readConfigFile.ConfigFile.getBoats(adaship.adaship)
    boatsList = []
    
    for i in range(len(boats)):
      boatsList.append(boatInfo.Boat(boats[i][0][0],boats[i][0],boats[i][1])) # array of boat objects
      
    return boatsList
```
Where the `Boat` object is:
```
class Boat():
  def __init__(self, ID, name, length):
    self.ID = ID
    self.name = name
    self.length = length
    self.damage = 0
    self.status = "NOT DEPLOYED"
```

I used some 'advanced' programming principles throughout my code for example, below is how I used a singleton method for reading the config file so that it could not be changed later. This meant the the base game attributes for configuration wuld have the same attributes all the way through. I also made use of private attrubutes which can be identified by the two underscores: `__`
```
class ConfigFile():
  def __init__(self):
    self.__file = None
    self.__width=0  # private instance attribute
    self.__height=0 # private instance attribute - can only be changed from class function 'setUserDimensions'
    self.__boats=[]
    self.readConfigFile() #automatically sets based on file


  #only opens and reads file once as controlled by None check making this a singleton function
  def readConfigFile(self):
    if self.__file is None:
      f = open("adaship_config.ini", "r")
      self.__file = f.readlines()
    count = 0

    for line in self.__file:
      count += 1
      type = ""
      i = 0
      while (i < len(line) and line[i] != ":"):
        type = type + line[i].lower()
        i += 1
    
      if (type == "board"):
        dimensions = line[i+1:].strip()
        width = int(dimensions.split("x")[0])
        height = int(dimensions.split("x")[1])
        # store width and height as attribute
        self.__width = width
        self.__height = height
      elif (type == "boat"):
        # add each identification of a boat to an array
        boat = line[i+1:].strip().split(",")
        boat[-1] = int(boat[-1])
        self.__boats.append(boat)
```

Another advanced programming principle I made use of was encapsulation which was showcased through various classes. Each class had specific methods and attributes that were only used in those classes for example the `PlaceShips()` class which is shown in ![placeShips](/Backend/GameLogic/placeShips.py "placeShips") as well as a snapshot below:
```
class PlaceShips():

  def placeShip(auto, player, boatLen, boatID):
    validRange = False
    validState = False
    while (validRange == False or validState == False):
      if auto:
        # if automatically placing ship gets random coordinates and orientation
        orientation = utils.Utils.getRandomOrientation()
        if (orientation == "V"):
          #check if space to place vertically
          space = validation.Validation.VerSpace(player.gameBoard, boatLen)
          if space == False:
            orientation = "H"
        else:
          #check if space to place horizontally
          space = validation.Validation.HorSpace(player.gameBoard, boatLen)
          if space == False:
            orientation = "V"
        x, y = utils.Utils.getRandomCoordinates(player.gameBoard)
      else:
        # get user inputs
        orientation = utils.Utils.getOrientation()
        x, y = utils.Utils.getCoordinates(player.gameBoard)
      validRange = validation.Validation.checkBoardRange(player.gameBoard, x, y, orientation, boatLen)    
      
      if (validRange):
          validState = validation.Validation.checkBoardState(player.gameBoard, x, y, orientation, boatLen)
          if (validState):
            #if everything is valid then place the ship
            player.gameBoard = PlaceShips.place(player.gameBoard, x, y, orientation, boatLen, boatID)
            

  def oneShip(auto, player):
    #if only one ship being placed, don't need a for loop
    os.system('clear')
    showInfo.DisplayInfo.getBoard(player, "game")
    boat = PlaceShips.getUserBoat(player)
    boatLen = boat.length
    boatID = boat.ID
    boatStatus = boat.status
    if (boatStatus == "DEPLOYED"):
      PlaceShips.removeShip(player.gameBoard, boatID)
    PlaceShips.placeShip(auto, player, boatLen, boatID)
    boat.status = "DEPLOYED"
    
    
  def autoPlaceAvailable(player):
    for i in range(len(player.boats)):
      boat = player.boats[i]
      if (boat.status == "NOT DEPLOYED"):
        # checks whether ship is not already placed
        boatLen = boat.length
        boatID = boat.ID
        PlaceShips.placeShip(True, player, boatLen, boatID)
        boat.status = "DEPLOYED"

  
  def autoPlaceAll(player):
    # places all ships regardless of already placed so clears board and status
    PlaceShips.resetBoard(player)
    for i in range(len(player.boats)):
      boat = player.boats[i]
      boatLen = boat.length
      boatID = boat.ID
      
      PlaceShips.placeShip(True, player, boatLen, boatID)
      boat.status = "DEPLOYED"
      ...
```
I used the concept of encapsulation in various places as well as modularisation since I grouped my modules by UI and Service although I think I could have made better use of it with UI formatting as some UI prompts were in Service files.
<br />
My best feature in my project was the use of a seperate boat class that encapsulated the attributes per boat:
```
class Boat():
  def __init__(self, ID, name, length):
    self.ID = ID
    self.name = name
    self.length = length
    self.damage = 0
    self.status = "NOT DEPLOYED"
```
It allowed my code to be cleaner and more understandable throughout when accessing different attributes of the boat. It was also my best improved algorith and made the overall design of my project much cleaner.

The improved design with the UI in the final stages really impacted the overall project in a positive light as the improved user experience made the overall project more user-friendly.

I learned a lot throughout this project even up until my review of my own code as one thing that I have reflected on which I wish I could have done better was:
- The use of regex for coordinate input instead of seperate inputs for the X and Y coordinates
- Exception handling for invalid input through better and more thorough unit testing instead of just console input
- Attempting the mines version if I didn't have the time constraint or looking at the overall solution from a more top-down perspective to incorporate it
- Use of polymorphism for cleaner code as I didn't attempt to use it