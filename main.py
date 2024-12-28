import random
from monster import Monster
from typewriter import typewriter
from settings import GRID_WIDTH, GRID_HEIGHT

# Check if player is in the same location as treasure
def treasure_found(player_position, treasure_position):
    return player_position == treasure_position

# Draw the map
def draw_map(player_position, monster_position, treasure_position, show_treasure=False):
    # Create an empty grid of □'s
    grid = [['□ ' for j in range(GRID_WIDTH)] for i in range(GRID_HEIGHT)]
    
    # Mark the searched positions with 'X'
    for pos in searched_positions:
        x, y = pos
        grid[y][x] = 'X '
    
    # Mark the player's position with '⧆'
    player_x, player_y = player_position
    grid[player_y][player_x] = '\033[92m⧆ \033[0m' # ANSI escape codes provide color
        
    # Mark the monster's position with 'M'
    monster_x, monster_y = monster_position
    grid[monster_y][monster_x] = '\033[95mM \033[0m' # Bright Magenta
    
    # Conditionally mark the treasure's position with '⚿'
    if show_treasure:
        treasure_x, treasure_y = treasure_position
        grid[treasure_y][treasure_x] = '\033[93m⚿ \033[0m' # Bright Yellow
    
    # Print the map
    for row in grid:
        print(''.join(row))

# Player lights a torch and looks at the map
def light_torch(player_position, monster_position, num_of_torches):
    if num_of_torches > 0:
        num_of_torches -= 1
        typewriter("You light a torch and check your map.",0.05)
        print(" ")
        
        # Display the map
        draw_map(player_position, monster_position, treasure_position)
        print(" ")
        
        typewriter("The ⧆ icon indicates your position on the map",0.05)
        typewriter("The X icon indicates indicates spots you've already searched for treasure",0.05)
        typewriter("You see an ominous shadowy figure where M is marked on the map...",0.05)
        typewriter(f"The light has gone out. You have {num_of_torches} torches left",0.05)
        print(" ")
    else:
        typewriter("You don't have any torches left",0.05)
    return num_of_torches

# Display the available commands
def display_commands():
    typewriter("*****************",0.02)
    typewriter("* Legal commands *",0.02)
    typewriter("*****************",0.02)
    print(" ")
    typewriter("GO NORTH",0.02)
    typewriter("GO SOUTH",0.02)
    typewriter("GO EAST",0.02)
    typewriter("GO WEST",0.02)
    typewriter("LOOK FOR TREASURE",0.02)
    typewriter("LIGHT A TORCH (check your map)",0.02)
    typewriter("HELP (displays these commands again)",0.02)
    print("")

# Use to debug, disable this function during gameplay
def debug(player_position, monster_position, treasure_position):
    draw_map(player_position, monster_position, treasure_position, show_treasure=True)
    print(" ")

# Welcome Screen
def welcome_screen():
    response = input(
        "Welcome to Frankie's text based adventure game. Have you played this game before? (Y/N): "
    ).strip().lower()
    
    if response == 'n' or response == 'no':
        print(" ")
        typewriter("Here are the rules:",0.05)
        typewriter("You start in a dark cave. Each turn you can go one pace North, South, East or West.",0.05)
        typewriter("Or you can spend your turn looking for treasure.",0.05)
        typewriter("Or you can spend your turn to light a torch and check your map. You only get 3 torches.",0.05)
        typewriter("Beware, there is a monster in the cave with you. Each turn the monster moves one pace.",0.05)
        typewriter("The game will end if you find the treasure... or the monster catches you. Good luck!",0.05)
        print(" ")
        display_commands()

# Variables
num_of_torches = 3
searched_positions = [] # List to track the locations where the player has searched for treasure

# Starting positions
player_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
treasure_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
monster = Monster((random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)))

# Display welcome screen
welcome_screen()

# Main game loop
while True:
    command = input("What do you want to do?: ").strip().lower()
    monster_should_move = True  # Default to true; adjust for specific commands

    match command:
        case "go north":
            if player_position[1] > 0:
                player_position = (player_position[0], player_position[1] - 1)
                typewriter("You moved north.", 0.05)
            else:
                typewriter("The way is blocked.", 0.05)

        case "go south":
            if player_position[1] < GRID_HEIGHT - 1:
                player_position = (player_position[0], player_position[1] + 1)
                typewriter("You moved south.", 0.05)
            else:
                typewriter("The way is blocked.", 0.05)

        case "go east":
            if player_position[0] < GRID_WIDTH - 1:
                player_position = (player_position[0] + 1, player_position[1])
                typewriter("You moved east.", 0.05)
            else:
                typewriter("The way is blocked.", 0.05)

        case "go west":
            if player_position[0] > 0:
                player_position = (player_position[0] - 1, player_position[1])
                typewriter("You moved west.", 0.05)
            else:
                typewriter("The way is blocked.", 0.05)

        case "look for treasure":
            if treasure_found(player_position, treasure_position):
                typewriter("Congratulations! You found the treasure!", 0.05)
                typewriter("Game Over", 0.05)
                break
            else:
                typewriter("There is nothing here.", 0.05)
                searched_positions.append(player_position)

        case "light a torch":
            num_of_torches = light_torch(player_position, monster.position, num_of_torches)

        case "help":
            display_commands()
            monster_should_move = False  # Skip monster movement for help

        case "cheat":
            debug(player_position, monster.position, treasure_position)
            monster_should_move = False  # Skip monster movement for cheat

        case _:
            typewriter(f"I don't know what '{command}' means.", 0.05)
            monster_should_move = False  # Skip monster movement for invalid commands

    # Move the monster only if required
    if monster_should_move:
        monster.move(player_position)
        if monster.check_if_caught(player_position):
            typewriter("The monster caught you! Game Over.", 0.05)
            break