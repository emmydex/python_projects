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


def new_task():
    task_input = input("enter new task ")
    tasks.append({"task": task_input, "Done": False})
    print(f"task '{task_input}' added succesfully")

    #this function is to validate input not having empty string or whitespace only
    def validate_task_input(task_input):
        if not task_input or not task_input.strip():
            raise ValueError("cannot be empty or whitespace only.")

        return task_input

    validate_task_input(task_input)
    

new_task()
print(tasks)
