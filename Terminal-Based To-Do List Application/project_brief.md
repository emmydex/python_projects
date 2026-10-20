# PROJECT BRIEF. Version 1
bulid a command-line application that allows users to manage everyday tasks. The applicaton must let users create, view, complete and delete tasks through a text-based menu.

# Main Objective
Build a working application independently while practising Python fundermentals.

# Project Requirements
These are the requirements the application must satisfy.
    treat each task below as a small development ticket. Work through them in order.

# TASK 1 - Create the main menu.
~ Priority: High
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

# TASK 2 - ADD A NEW TASK
~ Priority: High
User story: as a user, i want to add a task so i can remember something i need to do.
    Requirements
        ▪ Ask the user to enter a task description.
        ▪ Reject empty or whitespace -only descriptions.
        ▪ Store a valid task in the application's task collection.
        ▪ Confirm that the task was added successfully.
    Acceptance criteria
        ▪ A valid task is stored.
        ▪ An empty task is rejected.
        ▪ The user receives feedback for both success and failure.

# TASK 3 - VIEW ALL TASKS
~ Priority: High
User story: As a user, i want to see my tasks so i know what  needs to be done.
    Requirements
        ▪ Display every stored task
        ▪ Give each task a  visible number or identifier.
        ▪ Show whether each task is pending or completed.
        ▪ Display a helpful message whenno tasks exist.
    Acceptance criteria
        ▪ All stored tasks are displayed.
        ▪ Each task's status is visible.
        ▪ An empty task collection is handled correctly.

# TASK 4 - MARK A TASK AS COMPLETED
~ Priority: medium
User story: As a user, i want to mark a task as completed so i can track my progress.
    Requirements
        ▪ Display the available tasks or their identifiers.
        ▪ Ask which task the user wants to complete.
        ▪ Update the selected task's status.
        ▪ Handle invalid identifiers and already-completed tasks gracefully.
    Acceptance criteria
        ▪ The correct task is marked completed.
        ▪ Other tasks remain unchanged.
        ▪ Invalid selections do not crash the application.

# TASK 5 - DELETE A TASK
~ Priority: Medium
User story: As a user, i want to delete a task i no longer need
    Requirements
        ▪ Allow the userto select a task.
        ▪ Remove the selected task from the collection.
        ▪ Confirm successful deletion.
        ▪ Handle invalid selections and an empty task collection.
    Acceptance criteria
        ▪ Only the selected task is deleted.
        ▪ The remaining tasks can still be viewed.
        ▪ Invalid selections are handled safely.

# TASK 6 - HANDLE ERRORS AND EDGE CASES
User story: As a user, i want the application to handle mistakes without unexpectedly crashing.
    Requirments
        ▪ Handle non-numeric input when  a number is required.
        ▪ Handle task identifiers that do not exist.
        ▪ Handle attempts to complete or delete tasks when no tasks exist
        ▪ Keep the application usable after invalid input.
    acceptance criteria
        ▪ Expected user mistakes produce helpful messages.
        ▪ The program continues running when it can safely recover.