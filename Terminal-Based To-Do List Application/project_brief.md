# PROJECT BRIEF. Version 1
bulid a command-line application that allows users to manage everyday tasks. The applicaton must let users create, view, complete and delete tasks through a text-based menu.

# Main Objective
Build a working application independently while practising Python fundermentals.

# Project Requirements
These are the requirements the application must satisfy.
    treat each task below as a small development ticket. Work through them in order.

# TASK 1 -
Create the main menu.
User story: As a user, i want to see a menu so i can choose what action to perform.
    Requirments
    ▪ Display the application name.
    ▪ Display these options:
        ▪ Add a task
        ▪ view all tasks
        ▪ Mark a task as completed
        ▪ Delete a task
        ▪ Exit
    ▪ Ask the user to enter an option.
    ▪ Display a helpful message if the option is invalid.
    ▪ Keep displaying the menu until the user chooses to exit.
Acceptance criteria
    ▪ The menu appears when the program starts.
    ▪ Choosing an invalid option does not crash the application.
    ▪ Choosing Exit ends the program cleanly.

# TASK 2
User story: as a user, i want to see my tasks so i know what  needs to be done.
    Requirements
        ▪ Ask the user to enter a task description.
        ▪ Reject empty or whitespace -only descriptions.
        ▪ Store a valid task in the application's task collection.
        ▪ Confirm that the task was added successfully.
    Acceptance criteria
        ▪ A valid task is stored.
        ▪ An empty task is rejected.
        ▪ The user receives feedback for both success and failure.