"""Module for calculating valid digit combinations in Killer Sudoku cages."""

def combinations(target, size, exclude):
    """Find all valid unique digit combinations for a Killer Sudoku cage.

    Args:
        target (int): The target sum that the combination of digits must reach.
        size (int): The number of digits (cells) required in the cage.
        exclude (list[int]): Digits that cannot be used in the solution.

    Returns:
        list[list[int]]: A list of unique sorted digit combinations that sum to target.
    """
    solutions = []
    exclude_set = set(exclude)
    
    def backtrack(start, current_combination, current_sum):
        """Recursively explore digit combinations using a backtracking algorithm.

        Args:
            start (int): The next lowest candidate digit to evaluate (1-9).
            current_combination (list[int]): The partial combination being built.
            current_sum (int): The running total sum of digits in current_combination.
        """
        
        # Base case: exact size reached and target sum satisfied
        if len(current_combination) == size and current_sum == target:
            solutions.append(current_combination.copy()) # a copy of the list at the specific moment.
            return
        
        # Pruning: stop exploring if the target sum is exceeded 
        if current_sum > target or len(current_combination) >= size:
            return
        
        # Recursive case: try available digits in ascending order
        for number in range(start,10):
            if number not in exclude_set:
                current_combination.append(number)
                backtrack(number + 1, current_combination, current_sum + number)
                current_combination.pop()

    backtrack(1,[],0)
    return solutions