def morse_code_encode(string):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',
        ' ': '/',
        '.': '.-.-.-', ',': '--..--'
    }

    encoded_string = ''
    for char in string.upper():
        if char in morse_code_dict:
            encoded_string += morse_code_dict[char] + ' '

    return encoded_string.strip()


string = "HELLO WORLD"
encoded_string = morse_code_encode(string)
print(encoded_string)
