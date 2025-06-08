# Do not rename p, r or t, use them as input for your program.
# While testing we will change their values.
p = 100
r = 5
t = 2    
# Print the compound interest.
# Do not use compound interest formula to calculate the compound interest.
# Use simple interest formula and a loop to calculate the compound interest.
# START YOUR CODE AFTER THIS LINE. DO NOT REMOVE THIS LINE
compoundIntrest = 0
principal = p

for time in range(t):
    intrest = (principal * r) / 100
    principal = principal + intrest

compoundIntrest = principal - p
print(compoundIntrest)