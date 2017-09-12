"""
Welcome to the Loop Hole!
Today's Manager's Special is:
Crunch Jelly: A traditional jelly donut in which the jelly filling is made entirely of Capn' Crunch Oops! All Berries
How many would you like?
3.33333
How much would you like to pay per donut (suggested price is $4.35 each)?
2.5
Ok, let me prepare that for you....
After tax, your total is: $8.74999125
Thank you for snacking! Loop back around here soon!
"""

import time


def return_manager_special():
    donut_dic = {
        "Sunday": "BANANA CREAM PIE: banana glaze + vanilla wafers + powdered sugar",
        "Monday": "BLACK FOREST: raspberry glaze + mini chocolate chips + powdered sugar",
        "Tuesday": "BLACKBERRY COBBLER: blackberry glaze + graham crackers + powdered sugar",
        "Wednesday": "BLUEBERRY HILL: blueberry glaze + powdered sugar",
        "Thursday": "CARAMEL BLISS: caramel glaze + mini chocolate chips",
        "Friday": "CARNIVAL: honey glaze + rainbow sprinkles",
        "Saturday": "CHOCOLATE COVERED CHERRY: cherry glaze + mini chocolate chips"
    }

    weekday = time.strftime("%A")

    return donut_dic[weekday]


def calc_sales_price(donut, price):

    tax = 1.05
    charge = (donut * price) * tax

    return charge


def main():

    print("Welcome to the Loop Hole!\n" + "Today's Manager's Special is:")
    print(return_manager_special())

    num_donut = float(input("How many would you like? "))
    pay_donut = float(input("How much would you like to pay per donut (suggested price is $1000.00 each)? "))

    print("Ok, let me prepare that for you....")

    charge = calc_sales_price(num_donut, pay_donut)
    print("After tax, your total is: ${0:.2f}".format(charge))

    print("Thank you for snacking! Loop back around here soon!")


if __name__ == "__main__":
    main()
