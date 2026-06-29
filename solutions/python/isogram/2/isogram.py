""" Module providing a function for isograms verification"""
from string import ascii_lowercase

def is_isogram(phrase):
    """ Verify if a sequence of strings is an isogram.
    Args:
        phrase (str): The sequence to be verified
    Returns
        boolean"""
    
    alphabet_dic = dict.fromkeys(ascii_lowercase, 0)
    for letter in phrase.strip().lower():
        if letter in alphabet_dic:
            alphabet_dic[letter] += 1
            if alphabet_dic[letter] >= 2:
                return False
    return True
        

print(is_isogram("Alphabet"))
    
