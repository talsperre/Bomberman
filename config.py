COLUMNS = 20    # No of columns in board
ROWS = 20   # No of rows in board
PERCENT_BOXES = 0.05    # Percentage of boxes in the board
# For different levels percentage of enemies in board is represented by this constant
PERCENT_ENEMIES = {
    1: 0.06,
    2: 0.07,
    3: 0.08,
}
EXPLODE_TIME = 2    # Time taken for the bomb to explode

WIN = """
	                     .----------------.  .----------------.  .----------------.                     
	                    | .--------------. || .--------------. || .--------------. |                    
	                    | |  ____  ____  | || |     ____     | || | _____  _____ | |                    
	                    | | |_  _||_  _| | || |   .'    `.   | || ||_   _||_   _|| |                    
	                    | |   \ \  / /   | || |  /  .--.  \  | || |  | |    | |  | |                    
	                    | |    \ \/ /    | || |  | |    | |  | || |  | '    ' |  | |                    
	                    | |    _|  |_    | || |  \  `--'  /  | || |   \ `--' /   | |                    
	                    | |   |______|   | || |   `.____.'   | || |    `.__.'    | |                    
	                    | |              | || |              | || |              | |                    
	                    | '--------------' || '--------------' || '--------------' |                    
	                     '----------------'  '----------------'  '----------------'                     
	 .----------------.  .----------------.  .-----------------. .----------------.  .----------------. 
	| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
	| | _____  _____ | || |     _____    | || | ____  _____  | || |              | || |              | |
	| ||_   _||_   _|| || |    |_   _|   | || ||_   \|_   _| | || |      _       | || |      _       | |
	| |  | | /\ | |  | || |      | |     | || |  |   \ | |   | || |     | |      | || |     | |      | |
	| |  | |/  \| |  | || |      | |     | || |  | |\ \| |   | || |     | |      | || |     | |      | |
	| |  |   /\   |  | || |     _| |_    | || | _| |_\   |_  | || |     | |      | || |     | |      | |
	| |  |__/  \__|  | || |    |_____|   | || ||_____|\____| | || |     |_|      | || |     |_|      | |
	| |              | || |              | || |              | || |     (_)      | || |     (_)      | |
	| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
	 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

"""

LIVES_1 = """
            .----------------.  .----------------.  .----------------.  .----------------.  .----------------.            
           | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |           
           | |   _____      | || |     _____    | || | ____   ____  | || |  _________   | || |    _______   | |           
           | |  |_   _|     | || |    |_   _|   | || ||_  _| |_  _| | || | |_   ___  |  | || |   /  ___  |  | |           
           | |    | |       | || |      | |     | || |  \ \   / /   | || |   | |_  \_|  | || |  |  (__ \_|  | |           
           | |    | |   _   | || |      | |     | || |   \ \ / /    | || |   |  _|  _   | || |   '.___`-.   | |           
           | |   _| |__/ |  | || |     _| |_    | || |    \ ' /     | || |  _| |___/ |  | || |  |`\____) |  | |           
           | |  |________|  | || |    |_____|   | || |     \_/      | || | |_________|  | || |  |_______.'  | |           
           | |              | || |              | || |              | || |              | || |              | |           
           | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |           
            '----------------'  '----------------'  '----------------'  '----------------'  '----------------'            
 .----------------.  .----------------.  .----------------.  .----------------.   .----------------.   .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. | | .--------------. |
| |   _____      | || |  _________   | || |  _________   | || |  _________   | | | |              | | | |     __       | |
| |  |_   _|     | || | |_   ___  |  | || | |_   ___  |  | || | |  _   _  |  | | | |      _       | | | |    /  |      | |
| |    | |       | || |   | |_  \_|  | || |   | |_  \_|  | || | |_/ | | \_|  | | | |     (_)      | | | |    `| |      | |
| |    | |   _   | || |   |  _|  _   | || |   |  _|      | || |     | |      | | | |      _       | | | |     | |      | |
| |   _| |__/ |  | || |  _| |___/ |  | || |  _| |_       | || |    _| |_     | | | |     (_)      | | | |    _| |_     | |
| |  |________|  | || | |_________|  | || | |_____|      | || |   |_____|    | | | |              | | | |   |_____|    | |
| |              | || |              | || |              | || |              | | | |              | | | |              | |
| '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' | | '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'   '----------------'   '----------------' 
"""

