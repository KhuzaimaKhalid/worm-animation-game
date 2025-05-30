# Worm Animation Game

This project is a Python Pygame simulation of a segmented worm that follows your mouse cursor.  
The worm's body is made up of segments that smoothly follow the head, mimicking real worm or snake movement.

## Features

- Smooth, natural worm animation using segment following ("inverse kinematics")
- Worm head tracks the mouse cursor
- Body curves and wiggles naturally, even on sharp turns
- Simple mouse button status display

## How to Run

1. Make sure Python and [Pygame](https://www.pygame.org/) are installed:

    ```bash
    pip install pygame
    ```

2. Run the script:

    ```bash
    python worm_follow_cursor.py
    ```

3. Move your mouse in the window to see the worm follow the cursor.

## Screenshot

![Screenshot](screenshot.png) <!-- Replace with your own screenshot if needed -->

## Code Overview

- `update_worm(...)`: Moves the worm's head toward the mouse and updates each segment to follow the previous one.
- `draw_worm(...)`: Draws the worm segments and legs.
- Mouse buttons are tracked and displayed on the screen.

## Customization

- Change `SEGMENTS` and `LENGTH` to make the worm longer, shorter, or smoother.
- Adjust colors or add more effects as you wish.

## License

MIT License
