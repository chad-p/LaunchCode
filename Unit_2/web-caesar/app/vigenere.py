from helpers import alphabet_position, rotate_character


def format_key(key):

    if isinstance(key, int):
        yield key

    elif isinstance(key, str):
        for char in key:
            yield alphabet_position(char)

    else:
        return 0


def encrypt(message, key):

    message_list = []

    key_gen = format_key(key)
    key_list = list(key_gen)
    key_size = len(key_list)
    key_iterator = 0

    for char in message:

        if char.isalpha():

            if key_iterator > key_size - 1:
                key_iterator = 0

            # key_num = alphabet_position(key_tup[key_iterator])
            key_num = key_list[key_iterator]
            message_list.append(rotate_character(char, key_num))

            key_iterator += 1
        else:
            message_list.append(char)

    return_message = ''.join(message_list)
    return return_message


def main():
    # message = input("Type a message: ")
    # key = int(input("Rotate by: "))

    message = "Hello, World!"
    key = "103"

    encrypted_message = encrypt(message, key)
    print(encrypted_message)


if __name__ == "__main__":
    main()
