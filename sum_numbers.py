def sum_numbers(*args: float) -> float:
    """
    finds the sum of all numbers passed to it
    :param args: numbers to be summed
    :return: the sum of all numbers passed to function
    """
    total = 0
    for number in args:
        total += number
    print(total)


sum_numbers(1, 2, 3, 2, 1)
sum_numbers(8, 20, 2)
sum_numbers(12.5, 3.147, 98.1)