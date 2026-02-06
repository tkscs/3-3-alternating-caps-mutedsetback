def alt_caps(original_string):
    """Convert a string to Alternating Caps

    Args:
        original_string (str): A given string with any kind of capitalization
    Returns:
        str: A new string with alternating capitalization
    Examples:
        >>> print(alt_caps("Alternating Capitalization"))
        aLtErNaTiNg CaPiTaLiZaTiOn
    """
    new_string = ""

    # YOUR CODE HERE
def alt_caps(original_string):
    new_string = ""
    make_upper = False
    for x in original_string:
        if x.isalpha():
            if make_upper:
                new_string += x.upper()
            else:
                new_string += x.lower()
            make_upper = not make_upper
        else:
            new_string += x

    return new_string

print(alt_caps("Alternating Capitalization"))