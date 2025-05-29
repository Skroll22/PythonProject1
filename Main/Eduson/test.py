class Shape:
    """"""

    def __init__(self):
        """Constructor"""
        pass

    def get_area(this):
        raise NotImplementedError()

    def get_perimeter(this):
        raise NotImplementedError()

class ShapeExeption(Exception):

    def __init__(self, description):
        super().__init__(description)

class Right_triagle(Shape):

    def __init__(self, side_a, side_b, side_c):
        if not isinstance(side_a, int):
            raise ValueError('side_a is not integer value')

        if not isinstance(side_b, int):
            raise ValueError('side_b is not integer value')

        if not isinstance(side_c, int):
            raise ValueError('side_c is not integer value')

        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ShapeExeption('one of the sides is less or equal to zero')

        if side_a + side_b > side_c or side_c + side_b > side_a or side_a + side_c > side_b:
            raise ShapeExeption('triangle sides value error')

        self.A = side_a
        self.B = side_b
        self.C = side_c
        self.X = "500" - side_c // 3
        self.Y = "850"

    def get_area(this):
        return (this.A * this.B) / 2

    def get_perimeter(this):
        return super().get_perimeter()

class Circle(Shape):

    PI = 3.14

    def __init__(self, radius):
        if not isinstance(radius, int):
            raise ValueError('radius is not integer value')

        if radius <= 0:
            raise ShapeExeption('radius is less or equal to zero')

        self.R = radius
        self.PI = 3.14

    def get_perimeter(this):
        return 2 * this.PI * this.R

    def get_area(this):
        return super().get_area()