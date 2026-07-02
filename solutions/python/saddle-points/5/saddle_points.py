""" Module containing functions to detect Saddle Points is a matrix"""

def is_irregular(matrix):
    """Determine if a matrix is irregular
    Args:
        matrix (list(list[int]))
    Returns:
        boolean"""
    
    if matrix:
        return any(len(row) != len(matrix[0]) for row in matrix)
    else:
        return None


def saddle_points(matrix):
    """ Finds points in a matrix in which the value is the maximum in the row and the minimum in the column.
    Args:
        matrix (list(list[int]))
    Returns:
        list[ dict[str, int] ]
    """

    if is_irregular(matrix):
        raise ValueError("irregular matrix")

    found_places = []

    # Obtain the max for each row
    max_height_row = []
    for row in matrix:
        max_height_row.append(max(row))

    # Obtain the min for each column
    matrix_transposed = [list(col) for col in zip(*matrix)]
    min_height_col = []
    for row in matrix_transposed:
        min_height_col.append(min(row))

    # Verify the criteria for each value in the matrix
    for r_idx, row in enumerate(matrix):
        for c_idx, col in enumerate(matrix_transposed):

            if row[c_idx] == max_height_row[r_idx] and row[c_idx] == min_height_col[c_idx]:

                found_places.append({"row": r_idx+1, "column": c_idx+1})
    return found_places