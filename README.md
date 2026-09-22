# TaskTrack

TaskTrack is a command-line task manager created for CPS 310.

## Current Features

- Includes functionality for viewing and adding tasks to a list.
- Includes saving and loading tasks from a .txt file for future use post program termination.

## Requirements

- Python 3

## Project Files

- `tasktrack.py` - The central program script that contains all of the functionality we need.
- `tasks.txt` - The file tasktrack.py reads/writes from when loading/saving tasks.
- `.gitignore` - files that should not be pushed to the Git repository.

## Running the program
- Open a terminal in the project directory by going to ~/TaskTrack/ in file explorer, right clicking, and selecting "open in terminal."
- python `tasktrack.py`
- follow the prompted menu to use the program.
- (1) to view tasks added to your list
- (2) to add new tasks to the list
- (3) to exit the program

## Task Persistence

Tasks are loaded at the beginning of the program and then writen to `tasks.txt` after the add_tasks() function returns.

## Sample Interaction

Interact with the prompt provided to use the program.
- Pressing 1 on the keyboard views the tasks currently available.
- Pressing 2 on the keyboard adds new tasks to your list, and saves them to `tasks.txt`
- Pressing 3 exits the program.

## Current limitation
The program does not currently support "check list" functionality, there is no intermediary state between a task being added/removed. We could add a task "completed" state.