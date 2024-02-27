#!/usr/bin/python3
"""This module contains a Rectangle class that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """This is a Rectangle class the inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This is the constructor of the Rectangle class with the
        following:

        Args:
            width (int): Width of the rectangle set to a private instance
                attributes.
            height (int): Height of the rectangle set to a private
                instance attribute.
            x (int): x coordinate of the rectangle
            y (int): y coordinate of the rectangle
            id (int): id of the rectangle
        """

        self.id = id

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        # Validating each attribute with attribute validator
        self.attribute_validator("width",  self.__width)
        self.attribute_validator("height", self.__height)
        self.attribute_validator("x", self.__x)
        self.attribute_validator("y", self.__y)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, width):
        self.attribute_validator("width", width)
        self.__width = width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, height):
        self.attribute_validator("height", height)
        self.__height = height

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, x):
        self.attribute_validator("x", x)
        self.__x = x

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, y):
        self.attribute_validator("y", y)
        self.__y = y

    def __str__(self):
        """Overides the default __str__:
        Returns:
            '[Rectangle] (<id>) <x>/<y> - <width>/<height>'
        """
        return_string = "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                       self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)
        return (return_string)

    def area(self):
        """Calculates and returns the area value of the Rectangle Instance"""
        return (self.__width * self.__height)

    def display(self):
        """Prints in stdout the Rectangle instance with '#'"""
        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end="")
            print('\n', end="")

    @staticmethod
    def attribute_validator(attr_name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr_name))
        if (attr_name == 'x' or attr_name == 'y') and (value < 0):
            raise ValueError("{} must be >= 0".format(attr_name))
        if (attr_name == 'height' or attr_name == "width") and value <= 0:
            raise ValueError("{} must be > 0".format(attr_name))
