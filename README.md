# U.S. States Game

This is an educational game built with Python that helps users learn the names and locations of all 50 U.S. states. The game uses a blank map of the United States and prompts the player to name as many states as they can.

## Features

- Interactive map of the United States
- User input for guessing state names
- Visual feedback by placing state names on the map
- Score tracking
- Option to exit the game and save progress
- Generation of a CSV file with missed states for further learning

## Files

- `main.py`: The main game script
- `50_states.csv`: CSV file containing state names and their coordinates on the map
- `blank_states_img.gif`: Image file of the blank U.S. map
- `states_to_learn.csv`: Generated CSV file with states the player didn't guess

## Requirements

- Python 3.x
- pandas library
- turtle graphics library

## How to Run

1. Ensure you have Python installed on your system.
2. Install the required libraries:
   ```
   pip install pandas
   ```
3. Place all files in the same directory.
4. Run the game by executing the `main.py` file:
   ```
   python main.py
   ```

## How to Play

1. When prompted, type in the name of a U.S. state.
2. If correct, the state name will appear on the map.
3. Continue guessing state names.
4. To exit the game, type 'Exit' when prompted for a state name.

## Game Mechanics

- The game continues until all 50 states are guessed or the player chooses to exit.
- The current score is displayed as "[number of correct guesses]/50 Correct States".
- When exiting, the game generates a `states_to_learn.csv` file containing the names of states that were not guessed.

## Customization

You can customize the game by modifying the following:

- Update `50_states.csv` to change state coordinates or add/remove states.
- Replace `blank_states_img.gif` with a different map image (ensure coordinates in CSV file match).
- Modify `main.py` to add features like time limits, hints, or difficulty levels.

## Contributing

Feel free to fork this project and make your own modifications. Some ideas for enhancements:
- Add difficulty levels (e.g., time limits, spelling strictness)
- Include state capitals or other geographical features
- Create a graphical user interface for a more interactive experience
- Add sound effects or background music
- Implement a high score system

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
