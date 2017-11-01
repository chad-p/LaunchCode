from functools import lru_cache
"""
pascals triangle
row of 5

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

00001 (5)
000101 (6)
0010201 (7)
01030301 (8)
104060401 (9)

# alist = [
#     '00001',
#     '000101',
#     '0010201',
#     '01030301',
#     '104060401'
#     ]
"""

def add_prev_line(x, iterator=1):
    alist = x.split('o')
    alist = list(filter(None, alist))
    mult = []

    if len(alist) == 1:
        return 'o'

    for i in range(len(alist) - 1):
        numbers = (str(int(alist[i]) + int(alist[i + 1])) + 'o')
        mult.append(numbers)
        iterator += 1

    string = ''.join(mult)
    return ''.join('o' + string)


@lru_cache()
def pyramid(n, i=0):
    if type(n) != int:
        raise TypeError(n, "must be a positive int")
    if n < 1:
        raise ValueError(n, "must be a positive int")

    if n == 1:
        return alist
    elif i == 0:
        value = ("o" * n) + "1" + ("o" * n)
        alist.append(value)
        pyramid(n, i + 1)
    else:
        left = "o" * (n - 1) + "1"
        right = left[::-1]
        middle_nums = add_prev_line(alist[i - 1])
        alist.append(left + middle_nums + right)
        pyramid(n - 1, i + 1)

    return alist


alist = []

pyramid(15)

for line in alist:
     print(line.replace('o', ' '))
