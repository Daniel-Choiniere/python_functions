numbers = (0, 1, 2, 3, 4, 5)
# using star unpacks the tuple, or any sequence type
# print(numbers)
# print(*numbers)


def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)

print()
test_star()