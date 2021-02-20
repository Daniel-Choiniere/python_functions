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

# The game will take turns between the computer and user input starting
# with the computer at 0. The user will have to give the correct response
# to the number that they are currently on. The game will end when the
# player makes a mistake or the game reaches 100. If the player gives
# the wrong response than they lose.

# for the computers turns we will run the function and give the response
# for the players turn we will ask for input on the current iterated number
# and compare it to the correct response.
# if it is right the game continues, if wrong they get a message that they lost


for number in range(1, 101):
    correct_answer = fizz_buzz(number)
    if number == 0 or number % 2 == 0:
        print("Computer response {}".format(correct_answer))
    else:
        player_response = input("What is the correct response for this "
                                "number: {}?".format(number))
        if number == 99 and player_response == "fizz":
            print("Congratulations, You Won!!!")
            break
        if player_response == correct_answer:
            continue
        else:
            print("Wrong, You Lose!")
            break
