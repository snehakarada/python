a = 6   
count = a
first = 0
second = 1
while count > 0 :
    third = first + second
    first = second
    second = third
    count = count - 1
print("the vlaues is", first)