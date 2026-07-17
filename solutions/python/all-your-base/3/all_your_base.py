def _validations(input_base, digits, output_base):
    """Validate whether the data to produce the conversion is valid.
    
    This function performs the following safety checks:
    1. The input base must be equal or higher than 2.
    2. All the digits must be between 0 and the input_base values.
    3. The output base must be equal or higher than 2."""
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    digit_lower_than_zero = [digit < 0 for digit in digits]
    digit_higher_than_input_base = [digit >= input_base for digit in digits]
    
    if any(digit_lower_than_zero) or any(digit_higher_than_input_base):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")


def _convert_to_decimal(digits, input_base):
    """Convert a number represented in a list and a particular base to its decimal representation.

    This implementation makes use of the Horner's method to compute the conversion.

    Args:
        digits: list(int)
        input_base (int): the base in which the number is represented.
        
    Returns:
        number_in_decimal (int): the value in decimal base."""
    number_in_decimal = 0
    
    # Horner's method
    for digit in digits:
        number_in_decimal = number_in_decimal * input_base + digit

    return number_in_decimal
        

def _decimal_to_new_base(number, output_base):
    """ Converts a decimal number to a list representation in the desired base.

    Args:
        number(int): the decimal number to be converted.
        output_base(int): the base in which the result is represented.
    Returns:
        output_number (list[int])
    """
    output_number = []

    quotient, remainder = divmod(number, output_base)
    output_number.append(remainder)

    while quotient >= output_base:
        quotient, remainder = divmod(quotient, output_base)
        output_number.append(remainder)

    output_number.append(quotient)
    output_number = list(reversed(output_number))

    # Removes zeros on the left
    while output_number[0] == 0 and len(output_number) > 1:
        output_number.pop(0)
    
    return output_number


def rebase(input_base, digits, output_base):
    """ Converts a number from one base to another.
    
    Args:
        input_base (int): the base in which digits is represented.
        digits (list[int]): the number to be converted.
        output_base (int): the base for the output result

    Returns:
        desired_number (list[int]): the representation of the number in the desired base.
    """
    _validations(input_base, digits, output_base)

    number_base_10 = _convert_to_decimal(digits, input_base)
    if output_base == 10:
        # Convert the result to a list of strings
        desired_number = list((str(number_base_10)))
        # Convert them back to a list of int.
        desired_number = [int(number_string) for number_string in desired_number]
    else:
        desired_number = _decimal_to_new_base(number_base_10, output_base)
    return desired_number