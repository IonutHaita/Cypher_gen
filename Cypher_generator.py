alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', ',', '<', '>', '/', '?', ';', ':', '"', '|', '[', '{', ']', '}', '-', '+', '`', '~', '!', '@', '#', '$', '%', '^', '&', '(', ')', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = ""



def encrypt(text):
    ori_text = input("Type your message to be encrypted: \n")
    shift_no = int(input("Enter the shift number:\n"))

    for letter in ori_text:
        index = alphabet.index(letter)
        print(index)
        text += alphabet[index + shift_no]
    return text

def decrypt(text):
    ori_text = input("Type your message to be decrypted: \n")
    shift_no = int(input("Enter the shift number:\n"))

    for letter in ori_text:
        index = alphabet.index(letter)
        print(index)
        text += alphabet[index - shift_no]
    return text


decision = input("Please type encrypt to encrypt a message or decrypt to decrypt one:\n")
if decision == "encrypt":
    modified_text = encrypt(text)
    print(modified_text)
elif decision == "decrypt":
    modified_text = decrypt(text)
    print(modified_text)
else:
    print("Invalid input, try again!")
