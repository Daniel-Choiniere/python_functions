def multiply(x, y):
    result = x * y
    return result


# def is_palindrome(string):
#     # backwards = string[::-1]
#     # return backwards == string
#     return string[::-1].lower() == string.lower()


def is_sentence_palindrome(string):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return string[::-1].casefold() == string.casefold()

# my fist solution, not very efficent and not dynamic for a ll characters
# def is_sentence_palindrome(string):
#     return string[::-1].replace(" ", "").replace("?", "").replace(",", "").lower() \
#            == string.replace(" ", "").replace("?", "").replace(",", "").lower()


sentence = input("Please enter a sentence to check: ")
if is_sentence_palindrome(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a palindrome".format(sentence))

# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))


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
