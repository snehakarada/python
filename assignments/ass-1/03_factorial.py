# Do not rename it, use this as input for your program.
# While testing we will change its value.
n = 4
# print factorial of n.
# Do not print anything else. Printing more than one output or printing anything other than factorial might will be consider as error.
# START YOUR CODE AFTER THIS LINE. DO NOT REMOVE THIS LINE
factorial = 1
# for (let number = n; number > 0; number--) {
#     factorial = factorial * number
# }

for number in range(n, 0, -1) :
    factorial = factorial * number

print(factorial)