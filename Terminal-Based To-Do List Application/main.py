tasks = []            


# created the Main menu
# how do i keep displaying the menu until the user chooses to exit the application
def main_menu():
    print("----Terminal Based To-Do List----")
    print("----Main Menu----")
    print("1. Add a Task")
    print("2. view all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")



    # askiing the user to pick an option 
    list = {1 : new_task,
            2 : show_task,
            3 : mark_complete,
            4 : delete_task,
            5 : exit_program}


    # passing the continue to the if statement so if user chooses an option not in the list the continue keeps prompting the user
    # else the loop breaks and there is also an exption for a ValueError.
    while True:
        try:

            choose = int(input("choose an option "))    
            if choose not in list:
                print("not a valid input, try again")
                continue
            
            break
                            
        except ValueError:
            print(" oops!, not a valid input")

main_menu()

task_input = input("enter new task ")


# this function adds a new task and appends it to the tasks list

#1
def new_task(): 
    
    tasks.append({"task": task_input, "Done": False})
    

    #this function is to validate input not having empty string or whitespace only
    def validate_task_input():
        if not task_input or not task_input.strip():
            print("cannot be empty or whitespace only.")
        else:
            print(f"task '{task_input}' added succesfully")

    validate_task_input()
    

new_task()

#2
def show_task():
    for number, task in enumerate(tasks, start=1):
        if task_input :
            print(f"This are all the added tasks: {number}, {task}")
        else:
            print("no tasks available")

# show_task()

# this function shows the tasks and marks the selected ones as done

#3
def mark_complete():
    show_task()
    # i wrapped this in a while loop so i can catch the wrong input and prompt the user
    # to try again.
    while True:
        if not tasks:
            return

        try:
            index = int(input("Enter task number to mark done: "))-1
            if 0 >= index > len(tasks):
                print("invalid number!, try again")
                continue
                
            else:
                # i was calling the index of a lowercase ["done"] instead of ["Done"],
                # so it kept printing ["Done"] = False together with ["done"] = True
                tasks[index]["Done"] = True
                print("Marked as done!")
                break

                # this exeption should catch both the ValueError and IndexError
        except ValueError, IndexError:
            print("Please enter a valid number")

mark_complete()

#4
def delete_task():
    print(tasks)

    while True:
        if not tasks:
            return

        try:
            # i have to minus 1 from the input cause indexing starts at 0
            delete = int(input("Select task to delete: "))-1
            if 0 >= delete > len(tasks):
                print("invalid input, try again")
                continue
            else:
                del_task = tasks.pop(delete)
                print("task successfully deleted")
            break

        except ValueError, IndexError:
            print("Enter a valid input")

delete_task()

def exit_program():
    print("closing program")

print(tasks)