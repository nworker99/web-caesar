#Determines letter's location within alphabet
def alphabet_position(letter):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in letter:
        if char in alphabet_lower:
            return alphabet_lower.find(char)
        elif char in alphabet_upper:
            return alphabet_upper.find(char)
        else:
            return char

#Rotates letters by a number
def rotate_character(char, rot):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rot = int(rot)
    
    if char in alphabet_lower:
        final = rot + alphabet_lower.find(char)
        if final > 25:
            final = final % 26
            return alphabet_lower[final]
        else:
            return alphabet_lower[final]
    elif char in alphabet_upper:
        final = rot + alphabet_upper.find(char)
        if final > 25:
            final = final % 26
            return alphabet_upper[final]
        else:
            return alphabet_upper[final]
    else:
        return char

#Rotates letters by a key
def rotate_key(char, rot):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final = 0
    
    if char in alphabet_lower:
        if rot in alphabet_upper:
            final = alphabet_upper.find(rot) + alphabet_lower.find(char)
        elif rot in alphabet_lower:
            final = alphabet_lower.find(rot) + alphabet_lower.find(char)
        if final > 25:
            final = final % 26
            return alphabet_lower[final]
        else:
            return alphabet_lower[final]
    elif char in alphabet_upper:
        if rot in alphabet_upper:
            final = alphabet_upper.find(rot) + alphabet_upper.find(char)
        elif rot in alphabet_lower:
            final = alphabet_lower.find(rot) + alphabet_upper.find(char)
        if final > 25:
            final = final % 26
            return alphabet_upper[final]
        else:
            return alphabet_upper[final]
    else:
        return char

