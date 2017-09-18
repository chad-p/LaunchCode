def is_sorted(string):
    """Returns True if string is sorted from least to greatest
       False otherwise.

       Recall that the order operators are case-sensitive, so that "A" < "a" evaluates to True.
    """
    string = list(string)
    sorted_string = sorted(string)

    if sorted_string == string:
        print("True")
    else:
        print("False")

    return False

is_sorted("ABC")
is_sorted("aBc")
is_sorted("dog")