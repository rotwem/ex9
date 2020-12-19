HORIZONTAL = 1
VERTICAL = 0
HORIZONTAL_CAR_MOVES = {"r": "cause the car to move right", "l": "cause the car to move left"}
VERTICAL_CAR_MOVES = {"u": "cause the car to move up", "d": "cause the car to move down"}


class Car:
    """
    A class of car object, each car has these private attributions:
    a name - string
    length - int - how many "blocks" it occupies
    location - tuple of ints - the first coordinate of the car - meaning the nearest coordinate to (0,0)
    orientation -  0/1 - 0 if the car is VERTICAL and 1 if the car is HORIZONTAL
    the class also has methods to change and get attributes and receive information about a car instance
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        car_len = self.__length
        car_row, car_col = self.__location
        car_orient = self.__orientation
        car_coordinates = [self.__location]
        if car_orient == HORIZONTAL:
            for i in range(car_len - 1):
                car_col += 1
                car_location = (car_row, car_col)
                car_coordinates.append(car_location)
        else:
            for i in range(car_len - 1):
                car_row += 1
                car_location = (car_row, car_col)
                car_coordinates.append(car_location)
        return car_coordinates

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        if self.__orientation == VERTICAL:
            return VERTICAL_CAR_MOVES
        else:
            return HORIZONTAL_CAR_MOVES

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        car_possible_moves = self.possible_moves()
        car_coordinates = self.car_coordinates()
        first_coordinate = car_coordinates[0]
        first_row, first_col = first_coordinate
        last_coordinate = car_coordinates[len(car_coordinates) - 1]
        last_row, last_col = last_coordinate
        if movekey in car_possible_moves.keys():
            if movekey == "u":
                return [(first_row - 1, first_col)]
            elif movekey == "d":
                return [(last_row + 1, last_col)]
            elif movekey == "r":
                return [(last_row, last_col + 1)]
            else:
                return [(first_row, first_col - 1)]

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if movekey in self.possible_moves().keys():
            row, col = self.__location
            if movekey == "u":
                self.__location = (row - 1, col)
            elif movekey == "d":
                self.__location = (row + 1, col)
            elif movekey == "r":
                self.__location = (row, col + 1)
            else:
                self.__location = (row, col - 1)
            return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
