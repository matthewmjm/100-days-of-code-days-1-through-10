alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    if direction.lower() == "encode":
        plain_list = [char for char in text]
        cipher_list = []
        for letter in plain_list:
            original = (alphabet.index(letter))
            if original + shift > 25:
                original = original - 26
            encode = alphabet[original + shift]
            cipher_list.append(encode)
        string1 = ""
        cipher_text = string1.join(cipher_list)
        print(f"The encoded text is {cipher_text}.\n")
    else:
        decrypt_text = ""
        for letter in plain_text:
            position = (alphabet.index(letter))
            if position - shift < 0:
                position = position + 26
            decrypt_text += alphabet[position - shift]
        print(f"The decoded text is {decrypt_text}.\n")

from art import logo
print(logo)

should_end = False
while not should_end:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    encrypt(plain_text=text, shift_amount=shift)

    restart = input("Type 'yes' if you want to go again.  Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye!")