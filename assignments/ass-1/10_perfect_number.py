a = 12
sum = 0
for i in range(1, a + 1) :
    if a % i == 0 :
        sum = sum + i
if sum == a :
    print(a, "is perfect number")
else :
    print(a, "is not perfect number")