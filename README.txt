Language: Python 3
Packages Needed:
	- numpy
	- termcolor

How to run:
    - python3 game.py

Features:
	- Different Characters have different color
	- Scoring: 
		* Kill Enemies: 100 pts
		* Destroy Bricks: 20 pts
	- There are a total of 3 lives per game
	- 3 types of enemies:
		* Enemy: Will move randomly (60%) and sometimes towards the bomberman [Red]
		* Minion: Will mostly move towards the bomberman and sometimes randomly (20%) [Yellow]
		* Boss: Will move such that it maximizes distance from bomb and minimizes distance from bomberman
		  and sometimes moves randomly (10%) [Cyan]
	- 3 types of levels:
		* Level 1: Few enemies, only sing type of enemy is present
		* Level 2: More enemies, Both Minions and Enemy are present
		* Level 3: Lots of enemies, All the types of enemies are present
	- Input timeout: If no input is given in 1 second then the input timeouts and the next frame is printed.
	- Cool ASCII Art !!!!!!!

Code Features:
    - Highly modular code (Most of the core game play elements have been separated into different modules)
    - Encapsulation (The various game play elements have been made into classes. eg Bomberman, Bomb etc and some
      methods are private)
    - Inheritance (Has been used whenever required. eg. Minion inherits from Enemy)
    - Polymorphism (eg. check_move of Entity class has been overridden by Enemy as well as Bomberman class)
    - Certain important variables have been placed in config.py and are used everywhere by importing them.
      Thus, changing values in just one place will reflect in the whole game.
    - Conforms to the PEP8 coding standards

Controls:
	- a: left
	- s: down
	- d: right
	- w: up
	- b: plant bomb
	- q: quit game