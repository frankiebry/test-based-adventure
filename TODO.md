### Todo
- [ ] Add inventory using a dictionary.
- [ ] Allow player to find more items
- [ ] Warn player when monster is close
- [ ] Add `if __name__ == '__main__':`
- [ ] Separate debug into another file?
- [ ] Convert this entire game into a graphical version
- [ ] More immersive writing
- [ ] More commands
- [ ] Allow player to type more commands that do the same thing (e.g. "go north", "move north", "go up", etc)
- [ ] Add mor color to text

### Ideas for changes/improvements
- [ ] Instead of treasure, player looks for key to escape dungeon?
- [ ] Monster chases player when torch is lit?
- [ ] Player finds items that protect them from the monster?
- [ ] If player digs, and treasure isn't there, chance to find more torches or other items
- [ ] Introduce rare item that lights up cave completely, and reveals treasure on map, but monster moves faster and/or beelines for the player

### Bugs/Issues
- [ ] The monster can only move every other turn... difficulty went from high to low. Too slow now? Or movement to random?
- [ ] Metal detector doesn't seem to work properly sometimes. I'll be standing one tile next to the treasure and it's silent? But other playthroughs it works perfectly...
- [ ] The last icon that is drawn on the map will cover any icon drawn before it.

### Clean Code
- [ ] Better solution to making all variables global in reset_game() function
- [ ] Find a better solution to the way reset_game() and settings.reset() are used to initialize and reset variables
- [ ] Repeated distance calculations (e.g., in sweep_for_treasure and Monster.is_near_player) could be centralized.
- [ ] Create "randomize()" function that returns a tuple of random values? Then use this function anytime a position needs to be reset or randomize?
- [ ] All strings should use '' instead of ""? Or at least just be consistent
- [ ] Comment everything that doesn't have a clear purpose?
- [ ] Functions need to be better named and commented using docstrings?
- [ ] Find a more elegant solution to the following ~

This statement is awkward...
```Python
remaining_torches = light_torch(player_position, monster.position, remaining_torches)
```

Also this code block is used twice...
```Python
# Ask if the player wants to play again
if play_again():
    reset_game()  # Reset the game state
    continue  # Restart the game loop
else:
    typewriter("Thank you for playing!", 0.05)
    break
```