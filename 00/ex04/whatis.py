import sys

def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError
        if len(sys.argv) < 2:
            sys.exit(1)
    except AssertionError as e:
        print("AssertionError : more than one argument is provided")
        sys.exit(1)
    try:
        if not sys.argv[1].isdigit():
            raise AssertionError
        val = int(sys.argv[1])
        if val % 2 == 0:
            print(f"Im even")
        else:
            print(f"Im odd")
    except AssertionError as e:
        print(f"AssertionError : argument is not an integer")
        sys.exit(1)

if __name__ == "__main__":
    main()
