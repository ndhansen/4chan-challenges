print("Write the text you want encrypted:")
print("Note: It will be converted to lowercase.")
text = input("> ").lower()

def caesar_shift(text, shift):
    while shift > 26:
        shift -= 26
    while shift < 0:
        shift += 26

    result = ""
    for char in text:
        if ord(char) >= 97 and ord(char) <= 122:
            newletter = ord(char) + shift
            if newletter > 122:
                newletter -= 26
            result += chr(newletter)
        else:
            result += char
    return result

def vigenere_encode(text, encryption_text):
    while len(encryption_text) < len(text):
        encryption_text += encryption_text * 2
    result = ""
    for i in range(len(text)):
        if ord(text[i]) >= 97 and ord(text[i]) <= 122:
            newletter = ord(text[i]) + ord(encryption_text[i]) - 97
            if newletter > 122:
                newletter -= 26
            result += chr(newletter)
        else:
            result += text[i]
    return result

def vigenere_decode(cypher, enc_text):
    while len(enc_text) < len(cypher):
        enc_text += enc_text * 2
    result = ""
    for i in range(len(text)):
        if ord(cypher[i]) >= 97 and ord(cypher[i]) <= 122:
            newletter = ord(cypher[i]) - ord(enc_text[i]) + 97
            if newletter < 97:
                newletter += 26
            result += chr(newletter)
        else:
            result += cypher[i]
    return result

print("First, caesar.")
shift = int(input("What shift should be used? "))
caesar = caesar_shift(text, shift)
print(caesar)

print("Next, vigenere.")
print("please enter a text to encrypt the string. the longer the better.")
encryption_text = input("> ").lower()
vigenere = vigenere_encode(text, encryption_text)
print(vigenere)
old_text = vigenere_decode(vigenere, encryption_text)
print(old_text)
