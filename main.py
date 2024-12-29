import random
from monster import Monster
from typewriter import typewriter
# from settings import *

# Function to check if the player has found the treasure
def treasure_found(player_position, treasure_position):
    """
    Checks if the player's position matches the treasure's position.
    
    Args:
    player_position (tuple): The (x, y) coordinates of the player.
    treasure_position (tuple): The (x, y) coordinates of the treasure.
    
    Returns:
    bool: True if the player has found the treasure, False otherwise.
    """
    
    return player_position == treasure_position

# Function to draw the map showing the player's, monster's, and (if cheating) treasure's position
def draw_map(player_position, monster_position, treasure_position, show_treasure=False):
    """
    Draws the cave map with the player's, monster's, and optionally the treasure's position.
    
    Args:
    player_position (tuple): The (x, y) coordinates of the player.
    monster_position (tuple): The (x, y) coordinates of the monster.
    treasure_position (tuple): The (x, y) coordinates of the treasure.
    show_treasure (bool): Whether to show the treasure on the map or not.
    """
    
    # Create an empty grid of '□' representing unexplored areas
    grid = [['□ ' for j in range(GRID_WIDTH)] for i in range(GRID_HEIGHT)]
    
    # Mark the searched positions with 'X'
    for pos in searched_positions:
        x, y = pos
        grid[y][x] = '\033[96mX \033[0m' # ANSI escape codes provide color, 96 = Bright Cyan
    
    # Mark the player's position with '⧆'
    player_x, player_y = player_position
    grid[player_y][player_x] = '\033[92m⧆ \033[0m' # Bright Green
        
    # Mark the monster's position with 'M'
    monster_x, monster_y = monster_position
    grid[monster_y][monster_x] = '\033[95mM \033[0m' # Bright Magenta
    
    # Optionally, mark the treasure's position with '⚿'
    if show_treasure:
        treasure_x, treasure_y = treasure_position
        grid[treasure_y][treasure_x] = '\033[93m⚿ \033[0m' # Bright Yellow
    
    # Print the map
    for row in grid:
        print(''.join(row))

# Function for lighting a torch and displaying the map
def light_torch(player_position, monster_position, remaining_torches):
    """
    Lights a torch and displays the map if the player has any torches left.
    
    Args:
    player_position (tuple): The (x, y) coordinates of the player.
    monster_position (tuple): The (x, y) coordinates of the monster.
    remaining_torches (int): The number of torches the player has left.
    
    Returns:
    int: The updated number of remaining torches.
    """
    
    if remaining_torches > 0:
        remaining_torches -= 1
        typewriter("You light a torch and check your map.",0.05)
        
        # Display the map with the current positions
        print(" ")
        draw_map(player_position, monster_position, treasure_position)
        print(" ")
        
        typewriter("\033[92m⧆\033[0m: Your current location.",0.05)
        typewriter("\033[96mX\033[0m: Spots you've already dug.",0.05)
        typewriter("\033[95mM\033[0m: You see an ominous shadowy figure standing there...",0.1)
        if remaining_torches == 1:
            typewriter(f"The light has gone out. You have {remaining_torches} torch left",0.05)
        else:
            typewriter(f"The light has gone out. You have {remaining_torches} torches left",0.05)
        print(" ")
    else:
        typewriter("You don't have any torches left",0.05)
    
    return remaining_torches

# Function to sweep for treasure using the metal detector
def sweep_for_treasure(player_position, treasure_position):
    """
    Uses the metal detector to check how far the player is from the treasure.
    
    Args:
    player_position (tuple): The (x, y) coordinates of the player.
    treasure_position (tuple): The (x, y) coordinates of the treasure.
    """
    
    player_x, player_y = player_position
    treasure_x, treasure_y = treasure_position
    
    # Calculate Manhattan distance between player and treasure
    distance = abs(player_x - treasure_x) + abs(player_y - treasure_y)
    
    # Provide feedback based on the distance
    if distance == 0:
        typewriter("The metal detector is going wild!!", 0.05)
    elif distance == 1:
        typewriter("The metal detector is beeping rapidly!", 0.05)
    elif distance == 2:
        typewriter("The metal detector is slowly beeping.", 0.05)
    else:
        typewriter("The metal detector is silent.", 0.05)

