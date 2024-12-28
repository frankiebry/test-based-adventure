### Todo
- [ ] Make the monster beeline to the players last known position after the torch is lit? Unless it's 2 tiles away, then just chase like normal
- [ ] Add hint for where the treasure is? Option to show icon (last torch maybe?)
- [ ] Change look for treasure to "dig?"
- [ ] Add inventory using a dictionary.
- [ ] Add `if __name__ == '__main__':`
- [ ] Add a "play again" option.
- [ ] Separate debug into another file?
- [ ] Convert this entire game into a graphical version
- [ ] Instead of treasure, player looks for key to escape dungeon?
- [ ] Player and treasure should be separate classes as well?

### Issues
- [ ] When there is one torch left it says "you have 1 torches left"
- [ ] The last icon that is drawn on the map will cover any icon drawn before it.
- [ ] Functions need to be better named and commented. Use docstrings
- [ ] Comment everything that doesn't have a clear purpose.
- [ ] Find a more elegant solution to the following ~

There are several duplicates of this block of code:
```Python
monster.move(player_position)
    if monster.check_if_caught(player_position):
        break  # End the game if the player was caught by the monster
```

This statement is awkward...
```Python
num_of_torches = light_torch(player_position, monster.position, num_of_torches)
```