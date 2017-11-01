"""
Write a function analyze_text that receives a string as input. Your function should count the number of alphabetic characters (a through z, or A through Z) in the text and also keep track of how many are the letter 'e' (upper or lowercase).

Your function should return an analysis of the text in the form of a string phrased exactly like this:

“The text contains 240 alphabetic characters, of which 105 (43.75%) are ‘e’.”

You will need to make use of the isalpha function, which can be used like this

"a".isalpha() # => evaluates to True
"3".isalpha() # => evaluates to False
"&".isalpha() # => False
" ".isalpha() # => False

mystr = "Q"
mystr.isalpha() # => True
"""

def analyze_text(text):

    num_of_e = 0
    num_of_char = 0

    for char in text.lower():
        if char == "e":
            num_of_e += 1

        if char.isalpha():
            num_of_char += 1

    percentage_of_e = (num_of_e / num_of_char) * 100

    print_statement = "The text contains {} alphabetic characters, of which {} ({}%) are 'e'.".format(num_of_char, num_of_e, percentage_of_e)

    return print_statement


def main():

    analyze_text("abcdeee123")


if __name__ == "__main__":
    main()
