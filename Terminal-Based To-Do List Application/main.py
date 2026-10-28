tasks = []            


# created the Main menu
def main_menu():
    print("----Terminal Based To-Do List----")
    print("----Main Menu----")
    print("1. Add a Task")
    print("2. view all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

main_menu()

# askiing the user to pick an option
list = [1,2,3,4,5]


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


task_input = input("enter new task ")


# this function adds a new task and appends it to the tasks list
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

def show_task():
    if task_input :
        print(f"This are all the added: {tasks}")
    else:
        print("no tasks available")

show_task()

# this function shows the tasks and marks the selected ones as done
def mark_complete():
    show_task()



mark_complete()