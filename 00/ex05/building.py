import sys


def building(string: str) -> None:
    """
    This function takes a string as an argument and prints the number
    of spaces, uppercase letters, lowercase letters,
    """
    print(str(string.count(" ")) + " spaces")
    count = 0
    for i in range(len(string)):
        if string[i].isupper():
            count += 1
    print(str(count) + " uppercase letters")
    count = 0
    for i in range(len(string)):
        if string[i].islower():
            count += 1
    print(str(count) + " lowercase letters")
    count = 0
    for i in range(len(string)):
        if string[i].isdigit():
            count += 1
    print(str(count) + " digits")
    count = 0
    for i in range(len(string)):
        if (string[i] == '.' or string[i] == ',' or string[i] == ';' or
                string[i] == ':' or string[i] == '?' or string[i] == '!' or
                string[i] == '-' or string[i] == "'" or string[i] == '"'):
            count += 1

    print(str(count) + " punctuation characters")


def main():
    try:
        if len(sys.argv) < 2:
            print("What is the text to count?")
            print("Hello World!")
            building("Hello World!")
            sys.exit(1)
        if len(sys.argv) > 2:
            raise AssertionError
    except AssertionError:
        print("AssertionError : more than one argument is provided")
        sys.exit(1)
    building(sys.argv[1])


if __name__ == "__main__":
    main()
