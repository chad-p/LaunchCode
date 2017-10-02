from helpers import alphabet_position, rotate_character

def alphabet_position(char):
    """
    Take in a letter, make it lowercase and convert it to ascii number.  Subtract 97 (ascii starting num for 'a')
    :param letter:
    :return: Return number value of letter will return value greater than 25.  ie a == 0, z == 25,
    """

    return ord(char.lower()) - 97


def rotate_character(string, rot):
    value = ()

    for char in string:

        if not char.isalpha():
            value = value + (char,)
        else:
            is_upper = char.isupper()
            rot_num = alphabet_position(char) + rot

            while rot_num > 25:
                rot_num -= 26

            c = chr(rot_num + 97)

            if is_upper:
                c = c.upper()

            value = value + (c,)

    return value


def main():
    message = input("Type a message: ")
    rotation_number = int(input("Rotate by: "))

    print(''.join(rotate_character(message, rotation_number)))


if __name__ == "__main__":
    main()
