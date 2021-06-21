"""
This is a basic Caesar cipher.
Enter a message into the hide_message function and the encryption will take place.
Use the unhide_message to decrypt the message.
"""

alpha_string = 'abcdefghijklmnopqrstuvwxyz '

# Provides a numbered dictionary of the alphabet
alph_dict = {}
for number, letter in enumerate(alpha_string):
    alph_dict[letter] = number


# Returns a dictionary that has the alphabet numbers shifted according to how many places you specify
def get_encrypted_dict(input_string, num_letters_shifted):
    new_string = input_string[num_letters_shifted:] + input_string[:num_letters_shifted]
    shifted_dict = {}
    for num, let in enumerate(new_string):
        shifted_dict[num] = let

    return shifted_dict


def get_reverse_dict(input_dict):
    return dict([(value, key) for key, value in input_dict.items()])


def hide_message(message, shift_amount=5):
    text = ''
    new_cypher = get_encrypted_dict(alpha_string, shift_amount)
    for x in message.lower():
        text = text + new_cypher[alph_dict[x]]

    return text


def unhide_message(message, shift_amount=5):
    text = ''
    reverse_cypher = get_reverse_dict(get_encrypted_dict(alpha_string, shift_amount))
    reverse_base_dict = get_reverse_dict(alph_dict)
    for x in message:
        key = reverse_cypher[x]
        text = text + reverse_base_dict[key]

    return text


if __name__ == "__main__":
    secret_message = "this is a test"
    print(f"The secret message is: {secret_message}")

    hidden = hide_message(secret_message)
    print(f"The encrypted message is: {hidden}")

    unhidden = unhide_message(hidden)
    print(f"The decrypted message is: {unhidden}")
