# 24. Cumulative sum of a list [1, 2, 4, …] is defined as [1, 3, 7, . . .] Write a function
# cumulative_sum() to compute cumulative sum of a list

def cumulative_sum(numbers):
    """
    Compute the cumulative sum of a list of numbers.

    :param numbers: List of numbers
    :return: List containing the cumulative sum
    """
    cumulative = []
    total = 0
    for num in numbers:
        total += num
        cumulative.append(total)
    return cumulative


# Example usage
numbers = [1, 2, 4, 6]
result = cumulative_sum(numbers)
print(f"Original list: {numbers}")
print(f"Cumulative sum: {result}")
