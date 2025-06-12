direction = input("Welcome to Treasure Island.\nYour mission is to find the Treasure\nYou're at a cross road. Where do you want to go?\nType 'left' or 'right'\n")
if direction == "left" :
    instruction = input("You've came to a lake. There is an island in the middle of the lake.\n Type 'wait' to wait for the boat.Type 'swim' to swim across\n")
    if instruction == "wait" :
        doorColor = input("You arrive at the island unharmed. There is a house with 3 doors.One red, one yellow and one blue. Which colour do you choose?\n")
        if doorColor == "red" :
            print("It's a room full of fire. Game Over. ")
        elif doorColor == "yellow" :
            print("You found the treasure! You Win! ")
        elif doorColor == "blue" :
            print("You enter a room of beasts. Game Over. ")
    else :
        print("You get attacked by an angry trout. Game Over. ")

else :
    print("You fell into a hole. Game Over. ")
