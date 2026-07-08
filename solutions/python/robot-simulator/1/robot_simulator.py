""" Module containing a Class to simulate robot movement and rotation"""

EAST = "E"
NORTH = "N"
WEST = "W"
SOUTH = "S"

cardinals = [NORTH, EAST, SOUTH, WEST]


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.x = x_pos
        self.y = y_pos
        self.coordinates = (self.x, self.y)
        self.direction = direction
        self.cardinal_index = cardinals.index(self.direction)


    def move(self, instructions):
        for letter in instructions:
            if letter.upper() == "A":
                self.advance()
            if letter.upper() == "L":
                self.rotate_left()
            if letter.upper() == "R":
                self.rotate_right()    


    def advance(self):
        if self.direction == EAST:
            self.x +=1
        elif self.direction == WEST:
            self.x -= 1
        elif self.direction == NORTH:
            self.y += 1
        elif self.direction == SOUTH:
            self.y -= 1
        # Update coordinates
        self.coordinates = (self.x, self.y)


    def rotate_left(self):
        self.cardinal_index = (self.cardinal_index - 1) % 4
        self.direction = cardinals[self.cardinal_index]


    def rotate_right(self):
        self.cardinal_index = (self.cardinal_index + 1) % 4
        self.direction = cardinals[self.cardinal_index]


# prueba = Robot(EAST, 1,1)

# prueba.move("AaaRLL")

# print(prueba.coordinates, prueba.direction)
# print(prueba.cardinal_index)