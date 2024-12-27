import sys, time, os
import random

# Define the size of the map
GRID_WIDTH = random.randint(2,10)
GRID_HEIGHT = random.randint(2,10)

# Make text output slower for immersion
def typewriter(message, speed):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(speed)
        else:
            time.sleep(1)
            
    sys.stdout.write("\n")  # Ensure a newline at the end of the message
    sys.stdout.flush()

# Check if player is in the same location as treasure
def treasure_found(player_position, treasure_position):
    return player_position == treasure_position

# Player lights a torch and looks at the map
def light_torch(position, num_of_torches):
    if num_of_torches > 0:
        num_of_torches -= 1
        typewriter("You light a torch and check your map.",0.05)
        typewriter(f"This cave is {GRID_WIDTH} paces from east to west and {GRID_HEIGHT} paces north to south",0.05)
        typewriter(f"Your current coordinates are: {position}.",0.05)
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
def debug():
    print(f"The map is {GRID_WIDTH} wide and {GRID_HEIGHT} tall.")
    print(f"You are at position {player_position}.")
    print(f"The treasure is at {treasure_position}.")
    print(f"The monster is at {monster.position}.")
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
    

# Defining the Monster class
class Monster:
    def __init__(self, position):
        self.position = position

    def move(self):
        directions = ["north", "south", "east", "west"]
        direction = random.choice(directions)
        
        if direction == "north" and self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == "south" and self.position[1] < GRID_HEIGHT - 1:
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == "east" and self.position[0] < GRID_WIDTH - 1:
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == "west" and self.position[0] > 0:
            self.position = (self.position[0] - 1, self.position[1])

    def check_if_caught(self, player_position):
        if self.position == player_position:
            typewriter(f"You were caught by the monster at position {self.position}!",0.05)
            typewriter("Game Over!",0.05)
            return True
        return False

# Variables
num_of_torches = 3

# Starting positions
player_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
treasure_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
monster = Monster((random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)))

# Display welcome screen
welcome_screen()

# Main game loop
while True:
    command = input("What do you want to do?: ").strip().lower()
    
    if command.startswith("go "):
        direction = command[3:]  # Slicing syntax: Start at index 3 and begin extracting characters from the 4th character
        if direction == "north" and player_position[1] > 0:
            player_position = (player_position[0], player_position[1] - 1)
            typewriter(f"You moved north.",0.05)
            print(" ")
        elif direction == "south" and player_position[1] < GRID_HEIGHT - 1:
            player_position = (player_position[0], player_position[1] + 1)
            typewriter(f"You moved south.",0.05)
            print(" ")
        elif direction == "east" and player_position[0] < GRID_WIDTH - 1:
            player_position = (player_position[0] + 1, player_position[1])
            typewriter(f"You moved east.",0.05)
            print(" ")
        elif direction == "west" and player_position[0] > 0:
            player_position = (player_position[0] - 1, player_position[1])
            typewriter(f"You moved west.",0.05)
            print(" ")
        else:
            typewriter("The way is blocked.",0.05)
            print(" ")
        
        # Move the monster and check if the player is caught
        monster.move()
        if monster.check_if_caught(player_position):
            break  # End the game if the player was caught by the monster

    elif command == 'look for treasure'.strip().lower():
        if treasure_found(player_position, treasure_position):
            typewriter("Congratulations! You found the treasure!",0.05)
            print(" ")
            typewriter("Game Over",0.05)
            break
        else:
            typewriter("There is nothing here",0.05)
            print(" ")
            
            # Move the monster and check if the player is caught
            monster.move()
            if monster.check_if_caught(player_position):
                break  # End the game if the player was caught by the monster
    elif command == 'light a torch'.strip().lower():
        num_of_torches = light_torch(player_position, num_of_torches)  # Pass and update the number of torches
        monster.move()
        if monster.check_if_caught(player_position):
            break  # End the game if the player was caught by the monster
    elif command == 'help'.strip().lower():
        display_commands()
    elif command == 'cheat'.strip().lower():
        debug()
    else:
        typewriter(f"I don't know what '{command}' means.",0.05)
        print(" ")