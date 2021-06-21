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
def get_shifted_dict(input_string, num_letters_shifted):
    new_string = input_string[num_letters_shifted:] + input_string[:num_letters_shifted]
    shifted_dict = {}
    for num, let in enumerate(new_string):
        shifted_dict[num] = let

    return shifted_dict


# Reverses the above dictionary for translation back into readable English
def get_reverse_dict(input_string, num_letters_shifted):

    new_string = input_string[num_letters_shifted:] + input_string[:num_letters_shifted]
    shifted_dict = {}
    for let, num in enumerate(new_string):
        shifted_dict[num] = let
    return shifted_dict


def hide_message(message, shift_amount=5):
    text = ''
    new_cypher = get_shifted_dict(alpha_string, shift_amount)
    for x in message.lower():
        text = text + new_cypher[alph_dict[x]]

    return text


def unhide_message(message, shift_amount=5):
    text = ''
    reverse_cypher = get_reverse_dict(alpha_string, shift_amount)
    alpha_values = list(alph_dict.values())
    alpha_keys = list(alph_dict.keys())
    for x in message:
        key = reverse_cypher[x]
        text = text + alpha_keys[alpha_values.index(key)]

    return text


secret_message = "this is a test"
print(secret_message)

hidden = hide_message(secret_message)
print(hidden)

unhidden = unhide_message(hidden)
print(unhidden)

