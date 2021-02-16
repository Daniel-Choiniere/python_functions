def sum_eo(n, t):
    if t == "e":
        total = 0;
        for number in range(n):
            if number % 2 == 0:
                total += number
        return total

    elif t == "o":
        total = 0;
        for number in range(n):
            if number % 2 != 0:
                total += number
        return total
    else:
        return -1


print(sum_eo(4, "e"))  # 2
print(sum_eo(6, "e"))  # 6
print(sum_eo(4, "o"))  # 4
print(sum_eo(6, "o"))  # 9