LIVES_2 = """
            .----------------.  .----------------.  .----------------.  .----------------.  .----------------.            
           | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |           
           | |   _____      | || |     _____    | || | ____   ____  | || |  _________   | || |    _______   | |           
           | |  |_   _|     | || |    |_   _|   | || ||_  _| |_  _| | || | |_   ___  |  | || |   /  ___  |  | |           
           | |    | |       | || |      | |     | || |  \ \   / /   | || |   | |_  \_|  | || |  |  (__ \_|  | |           
           | |    | |   _   | || |      | |     | || |   \ \ / /    | || |   |  _|  _   | || |   '.___`-.   | |           
           | |   _| |__/ |  | || |     _| |_    | || |    \ ' /     | || |  _| |___/ |  | || |  |`\____) |  | |           
           | |  |________|  | || |    |_____|   | || |     \_/      | || | |_________|  | || |  |_______.'  | |           
           | |              | || |              | || |              | || |              | || |              | |           
           | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |           
            '----------------'  '----------------'  '----------------'  '----------------'  '----------------'            
 .----------------.  .----------------.  .----------------.  .----------------.   .----------------.   .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. | | .--------------. |
| |   _____      | || |  _________   | || |  _________   | || |  _________   | | | |              | | | |    _____     | |
| |  |_   _|     | || | |_   ___  |  | || | |_   ___  |  | || | |  _   _  |  | | | |      _       | | | |   / ___ `.   | |
| |    | |       | || |   | |_  \_|  | || |   | |_  \_|  | || | |_/ | | \_|  | | | |     (_)      | | | |  |_/___) |   | |
| |    | |   _   | || |   |  _|  _   | || |   |  _|      | || |     | |      | | | |      _       | | | |   .'____.'   | |
| |   _| |__/ |  | || |  _| |___/ |  | || |  _| |_       | || |    _| |_     | | | |     (_)      | | | |  / /____     | |
| |  |________|  | || | |_________|  | || | |_____|      | || |   |_____|    | | | |              | | | |  |_______|   | |
| |              | || |              | || |              | || |              | | | |              | | | |              | |
| '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' | | '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'   '----------------'   '----------------' 
"""

GAME_OVER = """
                     .----------------.  .----------------.  .----------------.  .----------------.                     
                    | .--------------. || .--------------. || .--------------. || .--------------. |                    
                    | |    ______    | || |      __      | || | ____    ____ | || |  _________   | |                    
                    | |  .' ___  |   | || |     /  \     | || ||_   \  /   _|| || | |_   ___  |  | |                    
                    | | / .'   \_|   | || |    / /\ \    | || |  |   \/   |  | || |   | |_  \_|  | |                    
                    | | | |    ____  | || |   / ____ \   | || |  | |\  /| |  | || |   |  _|  _   | |                    
                    | | \ `.___]  _| | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___/ |  | |                    
                    | |  `._____.'   | || ||____|  |____|| || ||_____||_____|| || | |_________|  | |                    
                    | |              | || |              | || |              | || |              | |                    
                    | '--------------' || '--------------' || '--------------' || '--------------' |                    
                     '----------------'  '----------------'  '----------------'  '----------------'                     
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ____     | || | ____   ____  | || |  _________   | || |  _______     | || |              | || |              | |
| |   .'    `.   | || ||_  _| |_  _| | || | |_   ___  |  | || | |_   __ \    | || |      _       | || |      _       | |
| |  /  .--.  \  | || |  \ \   / /   | || |   | |_  \_|  | || |   | |__) |   | || |     | |      | || |     | |      | |
| |  | |    | |  | || |   \ \ / /    | || |   |  _|  _   | || |   |  __ /    | || |     | |      | || |     | |      | |
| |  \  `--'  /  | || |    \ ' /     | || |  _| |___/ |  | || |  _| |  \ \_  | || |     | |      | || |     | |      | |
| |   `.____.'   | || |     \_/      | || | |_________|  | || | |____| |___| | || |     |_|      | || |     |_|      | |
| |              | || |              | || |              | || |              | || |     (_)      | || |     (_)      | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
"""

