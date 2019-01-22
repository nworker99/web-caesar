from helpers import alphabet_position, rotate_character

#Encrypt function
def encrypt(text, rot):
    new_text = ""
    for char in text:
        new_char = rotate_character(char, rot)
        new_text = new_text + new_char
    return new_text

if __name__ == "__main__":
    encrypt()