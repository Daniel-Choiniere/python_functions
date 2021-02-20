def fizz_buzz(n: int) -> str:
    """
        Checks to see if an `int` is divisible by 3, 5, both, or neither,
        and prints out the appropriate response.
    :param n: a `int` to be checked if divisible by 3 or 5 or both
    :return:  `str` fizz if divisible by 3, buzz if divisible by 5,
        fizz buzz if divisible by both, and the number as a string
        if not divisible by either
    """
    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


for number in range(1, 101):
    fizz_buzz(number)
