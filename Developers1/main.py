incompleteTasks = []
completeTasks = []

def greeting():
    print("Welcome to your task manager: Select an option: ")
    print("1: Add Tasks")
    print("2: Delete Tasks")
    print("3: View Completed Tasks \n")
    showTasks()

    choice = input("")

    if choice == "1":
        addTasks()
    elif choice == "2":
        deleteTasks()
    elif choice == "3":
        showTasks()
    else:
        print("Invalid Input")


def showTasks():
    print(f"To-Do List: {incompleteTasks}")
    print(f"Completed Tasks: {completeTasks}")



def addTasks():
    task = input("Enter Task: ")
    incompleteTasks.append(task)
    print(f"Tasks successfully added! Here are your current tasks: {incompleteTasks}")

    print("Select an option: ")
    print("1: Add Tasks")
    print("2: Delete Tasks")
    print("3: View Completed Tasks \n")
    showTasks()

    choice = input("")

    if choice == "1":
        addTasks()
    elif choice == "2":
        deleteTasks()
    elif choice == "3":
        showTasks()
    else:
        print("Invalid Input")

    
def completeTasks():
    task = input("Which task is completed? ")
    print("Congrats, task completed")
    completeTasks.append(task)
    incompleteTasks.remove(task)

    print("Select an option: ")
    print("1: Add Tasks")
    print("2: Delete Tasks")
    print("3: View Completed Tasks \n")
    showTasks()

    choice = input("")

    if choice == "1":
        addTasks()
    elif choice == "2":
        deleteTasks()
    elif choice == "3":
        showTasks()
    else:
        print("Invalid Input")


def deleteTasks():
    task = input("Which tasks do you want to delete? ")
    incompleteTasks.remove(task)

    print("Select an option: ")
    print("1: Add Tasks")
    print("2: Delete Tasks")
    print("3: View Completed Tasks \n")
    showTasks()

    choice = input("")

    if choice == "1":
        addTasks()
    elif choice == "2":
        deleteTasks()
    elif choice == "3":
        showTasks()
    else:
        print("Invalid Input")

greeting()
#addTasks("testing")