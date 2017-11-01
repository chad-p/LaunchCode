def is_leap(year):
    if year % 100 == 0:  # Check if a century
        if (year / 100) % 4 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


def main():
    year = int(input("Give me a year and I will return \"True\" if leap year and \"False\" otherwise: "))

    print(is_leap(year))


if __name__ == "__main__":
    main()
