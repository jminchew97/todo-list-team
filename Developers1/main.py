incompleteTasks = []
completeTasks = []


def addTasks(task):
    incompleteTasks.append(task)

def completeTasks(task):
    completeTasks.append(task)

def deleteTasks(task):
    incompleteTasks.remove(task)

print(addTasks(task))