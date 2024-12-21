def count_in_list(list_: list, string: str) -> int:
    """
    """
    count = 0
    for i in list_:
        if i == string:
            count += 1
    return count
