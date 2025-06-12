
def encodeMessage(message, shiftNumber, letters) :
    encodedMsg = ''
    for char in message :
        if char not in letters :
            encodedMsg += char
            continue
        value = letters.index(char) + shiftNumber
        if value > 26 :
            value = value - 26
        encodedMsg += letters[value]
    return encodedMsg

def decodedMessage(message, shiftNumber, letters) :
    decodedMsg = ''
    for char in message :
        if char not in letters :
            decodedMsg += char
            continue
        value = letters.index(char) - shiftNumber
        if value <= 0 :
            value = 26 + value
        decodedMsg += letters[value]      
    return decodedMsg  
        
def main(flag) :
    category = input("Type encode to encrpt, Type decode to decrypt\n")
    message = input("Type your message\n").lower()
    shiftNumber = int(input("Type the shift number\n"))
    letters = list("_abcdefghijklmnopqrstuvwxyz")

    if not flag :
        return ''
    if (category == 'encode') :
        print("The encoded message is", encodeMessage(message, shiftNumber, letters))
    if (category == 'decode') :
        print("The decoded message is ", decodedMessage(message, shiftNumber, letters))
    flag = input("Type 'True' if you want to go again. Otherwise type 'False\n")
    main(flag)
    
main(True)