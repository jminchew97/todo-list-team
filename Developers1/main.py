incompleteTasks = []
completeTasks = []

def showTasks():
    print(f"To-Do List: {incompleteTasks}")
    print(f"Completed Tasks: {completeTasks}")

def addTasks(task):
    incompleteTasks.append(task)
    print(f"Tasks successfully added! Here are your current tasks: {showTasks()}")

def completeTasks(task):
    completeTasks.append(task)

def deleteTasks(task):
    incompleteTasks.remove(task)

print(addTasks(task))