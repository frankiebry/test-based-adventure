import random

"""
Define the map as a 4x4 grid.
Each cell specifies which directions are open (north, east, south, west).
If a cardinal direction is false, that means there is a wall there.
The top left of the grid is (0,0) and the bottom right is (3,3)
""" 
map_grid = {
    (0, 0): {"north": False, "south": True, "east": True, "west": False},
    (1, 0): {"north": False, "south": True, "east": True, "west": True},
    (2, 0): {"north": False, "south": True, "east": True, "west": True},
    (3, 0): {"north": False, "south": True, "east": False, "west": True},
    
    (0, 1): {"north": True, "south": True, "east": True, "west": False},
    (1, 1): {"north": True, "south": True, "east": True, "west": True},
    (2, 1): {"north": True, "south": True, "east": True, "west": True},
    (3, 1): {"north": True, "south": True, "east": False, "west": True},
    
    (0, 2): {"north": True, "south": True, "east": True, "west": False},
    (1, 2): {"north": True, "south": True, "east": True, "west": True},
    (2, 2): {"north": True, "south": True, "east": True, "west": True},
    (3, 2): {"north": True, "south": True, "east": False, "west": True},
    
    (0, 3): {"north": True, "south": False, "east": True, "west": False},
    (1, 3): {"north": True, "south": False, "east": True, "west": True},
    (2, 3): {"north": True, "south": False, "east": True, "west": True},
    (3, 3): {"north": True, "south": False, "east": False, "west": True},
}

def treasure_found(player_position,treasure_position):
    if player_position == treasure_position:
        return True
    else:
        return False
    
def monster_move(monster_position):
    directions = ["north", "south", "east", "west"]
    direction = random.choice(directions)
    
    if direction == "north" and monster_position[1] > 0:
        return (monster_position[0], monster_position[1] - 1)
    elif direction == "south" and monster_position[1] < 3:
        return (monster_position[0], monster_position[1] + 1)
    elif direction == "east" and monster_position[0] < 3:
        return (monster_position[0] + 1, monster_position[1])
    elif direction == "west" and monster_position[0] > 0:
        return (monster_position[0] - 1, monster_position[1])
    return monster_position  # Return the position if no movement is possible

def update_monster(player_position, monster_position):
    # Move the monster
    monster_position = monster_move(monster_position)
    
    # Check if the player has been caught by the monster
    if player_position == monster_position:
        print(f"You were caught by a monster at position {monster_position}!")
        return True  # End the game if caught
    
    # Print the monster's position for feedback
    print(f"The monster is at position {monster_position}.")
    return False  # Continue the game if not caught
    
# Start the player in the top-left corner (0, 0)
player_position = (0, 0)
treasure_position = (random.randint(0, 3), random.randint(0, 3))
monster_position = (random.randint(0, 3), random.randint(0, 3))

# Main game loop
while True:
    print(f"You are at position {player_position}.")
    
    # use to debug, comment out during gameplay
    print(f"The treasure is at {treasure_position}.")
    print(f"The monster is at {monster_position}.")
    
    command = input("What do you want to do?: ").strip().lower()
    
    if command.startswith("go "):
        direction = command[3:] # Slicing syntax: Start at index 3 and begin extracting characters from the 4th character
        if direction in map_grid[player_position]:
            if map_grid[player_position][direction]:
                # Update the player's position
                if direction == "north":
                    player_position = (player_position[0], player_position[1] - 1)
                elif direction == "east":
                    player_position = (player_position[0] + 1, player_position[1])
                elif direction == "south":
                    player_position = (player_position[0], player_position[1] + 1)
                elif direction == "west":
                    player_position = (player_position[0] - 1, player_position[1])
                print(f"You moved {direction}.")
                print(" ")
                if update_monster(player_position, monster_position):
                    break  # End the game if the player was caught by the monster
            else:
                print("The way is blocked.")
                print(" ")
                if update_monster(player_position, monster_position):
                    break  # End the game if the player was caught by the monster
        else:
            print("Invalid direction.")
            print(" ")
    elif command == 'look for treasure'.strip().lower():
        if treasure_found(player_position, treasure_position):
            print("You found treasure!")
            print(" ")
            print("Game Over")
            break
        else:
            print("There is nothing here")
            print(" ")
            if update_monster(player_position, monster_position):
                break  # End the game if the player was caught by the monster
    else:
        print("I don't understand that command.")
        print(" ")