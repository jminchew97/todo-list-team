incompleteTasks = []
completeTasks = []

def greeting():
    print("Welcome to your task manager: Select an option: ")
    print("1: Add Tasks")
    print("2: Delete Tasks")
    print("3: View Completed Tasks \n")
    showTasks()

    choice = input("test")


def showTasks():
    print(f"To-Do List: {incompleteTasks}")
    print(f"Completed Tasks: {completeTasks}")

def addTasks(task):
    incompleteTasks.append(task)
    return(print(f"Tasks successfully added! Here are your current tasks: {incompleteTasks}"))
    

def completeTasks(task):
    completeTasks.append(task)

def deleteTasks(task):
    incompleteTasks.remove(task)

greeting()
#addTasks("testing")