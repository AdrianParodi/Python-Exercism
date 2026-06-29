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
    
    if any(count == 0 for _, count in alpha_dic.items()):
        return False
    return True

# print(is_pangram("abcdefghijklmnopqrstuvwxyz"))


# FRUITS = {"apple": 1, "pear": 5, "peach": 10}


# for fruit in FRUITS:
#     print(fruit.value())