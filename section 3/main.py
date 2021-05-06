


def is_isogram(string):
    all_lower = string.lower()
    myset = set(all_lower)

    if len(myset)== len(string):
        return True
    else:
        return False

is_isogram("Aabc")


