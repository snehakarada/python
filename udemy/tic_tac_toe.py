def horizentalBorder(char, length) :
    return char * length + "\n"

def isEnd(number) :
    if number % 3 == 0 :
        return "|\n" * 2 + horizentalBorder("_", 21)
    return ''

def getBox(number) :
    return "|    " + str(number)

def getBoard() :
    board = ''
    for i in range(1, 10) :
        board += getBox(i) + isEnd(i)
    return board


def wholeBoard () :
    return horizentalBorder("_", 21) + getBoard()



def updateBoard(board, userChoice, symbol) :
    newBoard = ''
    for char in board :
        if char == userChoice :
            newBoard += symbol
        else :
            newBoard += char
    return newBoard

def inputPrompt(name) :
    return input(f"{name} : Enter your choice :- ")

def isValid(choice, board) : 
    return choice in board

def recoredMoves(choice, user1) :
    return user1 + choice

def checkWinner(choice) :
    combinations = ["123", "456", "789", "159", "357", "147", "258", "369"]
    print("The choice is", choice)
    for index in range(len(choice)) : 
        if choice[index : index + 3] in combinations :
            return True
    return False
    
def gameStart() :
    board = wholeBoard()
    print(board)
    user1Name= input("Enter player1 name\n")
    user2Name= input("Enter player2 name\n")
    user1 = ''
    user2 = ''
    count = 0
    while count <= 8 :
        choice = inputPrompt(user1Name)
        board = updateBoard(board, choice, "O")
        print(board)
        user1 = recoredMoves(choice, user1)
        if checkWinner(user1) :
            print(user1Name, "is the winner")
            break
        count += 1
        choice = inputPrompt(user2Name)
        board = updateBoard(board, choice, "X")
        print(board)
        user2 = recoredMoves(choice, user2)
        if checkWinner(user2) :
            print(user2Name, "is the winner")
            break
        count += 1


gameStart()
