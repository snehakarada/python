string = "Bhgya"
charToFind = "l"
for index in range(1, len(string)) :
    if string[index] == charToFind:
        print("the index of character is", index)
        break
    if string[index] != charToFind and index == len(string) - 1 :
        print(-1)
