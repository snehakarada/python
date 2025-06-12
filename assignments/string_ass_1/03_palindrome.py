string = "pop"
reversedStr = ''
for index in range(len(string) - 1, -1, -1):
    reversedStr = reversedStr + string[index]
if (string == reversedStr) :
    print("it is palindrome string")
else :
    print("it is not a palindrome stirng")