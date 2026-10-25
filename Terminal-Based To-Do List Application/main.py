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

try:

    choose = int(input("choose an option "))    
    if choose not in list:
        print("not a valid input")               
except:
    print(" oops!, not a valid input; try again")

# this function adds a new task and appends it to the tasks list
def new_task():
    task_input = input("enter new task ")
    tasks.append({"task": task_input, "Done": False})
    

    #this function is to validate input not having empty string or whitespace only
    def validate_task_input():
        if not task_input or not task_input.strip():
            print("cannot be empty or whitespace only.")
        else:
            print(f"task '{task_input}' added succesfully")

    validate_task_input()
    

new_task()

# there is a bug in this section: so i am saying if tasks is true it should print
# notasks available
def show_task():
    if tasks:
        print("no tasks available")
    else:
        print(f"This are all the added: {tasks}")

show_task()
