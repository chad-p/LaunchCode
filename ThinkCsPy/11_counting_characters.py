from collections import defaultdict

def count_letters(string):

    # Refactor 3 ---------
    d = defaultdict(int)
    for char in string:
        d[char] += 1

    print_letters(d)
    # --------------------

    # Refactor 2 ---------
    # d = {}
    # for char in string:
    #     d[char] = d.get(char, 0) + 1
    #
    # print_letters(d)
    # ---------------------

    # Refactor 1 ----------
    # d = {}
    # for char in string:
    #     if char not in d:
    #         d[char] = 0
    #     d[char] += 1
    #
    # print_letters(d)
    # ----------------------

#  First attempt   ----------
#     dic_letters = {}
#
#     for char in string:
#         dic_letters[char] = 0
#
#         for scan_char in string:
#             if char == scan_char:
#                 dic_letters[char] += 1
#
#     print_letters(dic_letters)
# -----------------------------------

def print_letters(dic_letters):

    # while dic_letters:
    #     key, value = dic_letters.popitem()
    #     print(key + ": " + str(value))

     # First Attempt --------------------------
     for k, v in sorted(dic_letters.items()):
         print(k + ": " + str(v))
     # -----------------------------------------

string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin." \
         " Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus," \
         " non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa." \
         " Donec nec velit non ligula efficitur luctus."
count_letters(string)
