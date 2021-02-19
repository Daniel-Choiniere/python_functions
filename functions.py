def multiply(x: float, y: float) -> float:
    """
    Takes two `int` and gets the product.
    :param x: First `int` to be multiplied
    :param y: Second `int` to be multiplied
    :return: Product of x and y
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Checks if a `str` is the same backwards or forwards,
    :param string: The `str` to be checked.
    :return: `True` if the `str` is same backwards or forwards, `False` if it is not.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].lower() == string.lower()


def is_sentence_palindrome(sentence: str) -> bool:
    """
    Check if a sentence is the same backwards or forwards.
    Ignores whitespace, capitalisation, and punctuation in the sentence.
    :param sentence: Sentence to check
    :return: True if the sentence is same backwards or forwards, False if it is not.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)

# my fist solution, not very efficient and not dynamic for a ll characters
# def is_sentence_palindrome(string):
#     return string[::-1].replace(" ", "").replace("?", "").replace(",", "").lower() \
#            == string.replace(" ", "").replace("?", "").replace(",", "").lower()


sentence = input("Please enter a sentence to check: ")
if is_sentence_palindrome(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a palindrome".format(sentence))




# # two blank lines after a function declaration
# answer = multiply(3, 7)
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)
