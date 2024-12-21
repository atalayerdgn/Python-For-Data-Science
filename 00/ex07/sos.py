import sys


def NESTED_MORSE_FUNC(string: str) -> str:
    """
    This function takes a string as an argument and returns the morse code
    for the string
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- ",
    }
    morse_code = ""
    for char in string:
        if char in NESTED_MORSE:
            morse_code += NESTED_MORSE[char]
        else:
            raise AssertionError(f"Invalid character '{char}' found in input")
    return morse_code.strip()


def main():
    if len(sys.argv) != 2 or not isinstance(sys.argv[1], str):
        raise AssertionError("Invalid argument count or type")
    input_string = sys.argv[1].upper()
    morse_code = NESTED_MORSE_FUNC(input_string)
    print(morse_code)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    sys.exit(0)
