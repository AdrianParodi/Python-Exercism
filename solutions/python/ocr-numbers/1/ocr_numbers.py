"""Module containing a function to recognize digits from a string format"""
ocr_values = {
    (" _ ", 
     "| |", 
     "|_|", 
     "   "): 0,
     
    ("   ", 
     "  |", 
     "  |", 
     "   "): 1,

    (" _ ", 
     " _|", 
     "|_ ", 
     "   "): 2,

    (" _ ", 
     " _|", 
     " _|", 
     "   "): 3,

    ("   ", 
     "|_|", 
     "  |", 
     "   "): 4,

    (" _ ", 
     "|_ ", 
     " _|", 
     "   "): 5,

    (" _ ", 
     "|_ ", 
     "|_|", 
     "   "): 6,

    (" _ ", 
     "  |", 
     "  |", 
     "   "): 7,

    (" _ ", 
     "|_|", 
     "|_|", 
     "   "): 8,

    (" _ ", 
     "|_|", 
     " _|", 
     "   "): 9
}

# print(type((" _ ", 
#      "|_|", 
#      " _|", 
#      "   ")))

    #   _  _     _  _  _  _  _  _  #
    # | _| _||_||_ |_   ||_||_|| | # Decimal numbers.
    # ||_  _|  | _||_|  ||_| _||_| #
                                   # The fourth line is always blank

A=                [
                    "    _  _     _  _  _  _  _  _ ",
                    "  | _| _||_||_ |_   ||_||_|| |",
                    "  ||_  _|  | _||_|  ||_| _||_|",
                    "                              ",
                ]

A = [
                    "    _  _ ",
                    "  | _| _|",
                    "  ||_  _|",
                    "         ",
                    "    _  _ ",
                    "|_||_ |_ ",
                    "  | _||_|",
                    "         ",
                    " _  _  _ ",
                    "  ||_||_|",
                    "  ||_| _|",
                    "         ",
                ]


def convert(input_grid):
    """Convert the input text representing digits to the actual values
        Args: 
            input_grid (list(str))
        return
            str
    """
    
    number_of_lines = len(input_grid)
    chars_per_line = len(input_grid[0])

    if number_of_lines % 4 !=0:
        raise ValueError("Number of input lines is not a multiple of four")
    if chars_per_line % 3 != 0:
        raise ValueError ("Number of input columns is not a multiple of three")
    

    lines = []

    # Processing per blocks of 4 lines
    for row in range(0, number_of_lines,4):
        row0 = input_grid[row]
        row1 = input_grid[row + 1]
        row2 = input_grid[row + 2]
        row3 = input_grid[row + 3]

        chars_line = ""

        for col in range(0, chars_per_line, 3):
            char_line0 = row0[col:col+3]
            char_line1 = row1[col:col+3]
            char_line2 = row2[col:col+3]
            char_line3 = row3[col:col+3]

            char_tuple = (char_line0, char_line1, char_line2, char_line3)

            if char_tuple in ocr_values:
                chars_line += str(ocr_values[char_tuple])
            else:
                chars_line += "?"

        lines.append(chars_line)
    
    result = ",".join(lines)  # "," between lines, but not at the end
    return result