class Rectangle(object):
    """
    A rectangle has a length and a width. A rectangle should be able to provide its area and perimeter.
    A rectangle can indicate whether it is smaller than another rectangle in terms of area.
    A rectangle can indicate whether it is in fact a square.
    """

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def set_length_width(self, length, width):
        self.length = length
        self.width = width

    def get_length_width(self):
        return "Rectangle's length is {} and width is {}.".format(self.length, self.width)

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def is_smaller(self, other):
        return self.get_area() < other.get_area()

    def am_i_a_square(self):
        if self.length == self.width:
            return "I'm a square."
        else:
            return "I'm all rectangle."


chad = Rectangle(length=5, width=5)
print(chad.get_area())
print(chad.get_perimeter())
print(chad.get_length_width())
print(chad.am_i_a_square())

joe = Rectangle(length=10, width=5)
print(joe.get_area())
print(joe.get_perimeter())
print(joe.get_length_width())
print(joe.am_i_a_square())

print(chad.is_smaller(joe))
