const counter = () => {
    let count = 0;
    return () => {
        count++
        return count
    }
}

const taskManagement = (idCount: () => number, todo: {}) => {
    const number = Number(prompt("Enter respective number to perform the action\n 1. add Task\n 2. Remove Task\n 3. Mark Task as done\n 4. Mark Task as undone\n 5. Show\n 6.Exit\n Your choice :- "))
    const boarder = "-".repeat(10)
    switch (number) {
        case 1:
            const taskName = prompt("Enter the task name")
            todo[idCount()] = { taskName, status: "undone" }
            console.log(boarder + "task added successfully" + boarder)
            break;
        case 5:
            console.log(todo)
            break;
        default:
            console.log("invalid option")
    }


}

const main = () => {
    const todo = {}
    const idCount = counter()
    taskManagement(idCount, todo)
}

main()