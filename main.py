alphabet_extended = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@','#', '$', '%', '&', '(', ')', '*', '+']

from art import logo
print(logo)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    #get positions of the characters
    for char in start_text:
        if char in alphabet_extended:
            position = alphabet_extended.index(char)
            if cipher_direction == "encode":
                new_position = position + shift_amount
                if new_position > 46:
                    new_char = alphabet_extended[new_position - 46]
                else:
                    new_char = alphabet_extended[new_position]
                end_text += new_char
    
            elif cipher_direction == "decode":
                new_position = position - shift_amount
                new_char = alphabet_extended[new_position]
                end_text += new_char
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text} \n ")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 46

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    start_over =input("Type 'yes' if you want to go again.  Otherwise type 'no'.\n")
    if start_over == "no":
        should_continue = False
        print("Goodbye")