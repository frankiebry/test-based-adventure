from monster import Monster # class to represent the monster in the game
from typewriter import typewriter # function to simulate typing text
from settings import settings # where all variables are initialized and reset
from utils import calculate_distance # formula to calculate distance between two points
from commands import commands_dict # import dictionary of all possible commands

# Our main game class
class Game:
    def __init__(self):
        """Initialize the game by resetting to default settings."""
        self.reset_game() # Reset the game to its initial state with default settings

    def reset_game(self):
        """Reset the game to its initial state with default settings."""
        settings.reset() # Reset the settings to their default values
        self.remaining_torches = settings.DEFAULT_NUM_OF_TORCHES
        self.searched_positions = settings.DEFAULT_SEARCHED_POSITIONS
        self.player_position = settings.DEFAULT_PLAYER_POS
        self.key_position = settings.DEFAULT_KEY_POS
        self.monster = Monster(settings.DEFAULT_MONSTER_POS)

    def key_found(self):
        """Check if the player is at the key's position."""
        return self.player_position == self.key_position

    def draw_map(self, show_key=False):
        """
        Draw the game map with the player, monster, and optionally the key.

        Args:
            show_key (bool): Whether to display the key on the map.
        """
        grid = [['□ ' for _ in range(settings.GRID_WIDTH)] for _ in range(settings.GRID_HEIGHT)]
        for pos in self.searched_positions: # Mark the spots the player has already dug
            x, y = pos
            grid[y][x] = '\033[96mX \033[0m' # Use ANSI escape codes for colored text - Bright Cyan
        player_x, player_y = self.player_position
        grid[player_y][player_x] = '\033[92m⧆ \033[0m' # Bright Green
        monster_x, monster_y = self.monster.position
        grid[monster_y][monster_x] = '\033[95mM \033[0m' # Bright Magenta
        if show_key:
            key_x, key_y = self.key_position
            grid[key_y][key_x] = '\033[93m⚿ \033[0m' # Bright Yellow
        for row in grid: # Print the map row by row
            print(''.join(row))

    def light_torch(self):
        """Use a torch to reveal the map and display helpful information."""
        if self.remaining_torches > 0: # Check if the player has any torches left
            self.remaining_torches -= 1
            typewriter("You light a torch and check your map.", 0.05)
            print(' ')
            self.draw_map()
            print(' ')
            typewriter("\033[92m⧆\033[0m: Your current location.", 0.05)
            typewriter("\033[96mX\033[0m: Spots you've already dug.", 0.05)
            typewriter("\033[95mM\033[0m: You see an ominous shadowy figure standing there...", 0.1)
            if self.remaining_torches == 1: # Handle singular vs. plural in the message.
                typewriter(f"The light has gone out. You have {self.remaining_torches} torch left", 0.05)
            else:
                typewriter(f"The light has gone out. You have {self.remaining_torches} torches left", 0.05)
            print(' ')
        else:
            typewriter("You don't have any torches left", 0.05)

    def use_metal_detector(self):
        """Use the metal detector to get a hint about the key's location."""
        distance = calculate_distance(self.player_position, self.key_position)
        if distance == 0:
            typewriter("The metal detector is going wild!!", 0.05)
        elif distance == 1:
            typewriter("The metal detector is beeping rapidly!", 0.05)
        elif distance == 2:
            typewriter("The metal detector is slowly beeping.", 0.05)
        else:
            typewriter("The metal detector is silent.", 0.05)

    def display_commands(self):
        """Display the list of available commands to the player."""
        print(' ')
        typewriter("*****************", 0.02)
        typewriter("* Legal commands *", 0.02)
        typewriter("*****************", 0.02)
        print(' ')
        typewriter("MOVE NORTH", 0.02)
        typewriter("MOVE SOUTH", 0.02)
        typewriter("MOVE EAST", 0.02)
        typewriter("MOVE WEST", 0.02)
        typewriter("DIG HERE", 0.02)
        typewriter("USE A TORCH: check your map", 0.02)
        typewriter("SWEEP FOR KEY: use metal detector", 0.02)
        print(' ')

    def debug(self):
        """Display the full map, including the key's location (cheat/debug mode)."""
        print(' ')
        self.draw_map(show_key=True) # Show the key on the map
        print(' ')

    def welcome_screen(self):
        """Display the welcome screen and explain the rules for first timers."""
        response = input(
            "Welcome to Frankie's text based adventure game. Have you played this game before? (Y/N): "
        ).strip().lower()
        if response in ['n', 'no']:
            print(' ')
            typewriter('Here are the rules..', 0.05)
            print(' ')
            typewriter('You are in a dark cave and need to find the key to the exit.', 0.05)
            typewriter('Each turn you can do one of the following:', 0.05)
            typewriter('* Move north, south, east or west', 0.05)
            typewriter('* Use your metal detector to find the key.', 0.05)
            typewriter('* Dig to find the key. You may also find helpful items or treasure.', 0.05)
            typewriter('* Light a torch to check your map. You only get 3 torches.', 0.05)
            typewriter('Beware, there is a monster in the cave with you. Each turn the monster moves one pace.', 0.05)
            typewriter('The game will end if you find the key... or the monster catches you. Good luck!', 0.05)

    def play_again(self):
        """Prompt the player to decide whether to play again."""
        response = input("Do you want to play again? (Y/N): ").strip().lower()
        return response in ["y", "yes"]

    def run(self):
        """Run the main game loop, handling player commands and game logic."""
        self.welcome_screen()
        while True:
            print(' ')
            command = input("What do you want to do?: ").strip().lower()
            monster_should_move = True # Assume the monster will move on each turn by default

            # We are using a dictionary of lists to store the possible commands
            match command:
                case _ if command in commands_dict["up"]:
                    if self.player_position[1] > 0:
                        self.player_position = (self.player_position[0], self.player_position[1] - 1)
                        typewriter("You moved north.", 0.05)
                    else:
                        typewriter("The way is blocked.", 0.05)

                case _ if command in commands_dict["down"]:
                    if self.player_position[1] < settings.GRID_HEIGHT - 1:
                        self.player_position = (self.player_position[0], self.player_position[1] + 1)
                        typewriter("You moved south.", 0.05)
                    else:
                        typewriter("The way is blocked.", 0.05)

                case _ if command in commands_dict["right"]:
                    if self.player_position[0] < settings.GRID_WIDTH - 1:
                        self.player_position = (self.player_position[0] + 1, self.player_position[1])
                        typewriter("You moved east.", 0.05)
                    else:
                        typewriter("The way is blocked.", 0.05)

                case _ if command in commands_dict["left"]:
                    if self.player_position[0] > 0:
                        self.player_position = (self.player_position[0] - 1, self.player_position[1])
                        typewriter("You moved west.", 0.05)
                    else:
                        typewriter("The way is blocked.", 0.05)

                case _ if command in commands_dict["dig"]:
                    if self.key_found():
                        typewriter("Congratulations! You found the key!", 0.05)
                        print(' ')
                        if self.play_again():
                            self.reset_game()
                            continue
                        else:
                            typewriter("Thank you for playing!", 0.05)
                            break
                    else:
                        typewriter("There is nothing here.", 0.05)
                        self.searched_positions.append(self.player_position) # Mark the spot as searched

                case _ if command in commands_dict["torch"]:
                    self.light_torch()

                case _ if command in commands_dict["sweep"]:
                    self.use_metal_detector()

                case _ if command in commands_dict["help"]:
                    self.display_commands()
                    monster_should_move = False

                case _ if command in commands_dict["debug"]:
                    print(' ')
                    self.debug()
                    monster_should_move = False

                case _:
                    typewriter(f'I don\'t know what "{command}" means.', 0.05)
                    print(' ')
                    monster_should_move = False

            if monster_should_move:
                self.monster.move(self.player_position)
                if self.monster.check_if_caught(self.player_position):
                    print(' ')
                    typewriter(f'You were caught by the monster!', 0.05)
                    print(' ')
                    if self.play_again():
                        self.reset_game()
                        continue
                    else:
                        typewriter('Thank you for playing!', 0.05)
                        break

        print(' ')
        typewriter("GAME OVER", 0.5)

# Run the game if this script is executed
if __name__ == '__main__':
    game = Game()
    game.run()