CODE_DICT = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}

# Function to convert text to morse code
def text_to_morse(text):
    text = text.lower()
    filtered_text = ''.join([char for char in text if char in CODE_DICT or char == ' '])
    print(f"Filtered Text: {filtered_text}")
    morse_list = []
    for word in filtered_text.split():
        morse_word = [CODE_DICT[char] for char in word if char in CODE_DICT]
        morse_list.append(' '.join(morse_word))
    return ' / '.join(morse_list)  

# Main program
if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    morse_code = text_to_morse(sentence)
    print(f"Morse Code: {morse_code}")

# Circuit Playground extension code
import time
import board
import neopixel

def display_morse_on_cp(morse_list, unit_length):
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3)
    for morse_char in morse_list:
        if morse_char == '.':
            pixels.fill((0, 255, 0))  # Green for dot
            time.sleep(unit_length)
        elif morse_char == '-':
            pixels.fill((255, 0, 0))  # Red for dash
            time.sleep(3 * unit_length)
        elif morse_char == ' ':
            pixels.fill((0, 0, 0))  # Off for character space
            time.sleep(unit_length * 3)
        elif morse_char == '/':
            pixels.fill((0, 0, 0))  # Off for word space
            time.sleep(unit_length * 7)
        pixels.fill((0, 0, 0))
        time.sleep(unit_length)  

if __name__ == "__main__":
    unit_length = float(input("Enter the length of a unit (between 0 and 1 second): "))
    sentence = input("Enter a sentence: ")
    morse_code = text_to_morse(sentence)
    morse_list = list(morse_code)
    display_morse_on_cp(morse_list, unit_length)