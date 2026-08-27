from base64 import encodebytes, decodebytes
from email.mime import base


print("Welcome to the Caesar Cipher Program!")
print("This program allows you to encrypt and decrypt messages using the Caesar cipher technique.")



def encode(message, shift):
    encoded_message = ""
    for char in message:
        if char.isupper():
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_char = char
        encoded_message += encrypted_char
    print("Encoded message:", encoded_message)
    

def decode(message, shift):
    decoded_message = ""
    for char in message:
        if char.isupper():
            base = ord('A')
            new_pos = (ord(char) - base -shift) % 26
            decrypted_char = chr(new_pos + base)
        elif char.islower():
            base = ord('a')
            new_pos = (ord(char) - base -shift) % 26
            decrypted_char = chr(new_pos + base)
        else:
            decrypted_char = char
        decoded_message += decrypted_char
    print("Decoded message:", decoded_message)
    


while  True:
    choice1 = input("To encrypt type 'encode' and to decrypt type 'decode': ").lower()
    Shift = int(input("Enter the shift value (1-25): "))
    Message = input("Enter the message: ")

    if choice1 == "encode":
        print("Encoded message:", encode(Message, Shift))
    elif choice1 == "decode":
        print("Decoded message:", decode(Message, Shift))
    else:
        print("Invalid choice. Please try again.")

    exit_choice = input("Do you want to continue? (yes/no): ").lower()
    if exit_choice != "yes":
        print("Exiting the program. Goodbye!")
        break
