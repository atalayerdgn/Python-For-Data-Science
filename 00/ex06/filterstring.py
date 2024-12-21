import sys


def filterstring(string: str, count: int) -> None:
    """This function takes a string and an integer as
    arguments and prints the words that have more than the
     integer number of characters"""
    list_of_string = string.split()
    a = list()
    for i in list_of_string:
        if len(i) > count:
            a.append(i)
    print(a)


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError
        if not isinstance(sys.argv[1], str):
            raise AssertionError
        if not sys.argv[2].isdigit():
            raise AssertionError
        filterstring(sys.argv[1], int(sys.argv[2]))
    except AssertionError:
        print("AssertionError : the arguments are bad")
        sys.exit(1)


if __name__ == "__main__":
    main()
