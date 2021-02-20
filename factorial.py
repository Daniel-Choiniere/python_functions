def factorial(n: int) -> int:
    """
        finds the factorial of a number
    :param n: number to find the factorial of
    :return: the factorial of n
    """
    total = 1
    for number in range(1, n + 1):
        total *= number
    return total


factorial(0)