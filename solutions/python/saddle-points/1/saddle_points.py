def is_irregular(matrix):
    """Determine if a matrix is irregular
    Args:
        matrix (list(list[int]))
    Returns:
        boolean"""
    
    if matrix:
        len_row0 = len(matrix[0])
    for row in matrix:
        if len(row) != len_row0:
            return True
    return False

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
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == max_height_row[row] and matrix[row][col] == min_height_col[col]:
                found_places.append({"row": row+1, "column": col+1})
    return found_places

# # matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]
# matrix = []
# print(saddle_points(matrix))