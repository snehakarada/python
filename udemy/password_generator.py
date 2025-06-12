import random
from itertools import repeat
print("Welcome to Password Generator")
numberOfLetters = int(input("How many letters would you like in your password\n"))
numberOfSymbols = int(input("How many symbols would you like in your password\n"))
numberOfDigits = int(input("How many Numbers would you like in your password\n"))
str = "ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
letters = []
for char in str :
    letters.append(char)
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
numbers = ["0", "1", "2","3", "4", "5", "6", "7", "8", "9"]

password = ''
for i in range (numberOfLetters) :
    password += random.choice(letters)

for i in range (numberOfDigits) :
    password += random.choice(numbers)

for i in range (numberOfSymbols) :
    password += random.choice(symbols)


print("The password is ", password)
print("_" * 20)