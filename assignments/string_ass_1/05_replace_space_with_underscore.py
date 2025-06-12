string = "hi hello namaste"
replacedStr = ''
for char in string :
    if char == ' ' :
        replacedStr += '_'
    else :
        replacedStr += char
print("The replaced string is", replacedStr)