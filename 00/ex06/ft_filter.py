def ft_filter():
    """filter(function or None, iterable) --> filter object"""
    a = ["filter(function or None, iterable) --> filter object", "\n\n"]
    b = ["Return an iterator yielding those items",
         "of iterable for which function(item)\n"]
    c = ["is true. If function is None, return the items that are true."]
    string = "".join(a + b + c)
    return string

def main():
    print(ft_filter())

if __name__ == "__main__":
    main()
