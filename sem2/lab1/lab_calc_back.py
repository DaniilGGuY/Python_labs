def from_2_to_10(num):
    a = num.split(".")
    l = a[0]
    r = "0"
    if len(a) > 1:
        r = a[1]
    res = 0

    for i in range(len(l)):
        res += int(l[i]) * 2 ** (len(l) - i - 1)
    for i in range(len(r)):
        res += int(r[i]) * 2 ** (-(i + 1))

    return res


def from_10_to_2(num):
    a = num.split(".")
    l = int(a[0])
    r = 0
    len_r = 0
    if len(a) > 1:
        r = int(a[1])
        len_r = len(a[1])
    res = ""

    while l != 0:
        res = str(l % 2) + res
        l = int(l / 2)
    i = 0
    if r != 0:
        res += "."
    while r != 0 and i < 15:
        res += str(int(r * 2 / 10 ** len_r))
        r = r * 2 % 10 ** len_r
        i += 1

    return res
