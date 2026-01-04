# Text to Braille (Unicode) Converter

braille_map = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵',

    '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙', '5': '⠼⠑',
    '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓', '9': '⠼⠊', '0': '⠼⠚',

    ' ': ' ',
    '.': '⠲', ',': '⠂', '?': '⠦', '!': '⠖',
    ':': '⠒', ';': '⠆', '-': '⠤', "'": '⠄'
}

def text_to_braille(text):
    result = ""
    for char in text.lower():
        result += braille_map.get(char, '')
    return result


text = input("Enter text: ")
braille = text_to_braille(text)
print("Braille Output:")
print(braille)
