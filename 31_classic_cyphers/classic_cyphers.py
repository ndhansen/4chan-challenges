print("Write the text you want encrypted:")
print("Note: It will be converted to lowercase.")
text = input("> ").lower()

def caesar_shift(text, shift):
    while shift > 26:
        shift -= 26
    while shift < 1:
        shift += 26

    result = ""
    for char in text:
        if ord(char) >= 97 and ord(char) <= 122:
            newletter = ord(char) + shift
            if newletter > 122:
                newletter -= 26
            result += chr(ord(char) + shift)
        else:
            result += char
    return result

def vigenere_cypher(text, encryption_text):
    while encryption_text < text:
        encryption_text += encryption_text * 2
    result = ""
    for i in range(len(text)):
        if ord(text[i]) >= 97 and ord(text[i]) <= 122:
            result += chr(ord(char) + ord(encryption_text[i])
        else:
            result += char
    return result

print("First, caesar.")
shift = int(input("What shift should be used? "))
caesar = caesar_shift(text, shift)
print(caesar)

print("Next, vigenere.")
print("please enter a text to encrypt the string. the longer the better.")
encryption_text = input("> ").lower()
vigenere = vigenere_cypher(text, encryption_text)
print(vigenere)
