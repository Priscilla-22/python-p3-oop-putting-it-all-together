#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        self._condition = "New"

    @property
    def brand(self):
        return self._brand

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            print("size must be an integer")
        self._size = new_size

    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"

    @property
    def condition(self):
        return self._condition


quality_shoe = Shoe("AirMax", 9)
print(quality_shoe.brand)
print(quality_shoe.size)
print(quality_shoe.condition)
quality_shoe.size = 36
print(quality_shoe.size)

quality_shoe.cobble()
print(quality_shoe.condition)
