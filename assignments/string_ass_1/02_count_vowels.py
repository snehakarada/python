string = "bhagya lakshmi"
vowels = 'aeiou'
count = 0
for char in string :
    if char in vowels :
        count += 1
print("The count of vowels in", string, "are", count)