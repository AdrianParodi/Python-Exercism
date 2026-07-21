"""Encode and decode integers using Variable Length Quantity (VLQ).

This module provides functions to encode unsigned integers into VLQ byte
sequences and to decode VLQ byte sequences back into integers.
"""
def encode(numbers):
    """Encode unsigned integers using Variable Length Quantity (VLQ).

    Args:
        numbers (list[int]): Unsigned integers to encode.

    Returns:
        list[int]: The VLQ-encoded byte sequence representing all input
            integers.
    """
    result = []
    bytes_per_group = 7
    for number in numbers:
        if number == 0:
            result.append(0)
            continue  # jumps to the next number in numbers
        
        chunks = []
        value = number

        while value > 0:
            chunks.append(value & 0x7F)
            value >>= bytes_per_group
        
        chunks.reverse()

        for i in range(len(chunks)-1):
            chunks[i] |= 0x80

        result.extend(chunks)
    return result        


def decode(bytes_):
    """Decode a Variable Length Quantity (VLQ) byte sequence.

    Args:
        bytes_ (list[int]): A sequence of VLQ-encoded bytes.

    Returns:
        list[int]: The decoded unsigned integers.

    Raises:
        ValueError: If the input ends with an incomplete VLQ sequence.
    """
    result = []
    bytes_per_group = 7
    number = 0

    for byte in bytes_:
        # Take 7 bits of information (there are 8, the first is a flag)
        value = byte & 0x7F

        number = (number << bytes_per_group) | value

        # When the flag bit is zero, the number was completed
        if byte & 0x80 == 0:
            result.append(number)
            number = 0
    
    if bytes_[-1] & 0x80 != 0:
        raise ValueError("incomplete sequence")
    
    return result


print(len(bin(253)))




# numero = 8192
# grupo = numero & 0x7F
# grupo |= 0x80
# print(grupo)

# # # print(numero & 15)
# # print(64>>7)
# # print(0b0 << 7)

# result = decode([0xFFFFFFFF])
# print( 24 & 0x7f)
# print(result)