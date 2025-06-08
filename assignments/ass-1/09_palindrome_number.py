a = 221
number = a
reverse = 0
while number > 0 :
    remainder = number % 10
    reverse = reverse * 10 + remainder 
    number = number // 10
if reverse == a :
    print(a, "is palindrome number")
else :
    print(a, "is not a palindrome number")