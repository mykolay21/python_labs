from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
    # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift
    #  amount and print the decrypted text. e.g. cipher_text = "mjqqt" shift = 5 plain_text = "hello" print output:
    #  "The decoded text is hello"
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")


def encrypt_decrypt(text, direction, shift_amount):
    '''

    :param text:
    :param direction:
    :param shift_amount:
    :return:
    '''
    plain_text = ""

    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == 'encode':
                new_position = position + shift_amount
            elif direction == 'decode':
                new_position = position - shift_amount
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"The {direction}d text is {plain_text}")


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call
#  the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND*
#  decrypt a message.
if __name__ == '__main__':
    print(logo)
    should_continue = True
    while should_continue:

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26

        encrypt_decrypt(text=text, direction=direction, shift_amount=shift)

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if restart == "no":
            should_continue = False
            print("Goodbye")
