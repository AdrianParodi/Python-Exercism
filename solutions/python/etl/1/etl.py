""" Module containing a function to modify dictionary structures"""

def transform(legacy_data):
    """Convert a legacy score mapping into a letter-to-score mapping.

    Given a dictionary where each key is a score and each value is a list
    of uppercase letters, return a new dictionary where each lowercase
    letter maps to its corresponding score.

    Args:
        legacy_data (dict[int, list[str]]): Mapping of scores to lists of
            uppercase letters.

    Returns:
        dict[str, int]: Mapping of lowercase letters to their scores.

    Example:
        >>> transform({1: ["A", "E"], 2: ["D", "G"]})
        {'a': 1, 'e': 1, 'd': 2, 'g': 2}
    """
    new_data = {}
    for points, letters in legacy_data.items():
        for letter in letters:
            new_data[letter.lower()] = points
    return new_data
