from helpers import alphabet_position, rotate_character


def encrypt(message, key):

    return_message = []

    for char in message:

        if char.isalpha():
            return_message.append(rotate_character(char, key))
        else:
            return_message.append(char)

    return ''.join(return_message)


def main():
    # message = input("Type a message: ")
    # key = int(input("Rotate by: "))

    message = "Hello, World!"
    key = 5

    encrypted_message = encrypt(message, key)
    print(encrypted_message)

if __name__ == "__main__":
    main()
