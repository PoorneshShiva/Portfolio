from logo import banner
import pyperclip

ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' '}
DECRYPTED_MESSAGE = ""
ENCRYPTION_MESSAGE = ""


def encryption_to_morse(word):
    """Encrypts the English Words to Morse Code, Required few English Words."""
    global ENCRYPTION_MESSAGE
    ENCRYPTION_MESSAGE = ""
    for letter in word.upper():
        new_letter = ENGLISH_TO_MORSE[letter]
        ENCRYPTION_MESSAGE += new_letter + "/"

    return ENCRYPTION_MESSAGE


def decryption_to_english(word):
    """Decrypts the Morse Code to English Words, Required few Morse code."""
    global DECRYPTED_MESSAGE
    DECRYPTED_MESSAGE = ""
    for each in word.split("/"):
        values = list(ENGLISH_TO_MORSE.values())
        keys = list(ENGLISH_TO_MORSE.keys())
        if each in values:
            decrypt_letter = keys[values.index(each)]
            DECRYPTED_MESSAGE += decrypt_letter

    return DECRYPTED_MESSAGE.title()


def main():
    # Printing the Banner!
    print(banner)
    # Asking the User to enter the requirements.
    choice = input('Do you want to encode(e), decode(d), or quit(q)?:').lower()
    if choice == "e":
        encode = input('Enter the English code to decode?:').upper()
        encoded_text = encryption_to_morse(encode)
        # Copies the encoded text.
        pyperclip.copy(encoded_text)
        print("Your encoded text is copied to your clipboard Successfully!")
        print(f"Your encoded text is {encoded_text}")

    elif choice == "d":
        decode = input('Enter the Morse code to decode?:').upper()
        decoded_text = decryption_to_english(decode)
        # Copies the decoded text.
        pyperclip.copy(decoded_text)
        print("Your decoded text is copied to your clipboard Successfully!")
        print(f"Your decoded text is '{decoded_text}'")
    elif choice == "q":
        end = True
    else:
        print("Sorry you've chosen a wrong choice!")


if __name__ == "__main__":
    main()
