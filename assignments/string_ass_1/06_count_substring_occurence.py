string = "daauplicate"
subString = "aa"
count = 0
for index in range(0, len(string)) :
    if string[index : index + len(subString)] == subString :
        count += 1
print("The number of ", subString, "is ", count)