def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_index = ''
    letter = letter.lower()
    for char in alphabet:
        letter_index = alphabet.index(letter)
        if char == letter:
            return letter_index
    return letter_index
#print(alphabet_position("Z"))

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    is_alpha = "False"
    is_upper = "False"
    index = 0
    new_index = 0
    if char.isalpha() == False:
        print
        return char #,("not alpha")
    else:
        if char.isupper() == True:
            index = alphabet_position(char)
            new_index = (index + rot) % 26
            rotate_character = upper_alphabet[new_index]
            return rotate_character #,("is upper"), index, new_index
        else:
            index = alphabet_position(char)
            new_index = (index + rot) % 26
            rotate_character = alphabet[new_index]
            return rotate_character #,("is lower"), index, new_index

def encrypt(message, rot):
    encrypted = ''
    for char in message:
        encrypted = encrypted + rotate_character(char, rot)
    return encrypted #,text, rot
