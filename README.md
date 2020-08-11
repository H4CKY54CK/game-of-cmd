# game-of-cmd
Game of Life in pygame.

## Instructions

You need `pygame` and `numpy` to run this.

If you don't have these, and want a no-fuss install/setup, run the installation script `no-fuss-setup.py`. It prompts you before each decision, so don't worry. Not that there's many decisions. There's two.

### Controls

- P - Pause/Unpause
- G - Place glider
- S - Place Spaceship
- U - Place Glider Gun
- C - Change color of active squares (cycle between red, green, and blue)
- R - Clear the board

- Left Click - Fill in cell (supports dragging the cursor to color in squares)
- Right Click - Erase cell (supports dragging the cursor to color in squares)

- Q - Slow the game down
- W - Speed the game up

The game starts paused. You'll have to unpause with `P`.

Bonus:

- B - This is supposed to be unbounded growth with a fixed starting pattern. The borders of the game prevent this, though, because they're collidable.

 ![preview](https://github.com/H4CKY54CK/game-of-life/blob/master/preview.png)
