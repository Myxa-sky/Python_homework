import math


def square(side):
    area = side * side
    if not isinstance(side, int):  # Если side не целое число
        area = math.ceil(area)
    return area


print(square(5.8))
