### Todo
- [ ] More immersive writing

### Ideas for changes/improvements
- [ ] Add option to move 2 or 3 paces at once?
- [ ] Add combat and HP (change "caught" to "encounter")
- [ ] If player digs, and the key isn't there, chance to find more torches or other items
- [ ] Allow player to find more items, helpful items like torches and score items like gems
- [ ] Add high score file using JSON
- [ ] Monster heads straight to the player's last known location when a torch is lit, unless it's 2 paces away.
- [ ] Player finds items that protect them from the monster?
- [ ] Introduce rare item that lights up cave completely, and reveals treasure on map, but monster moves faster and/or beelines for the player
- [ ] Convert this entire game into a graphical version
- [ ] Add additional commands that display text but do nothing (e.g. "bang on door" -> "there is no response")
- [ ] Warning message when monster is near should not repeat, it should say something different to indicate the monster is chasing you.

### Bugs/Issues
- [ ] X's are no longer being drawn on the map for spots that have been already dug!
- [ ] The alt codes for the icons on the map are different sizes and make the map look wonky. Find a set that are all the same dimensions
- [ ] Metal detector doesn't seem to work properly sometimes. I'll be standing one tile next to the treasure and it's silent? But other playthroughs it works perfectly...
- [ ] The player, monster and treasure can stack, and the last icon that is drawn on the map will cover any icon drawn before it.
- [ ] Apparently if ANSI escape codes that set the text color explicitly are not reset with \033[0m, the terminal will continue applying the color to subsequent text, even after the program exits. The terminal has to be closed to fix this.
- [ ] The typewriter "stutters" when printing color text

### Cleaner Code
- [ ] All strings should use '' instead of ""? Or at least just be consistent
- [ ] Comment everything that doesn't have a clear purpose or needs to be explained?
- [ ] Find a more elegant solution to the following ~

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