# Function to display the available commands
def display_commands():
    """
    Displays the list of available commands for the player.
    """
    
    print(" ")
    typewriter("*****************",0.02)
    typewriter("* Legal commands *",0.02)
    typewriter("*****************",0.02)
    print(" ")
    typewriter("GO NORTH",0.02)
    typewriter("GO SOUTH",0.02)
    typewriter("GO EAST",0.02)
    typewriter("GO WEST",0.02)
    typewriter("DIG",0.02)
    typewriter("LIGHT TORCH: check your map",0.02)
    typewriter("SWEEP: use metal detector",0.02)
    typewriter("HELP: displays these commands again (the monster will not move)",0.02)
    print(" ")

# Debugging function to view the map with treasure location
def debug(player_position, monster_position, treasure_position):
    """
    Displays the map for debugging purposes, showing the treasure's location.
    
    Args:
    player_position (tuple): The (x, y) coordinates of the player.
    monster_position (tuple): The (x, y) coordinates of the monster.
    treasure_position (tuple): The (x, y) coordinates of the treasure.
    """
    
    print(" ")
    draw_map(player_position, monster_position, treasure_position, show_treasure=True)
    print(" ")

# Function to display the welcome screen and explain the game rules
def welcome_screen():
    """
    Displays the welcome screen with the game rules and commands.
    """
    
    response = input(
        "Welcome to Frankie's text based adventure game. Have you played this game before? (Y/N): "
    ).strip().lower()
    
    if response == 'n' or response == 'no':
        print(" ")
        typewriter("Here are the rules:",0.05)
        typewriter("You are in a dark cave. Each turn you can use a command to do one of the following.",0.05)
        typewriter("- Move north, south, east or west",0.05)
        typewriter("- Use a metal detector.",0.05)
        typewriter("- Dig for treasure.",0.05)
        typewriter("- Light a torch and check your map. You only get 3 torches.",0.05)
        typewriter("Beware, there is a monster in the cave with you. Each turn the monster moves one pace.",0.05)
        typewriter("The game will end if you find the treasure... or the monster catches you. Good luck!",0.05)
        print(" ")
        display_commands()

def play_again():
    """
    Asks the player if they want to play again and returns True for yes, False for no.
    """
    response = input("Do you want to play again? (Y/N): ").strip().lower()
    if response == "y" or response == "yes":
        return True
    else:
        return False
    
def reset_game():
    """
    Resets all necessary variables to their initial state for a new game.
    """
    # This is really ugly... fix this
    global remaining_torches, searched_positions, player_position, treasure_position, monster, GRID_WIDTH, GRID_HEIGHT

    # Reset grid size (randomize each time)
    GRID_WIDTH = random.randint(4, 10)
    GRID_HEIGHT = random.randint(4, 10)
    
    # Reset variables as defined in settings.py
    remaining_torches = 3
    searched_positions = []
    player_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    treasure_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    
    # Create a new monster with a random position within the new grid size... this doesn't look good though
    monster = Monster((random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)),GRID_WIDTH,GRID_HEIGHT)

# Initializing variables before the game starts
reset_game()

# Display the welcome screen at the start, outside the loop so it isn't shown on "Play again?"
welcome_screen()

# Main game loop
while True:
    print(" ")
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

        case "dig":
            if treasure_found(player_position, treasure_position):
                typewriter("Congratulations! You found the treasure!", 0.05)
                print(" ")
                # Ask if the player wants to play again
                if play_again():
                    reset_game()  # Reset the game state
                    continue  # Restart the game loop
                else:
                    typewriter("Thank you for playing!", 0.05)
                    break
            else:
                typewriter("There is nothing here.", 0.05)
                searched_positions.append(player_position)

        case "light torch":
            remaining_torches = light_torch(player_position, monster.position, remaining_torches)

        case "sweep":
            sweep_for_treasure(player_position, treasure_position)

        case "help":
            display_commands()
            monster_should_move = False  # Skip monster movement for help

        case "cheat":
            print(" ")
            debug(player_position, monster.position, treasure_position)
            monster_should_move = False  # Skip monster movement for cheat

        case _:
            typewriter(f"I don't know what '{command}' means.", 0.05)
            print(" ")
            monster_should_move = False  # Skip monster movement for invalid commands

    # Move the monster only if required
    if monster_should_move:
        monster.move(player_position)
        if monster.check_if_caught(player_position):
            print(" ")
            typewriter(f"You were caught by the monster!",0.05)
            print(" ")
            # Ask if the player wants to play again
            if play_again():
                reset_game()  # Reset the game state
                continue  # Restart the game loop
            else:
                typewriter("Thank you for playing!", 0.05)
                break

print(" ")
typewriter("GAME OVER", 0.5)