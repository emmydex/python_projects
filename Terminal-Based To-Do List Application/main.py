tasks = []            
list = [1,2,3,4,5]


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


    

    while True:
        try:
            # probably dont need a dictionary i think i can bind the function with a list 
            
            

            choose = int(input("choose an option "))    
            if choose not in list:
                print("not a valid input, try again")


                # trying to assign each input to call its respected function
            if choose == 1:
                new_task
            elif choose == 2:
                show_task
            elif choose == 3:
                mark_complete
            elif choose == 4:
                delete_task
            else:
                print("exiting program")
                    # exit_program
                continue    
            break
                                
        except ValueError:
            print(" oops!, not a valid input")



    

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
            

    # new_task()

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

    # mark_complete()

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

    # delete_task()

    def exit_program():
            print("closing program")








main_menu()
print(tasks)