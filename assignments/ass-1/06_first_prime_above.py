prime = 19
value = prime + 1
while True :
    count = 0
    for i in range(1, value + 1) :
        if value % i == 0 : 
            count = count + 1
    if count == 2 : 
        print("The number is ", value)
        break
    value = value + 1