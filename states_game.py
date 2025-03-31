#!/usr/bin/env python3
"""
usStateGame.py - A simple game to identify US states on a map using turtle graphics.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/31
License: MIT
Dependencies: pandas, turtle (Python libraries)

Description:
This script is a US state guessing game where users enter the name of a state,
and if it's correct, the state is displayed on a map. It utilizes turtle graphics
to show the state name on a background map with the correct coordinates.

The script performs the following:
1. Displays a map with US states.
2. Prompts the user to enter a state.
3. Checks if the entered state is valid.
4. If valid, the script displays the state's name at the corresponding coordinates on the map.

Usage:
Run the script and follow the prompts:
    python usStateGame.py

Example Output:
    Enter an US State: California
    (State is displayed at the correct coordinates on the map)
"""

# Import necessary libraries
import turtle
from state import State  # Import the State class from the state module
from process_data import check_state  # Import the check_state function from the process_data module


def main():
    # Set up the turtle screen
    screen = turtle.Screen()
    screen.title("Pantalla con Background en Turtle")  # Set the window title
    screen.setup(width=800, height=600)  # Set the screen size

    # Set the background image
    background_image = "blank_states_img.gif"  # Path to the background image
    screen.bgpic(background_image)  # Load the background image on the screen

    game_active = True  # Variable to keep the game running
    while game_active:
        # Prompt user for input
        us_state_input = turtle.textinput("US State game", "Enter an US State")  # Ask for user input (US state)

        # Create a State object
        us_state = State()  # Create a new instance of the State class

        # Get the coordinates (x, y) for the entered state
        x, y = check_state(us_state_input)  # Use check_state to find coordinates for the state

        # If valid coordinates are found (x != 0), display the state on the screen
        if x != 0:
            us_state.write_state(us_state_input, x, y)  # Write the state on the screen at (x, y)

    # Finish the turtle graphics session
    turtle.done()


# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    main()  # Call the main function to start the game

