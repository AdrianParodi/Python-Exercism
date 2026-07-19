"""Module containing a function to generate a spiral matrix"""
def spiral_matrix(size):
    """Generate and return a square matrix filled in clockwise spiral order.
    
    The function generates the numbers in a clockwise very intuitive process.
    It initializes a square matrix of a given size and then it populates it with
    the numbers in ascending order starting from the left upper corner.
    It uses a series of delimiting indexes that are adjusted every step to 
    navigate the matrix effectively. 
      
    Args:
        size (int): the number of rows and columns of the resulting matrix
    Returns:
        list[list[int]]: A size x size matrix containing the integers
            from 1 to size**2  in clockwise spiral order."""
    result = [[0 for col in range(size)] for row in range(size)]

    top_idx, left_idx  = 0, 0
    bot_idx, right_idx  = size - 1, size - 1

    next_number = 1
    while next_number <= size ** 2:
        #Left -> Right
        for col in range(left_idx, right_idx + 1):
            result[top_idx][col] = next_number
            next_number += 1
        top_idx += 1
        
        #Top -> Bottom
        for row in range(top_idx, bot_idx + 1):
            result[row][right_idx] = next_number
            next_number += 1
        right_idx -= 1

        #Right -> Left
        for col in reversed(range(left_idx, right_idx + 1)):
            result[bot_idx][col] = next_number
            next_number += 1
        bot_idx -= 1
        
        #Bot -> Top
        for row in reversed(range(top_idx, bot_idx + 1)):
            result[row][left_idx] = next_number
            next_number += 1
        left_idx += 1

    return result