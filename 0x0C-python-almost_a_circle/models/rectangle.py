#!/usr/bin/python3
"""Module containing the definition of class rectangle
class Rectangle inherits from class Base
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inheriting from class Base
    Containing all attributes and methods required"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class Rectangle
        Args:
            - width (int)
            - height (int)
            - x (int)
            - y (int)
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width
        Args:
            - self
            - value
        Raises:
            - TypeError for wrong width type
            - ValueError for width less or equal to zero
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height
        Args:
            - self
            - value
        Raises:
            - TypeError for wrong height type
            - ValueError for height less or equal to zero
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x attribute"""

        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x
        Args:
            - self
            - value
        Raises:
            - TypeError for wrong x type
            - ValueError for x less or equal to zero
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y
        Args:
            - self
            - value
        Raises:
            - TypeError for wrong y type
            - ValueError for y less or equal to zero
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the rectangle instance
        Area: height x width
        """

        return self.height * self.width

    def display(self):
        """Prints in stdout, the Rectangle instance with the character #
        with dimensions self.height and self.width
        """

        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__:
        """Returns a string representation of the Rectangle object
        Prints all defining variables
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)
