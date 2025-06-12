""""
1.Rock 
2.Paper
3.Scissor
"""

import random
userName = input("Enter your name\n")
userChoice = int(input("What do you choose? Type\n1.Rock\n2.Paper\n3.Scissor\n"))
computerChoice = random.randint(1, 3)
print("computer choose", computerChoice)
if userChoice == 1 and computerChoice == 2 :
    print("computer is the winner")
elif userChoice == 2 and computerChoice == 1 :
    print(userName, "is the winner")
elif userChoice == 1 and computerChoice == 3 :
    print(userName, "is the winner")
elif userChoice == 3 and computerChoice == 1 :
    print("computer is the winner")
elif userChoice == 2 and computerChoice == 3 :
    print("computer is the winner")
elif userChoice == 3 and computerChoice == 2 :
    print(userName, "is the winner")
elif userChoice == computerChoice :
    print("The game is DRAW!")
else :
    print("Enter correct Input")

