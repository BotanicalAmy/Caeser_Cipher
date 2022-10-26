alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    #get positions of the characters
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = position + shift_amount
                if new_position > 26:
                    new_letter = alphabet[new_position - 26]
                else:
                    new_letter = alphabet[new_position]
                end_text += new_letter
    
            elif cipher_direction == "decode":
                new_position = position - shift_amount
                new_letter = alphabet[new_position]
                end_text += new_letter
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text} \n ")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    start_over =input("Type 'yes' if you want to go again.  Otherwise type 'no'.\n")
    if start_over == "no":
        should_continue = False
        print("Goodbye")