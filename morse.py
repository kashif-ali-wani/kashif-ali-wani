# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ' ': '/', ',': '--..--', '.': '.-.-.-', '?': '..--..', ';': '-.-.-.', ':': '---...',
    "'": '.----.', '-': '-....-', '(': '-.--.', ')': '-.--.-', '/': '-..-.', '_': '..--.-',
    '"': '.-..-.', '@': '.--.-.', '=': '-...-', '!': '-.-.--'
}

def text_to_morse(text):
    """
    Converts a string of text to Morse code.

    Args:
        text (str): The input text to be converted.

    Returns:
        str: The Morse code representation of the input text.
    """
    morse_code = ''
    # Convert the input text to uppercase for dictionary lookup
    for char in text.upper():
        # Check if the character exists in our Morse code dictionary
        if char in MORSE_CODE_DICT:
            # Add the corresponding Morse code and a space
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            # If a character is not found, we will just ignore it.
            # You could also add a placeholder like '#' if you want to represent unknown characters.
            pass
    # Return the final morse code string, removing any trailing space
    return morse_code.strip()

# Main part of the script that runs
if __name__ == "__main__":
    print("--- Text to Morse Code Converter ---")
    
    # Loop indefinitely to allow multiple conversions
    while True:
        # Get input from the user
        input_text = input("Enter text to convert (or type 'exit' to quit): ")
        
        # Check if the user wants to exit
        if input_text.lower() == 'exit':
            print("Exiting converter. Goodbye!")
            break
            
        # Perform the conversion
        result = text_to_morse(input_text)
        
        # Print the result
        if result:
            print(f"Morse Code: {result}\n")
        else:
            print("You entered text that couldn't be converted. Please try again.\n")
