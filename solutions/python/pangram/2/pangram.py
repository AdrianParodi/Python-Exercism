"""Module to verify whether a string is a pangram"""

def is_pangram(sentence):
    """ Verify if a sequence of string is a pangram.
    Args:
        sentence (str): The sequence to be verified.
    Returns
        boolean: True if the setence is a pangram.
    """
    alphabet = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
    alpha_dic = dict.fromkeys(alphabet, 0)
    
    for char in sentence.strip().lower():
        if char in alpha_dic.keys():
            alpha_dic[char] += 1
    
    if any(count == 0 for count in alpha_dic.values()):
        return False
    return True