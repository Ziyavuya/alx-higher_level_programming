#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width, self.height, self.x, self.y = width, height, x, y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print(" " * self.x + "#" * self.width) for y in range(self.y + self.height)]

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
