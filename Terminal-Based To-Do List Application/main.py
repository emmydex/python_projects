import sys
tasks = []            


    # this function adds a new task and appends it to the tasks list
  



def new_task():
    while True:
        task_input = input("enter new task ")
        # used the strip() method to catch whitespaces
        if not task_input or not task_input.strip():
            print("can not be empty or whitespace")
            continue

        tasks.append({"task": task_input, "Done": False})
        print(f"Task '{task_input}' added successfully.")
        break
            


# this function shows the tasks available
def show_task():
            # the if statement checks if the list is empty before entering the for loop
            if not tasks:
                 print("list is empty")
            else:
            # the enumerate gives each task a visible number 
                for number, task in enumerate(tasks, start=1):
                    # instead of using the task_input, i could use tasks and check if the list is occupied
                    if tasks :
                        print(f"This are all the added tasks: {number}, {task}")  
                    else:
                        print("no tasks available")


        # this function shows the tasks and marks the selected ones as done

    
def mark_complete():
        # this displays all visible tasks 
        show_task()
            # i wrapped this in a while loop so i can catch the wrong input and prompt the user
            # to try again.
        while True:
            if not tasks:
                print("no visible task")
                return

            try:
                index = int(input("Enter task number to mark done: "))-1
                # this condition is logically incorrect 
                # fixed negative and out-of-range task selections
                if  index > len(tasks) or index <= 0:
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
                
# a new bug has showed its face as the program does not stop completely when i end the program 

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

                except (ValueError, IndexError):
                    print("Enter a valid input")


# used the import sys and the .exit() 
def exit_program():
            print("exiting program goodbye")
            sys.exit()

    

# created the Main menu
# how do i keep displaying the menu until the user chooses to exit the application
   
def main_menu():
    while True:
        print("----Terminal Based To-Do List----")
        print("----Main Menu----")
        print("1. Add a Task")
        print("2. view all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")


        # i renamed the variable and moved the dictionary outside the loop
        option_list = {1 : new_task, 2 : show_task, 3 : mark_complete, 4 : delete_task, 5 : exit_program}

        while True:
            try:
                choose = int(input("choose an option "))    
                if choose not in option_list:
                    print("not a valid input, try again")
                    continue
                
                elif choose in option_list:
                    option_list[choose]() # calls the function

                    # placed the statement inside the elif block 
                    if choose == 5:
                         break
                
                
                                    
            except ValueError:
                print(" oops!, not a valid input")
        


main_menu()

    





print(tasks)