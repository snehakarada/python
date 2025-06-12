sentence = "This is cool"
reversedSentence = ""
words = sentence.split(' ')
for index in range(len(words) - 1, -1, -1) :
    print("is it there", index)
    reversedSentence = reversedSentence + " " + words[index]
print("The reversed sentence is ", reversedSentence)