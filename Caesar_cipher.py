# text using for message encrypt, shift using for 
def caesar_encrypt(text, shift):
    result = "" # blank String for message 
    for char in text :
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else :
            result += char
    return result

def caesar_decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char

    return result


message = input("Enter Message: ")
shift = 5

encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)
print("You Message: " , message)
print("You encrypted message: ", encrypted)
print("You encrypted message: ", decrypted)