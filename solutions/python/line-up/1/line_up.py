""" Module containing a function to line up people in a queue"""
def line_up(name, number):
    """ Converts the number to a ordinal position and returns a message
        with the name entered
    Args:
        name (str): The name of the person.
        number (int): The position in the queue.
    Returns:
        str : The personalized message for the customer in the line.    
    """
    ending = {1:"st", 2:"nd", 3:"rd"}

    if number % 10 not in [1,2,3] or number % 100 in [11,12,13]:
    # if 1 >= number%10 <=3 or 11 >= number%100 <= 13:
        ordinal = "th"
    else:
        ordinal = ending[number % 10]      

    return f"{name}, you are the {number}{ordinal} customer we serve today. Thank you!"    