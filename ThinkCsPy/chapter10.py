def get_country_codes(prices):
    country_code = []
    #print(prices)
    prices = prices.split()

    for price in prices:
        #print(price)
        country_code.append(price[0:2])

    return ", ".join(country_code)


def main():
    get_country_codes("NZ$300, KR$1200, DK$5")

main()