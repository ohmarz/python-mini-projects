import time

time.sleep(0.3)
print("=====", "TO-DO LIST📋".center(70), "=====")
print()

class ToDo():
    def __init__(self):
        self.tasks = []
        self.read_file()

    def read_file(self):
        try:
            with open("tasks.txt", "r") as f:
                self.tasks = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            # create an empty list for the tasks
            self.tasks = []


    def save_file(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task+"\n")

    def add_task(self, task):
        if task == "q":
            return False

        if not task:
            time.sleep(0.3)
            print("*****" * 15)
            print("Can't add empty task⚠️")
            print("*****" * 15)
            return None

        self.tasks.append(task)
        print(f"Added: {task} ☑️")
        self.save_file()
        return True


    def view_tasks(self):
        print("TASKS".center(50))

        if not self.tasks:
            time.sleep(0.3)
            print("*****"*15)
            print("No tasks yet⚠️")
            print("*****" * 15)

        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")


    def delete_task(self, task):
        print("Deleting task".center(50))

        if task == "q":
            return False

        if not self.tasks:
                time.sleep(0.3)
                print("*****" * 15)
                print("No tasks yet⚠️")
                print("*****" * 15)
                return
        if task in self.tasks:
                self.tasks.remove(task)
                self.save_file()
                print(f"Deleted: {task}☑️")
        else:
            time.sleep(0.3)
            print("*****" * 15)
            print("Task NOT found⚠️. \nHere's the list of tasks")
            self.view_tasks()
            print("*****" * 15)


todo_list = ToDo()

while True:
    time.sleep(0.3)
    menu = ["A: Add Task", "B: View Tasks", "C: Delete Tasks", "D: Exit"]
    print()
    print("MENU📋".center(50))
    for m in menu:
        print(m)

    print()
    option = input("Select an option📋(A/B/C/D): ").upper()
    match option:
        case "A":
            print()
            time.sleep(0.3)
            task = input("Enter a task (q to quit): ").lower().strip()
            todo_list.add_task(task)
        case "B":
            todo_list.view_tasks()
        case "C":
            print()
            time.sleep(0.3)
            task = input("Enter a task to delete🚮 (q to quit): ").lower().strip()
            todo_list.delete_task(task)
        case "D":
            break
        case _:
            time.sleep(0.3)
            print("Invalid option")

    print()
    time.sleep(0.3)
    print("=====" * 15)
    main_return = input("Return to main menu? (y/n): ").lower()
    print("=====" * 15)
    if main_return != "y":
        print("Exiting...")
        time.sleep(0.3)
        print("BYEEEEEE👋👋")
        time.sleep(0.3)
        break
