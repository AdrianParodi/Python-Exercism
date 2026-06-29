"""Module to verify whether a string is a pangram"""

from string import ascii_lowercase
def is_pangram(sentence):
    """ Verify if a sequence of string is a pangram.
    Args:
        sentence (str): The sequence to be verified.
    Returns
        boolean: True if the setence is a pangram.
    """
    return all(char in sentence.lower() for char in ascii_lowercase)