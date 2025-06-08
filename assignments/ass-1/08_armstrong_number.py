a = 13
number = a
sum = 0
while number > 0 :
    remainder = number % 10
    sum = sum + remainder * remainder * remainder
    number = number //  10
if sum == a :
    print(a, "is an armstrong number")
else :
    print(a, "is not an armstrong number")