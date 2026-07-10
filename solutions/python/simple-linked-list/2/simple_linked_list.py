class EmptyListException(Exception):
    """Exception raised when the linked list is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class Node:
    """It creates a node with a value"""
    def __init__(self, value):
        """Initialize the node with a value. It has a pointer to the next node. 
        Args:
            value(int): the value of the node
        Returns: None"""
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next
        

class LinkedList:
    """"Creates a linked list of nodes with the values passed as parameter.
    Args:
        values (list): a list of values for each node."""
    def __init__(self, values=None):
        self._head = None
        self._length = 0

        if values:
            for value in values:
                self.push(value)


    def __iter__(self):
        current_node = self._head
        while current_node:
            yield current_node.value()
            current_node = current_node.next()


    def __len__(self):
        return self._length

    def head(self):
        if self._length == 0:
            raise EmptyListException("The list is empty.")
        
        return self._head

    def push(self, value):
        new_node = Node(value)

        # Update the head and length
        new_node._next = self._head
        # new_node._next = self.head()
        self._head = new_node
        self._length += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        
        node_to_eliminate = self._head
        self._head = node_to_eliminate.next()
        # Update head and length
        self._length -= 1

        return node_to_eliminate.value()

    def reversed(self):
        reversed_linked_list = LinkedList()
        for node in self.__iter__():
            reversed_linked_list.push(node)
        return reversed_linked_list
    
musica = LinkedList([1,2,3])
print(musica.reversed())
# musica = LinkedList([5,7,9])
# # print(len(musica))
# print(f"Head Value: {musica.head().value()}")
# print(f"Longitud: {len(musica)}")
# print(f"Popeo: {musica.pop()}")
# print(f"NEW Head Value: {musica.head().value()}")
# print(f"NEW Longitud: {len(musica)}")
# print(f"Popeo: {musica.pop()}")
# print(f"Popeo: {musica.pop()}")
# print(f"Popeo: {musica.pop()}")