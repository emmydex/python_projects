tasks = []


def new_task():
    while True:
                    task_input = input("enter new task ") 
                    tasks.append({"task": task_input, "Done": False})
                    
    
                    #this function is to validate input not having empty string or whitespace only
                    def validate_task_input():
                        
                        try:
                            if not task_input or not task_input.strip():
                                print("cannot be empty or whitespace only.")
                                # continue
    
                            else:
                                print(f"task '{task_input}' added succesfully")
                            break
                        except ValueError, IndexError:
                            print("try again")
    
                    validate_task_input()