### Todo
- [ ] Monster now chases the player but difficulty has spiked. Either slow the monster down (can only move once every two turns?) and/or it only chases when it gets close to the player.
- [ ] Add hint for where the treasure is?
- [ ] Add inventory using a dictionary.
- [ ] Add code that checks if main?
- [ ] Add a "play again" option.
- [ ] Change cheat (debug) to just show the map

### Issues
- [ ] If the player types "go " + anything other than a cardinal direction, it just says "the way is blocked"
- [ ] When there is one torch left it says "you have 1 torches left"
- [ ] The last icon that is drawn on the map will cover any icon drawn before it.
- [ ] Functions need to be better named and commented.
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