start = 1
end = 10
for i in range(start, end) :
    count = 0
    for j in range(1, i + 1) :
        if i % j == 0 : 
            count = count + 1
    if count == 2 : print("*************** numbers are *******************", i)