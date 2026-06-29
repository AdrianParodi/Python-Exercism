""" Module containing a function to flatten lists or tuples"""
def flatten(iterable):
    """Flatten a nested structure of lists or tuples into a single flat list.

    This function recursively traverses any nested lists or tuples, extracting 
    all non-None elements and combining them into a single-dimensional list.
    Null values (None) are omitted from the final result.

    Args:
        iterable (iterable): A nested list, tuple, or mixed structure 
            containing elements and/or other iterables.

    Returns:
        list: A new flat list containing all the deeply extracted 
            non-None elements.
            
    Examples:
        >>> flatten([1, [2, 3], None, [4, [5]]])
        [1, 2, 3, 4, 5]
    """

    def _flatten_generator(items):
        for element in items:
            if isinstance (element, (list, tuple)):
                yield from _flatten_generator(element)
            elif element is not None:
                yield element
    return list(_flatten_generator(iterable))