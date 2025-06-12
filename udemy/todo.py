class Todo :
    def __init__(self, todo, count) :
        self.todo = todo
        self.count = count

    def addTask(self,taskName) :
        self.count += 1
        self.todo.update({self.count : {"name" : taskName, "status" : "undone"}})
    
    def removeTask(self, id) :
        self.todo.pop(id)
        self.count -= 1
    
    def toggleTask(self, id) :
        print(self.todo)
        print("hello", self.todo, self.todo[id]["status"])
        self.todo[id]["status"] = "undone" if self.todo[id]["status"] == "done" else "done"
    
    def showTodo(self) :
        print("The Tasks are\n" + "*" * 20 + "\nS.No" +  " " * 5 + "Task name" + " " * 5 + "status" + " " * 5)
        for k, v in self.todo.items():
            print(k , " " * 6 , v["name"] , " " * 6 , v["status"])
        print("*" * 20)

    def validation(taskNumber, todo) :
        return taskNumber in todo

def handleAddTask(list) :
    taskName = input("Enter your Task Name :- ")
    list.addTask(taskName)
    print("-" * 10 , "task added successfully ", "-" * 10 )

def handleRemoveTask(list) :
    taskNumber = int(input("Enter the task number :- "))
    list.removeTask(taskNumber)
    print("-" * 10 , "task removed successfully", "-" * 10)

def handleToggleTask(list) :
    taskNumber = int(input("Enter the task number:- "))
    list.toggleTask(taskNumber)
    print("-"* 10, "Task toggled successfully", "-" * 10)

def functionalities(list) :
    number = int(input("Enter respective number to perform the action\n 1. add Task\n 2. Remove Task\n 3. Toggle Task\n 4. Show\n 5. Exit\n Your choice :- "))
    match number :
        case 1 :
            handleAddTask(list)
        case 2:
            handleRemoveTask(list)
        case 3 :
            handleToggleTask(list)
        case 4 :
            list.showTodo()
        case 5 :
            return "Bye"
        case _:
            print("invalid option")
    return functionalities(list)
    
def main() :
    print("*" * 10, "Hello Welcome to MY TODO", "*" * 10)
    list = Todo({}, 0)
    print(functionalities(list))

main()