LEVEL_2 = """
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |   _____      | || |  _________   | || | ____   ____  | || |  _________   | || |   _____      | |
| |  |_   _|     | || | |_   ___  |  | || ||_  _| |_  _| | || | |_   ___  |  | || |  |_   _|     | |
| |    | |       | || |   | |_  \_|  | || |  \ \   / /   | || |   | |_  \_|  | || |    | |       | |
| |    | |   _   | || |   |  _|  _   | || |   \ \ / /    | || |   |  _|  _   | || |    | |   _   | |
| |   _| |__/ |  | || |  _| |___/ |  | || |    \ ' /     | || |  _| |___/ |  | || |   _| |__/ |  | |
| |  |________|  | || | |_________|  | || |     \_/      | || | |_________|  | || |  |________|  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
                                         .----------------.                                                     
                                        | .--------------. |                                                    
                                        | |    _____     | |                                                    
                                        | |   / ___ `.   | |                                                    
                                        | |  |_/___) |   | |                                                    
                                        | |   .'____.'   | |                                                    
                                        | |  / /____     | |                                                    
                                        | |  |_______|   | |                                                    
                                        | |              | |                                                    
                                        | '--------------' |                                                    
                                         '----------------'                                                    
"""

LEVEL_3 = """
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |   _____      | || |  _________   | || | ____   ____  | || |  _________   | || |   _____      | |
| |  |_   _|     | || | |_   ___  |  | || ||_  _| |_  _| | || | |_   ___  |  | || |  |_   _|     | |
| |    | |       | || |   | |_  \_|  | || |  \ \   / /   | || |   | |_  \_|  | || |    | |       | |
| |    | |   _   | || |   |  _|  _   | || |   \ \ / /    | || |   |  _|  _   | || |    | |   _   | |
| |   _| |__/ |  | || |  _| |___/ |  | || |    \ ' /     | || |  _| |___/ |  | || |   _| |__/ |  | |
| |  |________|  | || | |_________|  | || |     \_/      | || | |_________|  | || |  |________|  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
                                         .----------------.                                                     
                                        | .--------------. |                                                    
                                        | |    ______    | |                                                    
                                        | |   / ____ `.  | |                                                    
                                        | |   `'  __) |  | |                                                    
                                        | |   _  |__ '.  | |                                                    
                                        | |  | \____) |  | |                                                    
                                        | |   \______.'  | |                                                    
                                        | |              | |                                                    
                                        | '--------------' |                                                    
                                         '----------------'                                                     
"""

LEVEL_1 = """
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |   _____      | || |  _________   | || | ____   ____  | || |  _________   | || |   _____      | |
| |  |_   _|     | || | |_   ___  |  | || ||_  _| |_  _| | || | |_   ___  |  | || |  |_   _|     | |
| |    | |       | || |   | |_  \_|  | || |  \ \   / /   | || |   | |_  \_|  | || |    | |       | |
| |    | |   _   | || |   |  _|  _   | || |   \ \ / /    | || |   |  _|  _   | || |    | |   _   | |
| |   _| |__/ |  | || |  _| |___/ |  | || |    \ ' /     | || |  _| |___/ |  | || |   _| |__/ |  | |
| |  |________|  | || | |_________|  | || |     \_/      | || | |_________|  | || |  |________|  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
                                         .----------------.                                                     
                                        | .--------------. |                                                    
                                        | |     __       | |                                                    
                                        | |    /  |      | |                                                    
                                        | |    `| |      | |                                                    
                                        | |     | |      | |                                                    
                                        | |    _| |_     | |                                                    
                                        | |   |_____|    | |                                                    
                                        | |              | |                                                    
                                        | '--------------' |                                                    
                                         '----------------'                                                     
"""