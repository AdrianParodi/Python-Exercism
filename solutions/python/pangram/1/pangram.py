
def is_pangram(sentence):
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    alpha_dic = dict.fromkeys(alphabet, 0)
    
    for char in sentence.strip().lower():
        if char in alpha_dic.keys():
            alpha_dic[char] += 1
    

    for char_count in alpha_dic.values():
        if char_count == 0:
            return False
        
    return True
