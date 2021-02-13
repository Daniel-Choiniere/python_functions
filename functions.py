def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].lower() == string.lower()


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))


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
