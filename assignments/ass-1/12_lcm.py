a = 4
b = 3
lcm = 1
number1 = a
number2 = b
factor = 2

while factor <= number1 or factor <= number2 :
    if number1 % factor == 0 and number2 % factor == 0 :
        number1 = number1 // factor
        number2 = number2 // factor
        lcm = lcm * factor
        continue
    factor = factor + 1

lcm = lcm * number1 * number2
print("The lcm of", a, "and", b , "is ", lcm)