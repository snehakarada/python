# Do not rename a and b, use them as input for your program.
# a and b will be whole numbers.
# While testing we will change their values.
a = 4
b = 27
# // Print the HCF of a and b
# // Printing more than one output or printing anything other than HCF might will be consider as error.
# // START YOUR CODE AFTER THIS LINE. DO NOT REMOVE THIS LINE
firstNumber = a
secondNumber= b
remainder = 1
while secondNumber > 0 :
    if remainder > 0 :
        remainder = firstNumber % secondNumber
        firstNumber = secondNumber
        secondNumber = remainder
    

print(firstNumber);