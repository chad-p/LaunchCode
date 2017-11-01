def get_initials(fullname):

    initials = []

    for name in fullname.split(" "):
        initials.append(name[0].capitalize())

    return "".join(initials)


def main():
    # some more code here (input and print statements)
    ozzie_inits = get_initials("ozzie Smith")
    print("The initials of 'Ozzie Smith' are", ozzie_inits)

    day_lewis_inits = get_initials("Daniel Day Lewis")
    print("The initials of 'Daniel Day Lewis' are", day_lewis_inits)

    users_fullname = input("What is your full name? ")
    users_inits = get_initials(users_fullname)
    print(users_inits)


if __name__ == '__main__':
    main()
