tasks = []


def new_task():
    while True:
        task_input = input("enter new task ")
        if not task_input:
            print("can not be empty or whitespace")
            continue

        tasks.append({"task": task_input, "Done": False})
        print(f"Task '{task_input}' added successfully.")
        break