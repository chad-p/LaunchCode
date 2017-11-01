"""
It is possible to name the days 0 through 6, where day 0 is Sunday and day 6 is Saturday.
If you go on a wonderful holiday leaving on day 3 (a Wednesday) and you return home after 10 nights, you arrive home on day 6 (a Saturday).

Write a general version of the program which asks for the day number that your vacation starts on and the length of your holiday,
and then tells you the number of the day of the week you will return on.
"""


def calc_return_day(start_day, length):
    return_day = (start_day + length) % 7
    return return_day


def main():

    vacation_start_day = input("What day does your vacation start on? ")
    length_of_holiday = int(input("How many days are you on holiday? "))

    #vacation_start_day = "Wednesday"
    #length_of_holiday = 10

    vacation_start_day = vacation_start_day.lower()

    weekday_dict = {
        "sunday": 0,
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6
    }

    return_num = calc_return_day(weekday_dict[vacation_start_day], length_of_holiday)

    for day, num in weekday_dict.items():
        if num == return_num:
            return_day = day

    print("You are leaving on day number: {} ({})".format(weekday_dict[vacation_start_day], vacation_start_day.capitalize()))
    print("You will be returning from your {} day trip on a {}.".format(length_of_holiday, return_day.capitalize()))


if __name__ == "__main__":
    main()
