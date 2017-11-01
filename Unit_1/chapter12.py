class Car:

    def __init__(self, gas_level):

        self.gas_level = gas_level


    def add_gas(self, amount_to_add):

        self.gas_level += amount_to_add
        return amount_to_add


    def fill_up(self):

        if self.gas_level < 13:
            return self.add_gas(13 - self.gas_level)
        else:
            return 0


honda = Car(9)
ford = Car(18)
