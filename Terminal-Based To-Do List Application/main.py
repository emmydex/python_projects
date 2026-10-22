task = []            


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
list = [1,2,3,4,5]
print(list)
print(list[1])
try:
# askiing the user to pick an option
    choose = int(input("choose an option"))    
    if choose != [1,2,3,4,5]:
        print("not a valid input")
                
except:
    print(" oops!, that is not a valid option; try again")
