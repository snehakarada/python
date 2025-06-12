string = "hero"
reversedStr = ''
for index in range(len(string) - 1, -1, -1):
    reversedStr = reversedStr + string[index]
print("The reverse version of the string", string, "is ", reversedStr)