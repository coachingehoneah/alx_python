"""Module to reverse strings"""

def reverse_string(string):
    """
    Returns the reversed string
    """
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string
