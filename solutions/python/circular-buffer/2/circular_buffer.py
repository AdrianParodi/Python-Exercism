"""Module containing a class that simulates the management of a FIFO (First In, First Out) stack"""

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    """ A circular buffer simulator that uses a single fixed-size buffer as it were connected end-to-end.
    """
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity


    def read(self):
        """Permits to read the oldest element added to the buffer,  removing it from the memory.
        Returns:
            (int): The oldest element"""
        if len(self.buffer) == 0:
            raise BufferEmptyException("Circular buffer is empty")

        return self.buffer.pop(0)


    def write(self, data):
        """Writes the current memory position of the buffer.
        Args:
            data (int): the value to be written in memory.
        Returns:
            None"""
        
        if len(self.buffer) >= self.capacity:
            raise BufferFullException("Circular buffer is full")
        
        self.buffer.append(data)


    def overwrite(self, data):
        """Overwrites the oldest element in the buffer with new data.
        Args:
            data (): the new element to be written
        Returns:
            None"""
        if len(self.buffer) < self.capacity:
            self.buffer.append(data)
        else:
            self.buffer.pop(0)
            self.buffer.append(data)
        

    def clear(self):
        """Removes all the elements of the buffer."""
        self.buffer = []