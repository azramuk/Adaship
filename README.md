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

// insert uml diagram
![UML1](/relative/path/to/img.jpg?raw=true "UML1")
As shown in the diagram above, the main components of this game are the boards, ships and the game play. 

My approach to this, was to work using a bottom-up design for the overall game and focused on each individual component and method before building them together. However for each component, it was more of a top-down design as I broke methods down as I went along.
I started with creating empty boards, then moved on to creating an array of boats to store all the boat information which would then be used in the boat methods. By focussing on individual methods, it allowed me to identify where code could be reused amongst different tasks so I could further break them down.

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



e. Initial object-oriented design ideas and planned phased breakdown into smaller tasks (linked to 1d).

having all validation in one class as used in multiple places
player class and computer class so computer can't use player methods
auto function class used by both player and computer
encapsulation for config file so can't be changed later on, use setters and getters for board size
making board class and boat class to keep states of each respectively 

break down by versions and then by tasks - open file, read contents, configure boards etc, worked on player workflow then computer, manual then auto, merging of reused code for auto and making com and user one class


3. Development – 15%
a. Adoption and use of ‘good’ standards (linked to 1a, 1b, 1c).

code reusability, private attributes

b. Phase 1 development: tasks, code review and changes (linked to 1d,1e).

one big file with repeated code for version 1

c. ..repeated for each development phase.

breaking into files, reusing code, merging similar classes, testing in each stage at every function implementation, unit testing then integration
version 2
version 3


d. Phase n development: tasks, code review and changes (linked to 1d,1e).

last stage code cleanup and testing

e. Ensuring quality through testing and resolving bugs (linked to 1a, 1b, 2a, 2b..2c).

repeat testing, what bugs came where and overall solution e.g taking string inputs then converting to avoid type errors

f. Reflection on key design challenges, innovations and how they were solved (with examples).

initial user and computer seperate but lots of repeated code so created a tag instead, array for boats then created objects beacause messy indexing to get attributes

3. Evaluation (academic standard: distinction level detail: section required for distinction) – 10%
a. Analysis with embedded examples of key code refactoring, reuse, smells.

adaship global variable, seperate com and player class, copying arrays not working before

b. Implementation and effective use of ‘advanced’ programming principles (with examples).

look at google classroom - reading config file singleton, states

c. Features showcase and embedded innovations (with examples) - opportunity to ‘highlight’ best bits.



d. Improved algorithms – research, design, implementation, and tested confirmation (with examples).

UI improvements? salvo version bringing num of shots so can be reused

e. Reflective review, opportunities to improve and continued professional development.