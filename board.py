EXIT = "Exit"


class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        board_list = []
        for i in range(7):
            row = []
            if i == 3:
                for j in range(8):
                    if j != 7:
                        row.append(0)
                    else:
                        row.append(EXIT)
            else:
                for j in range(7):
                    row.append(0)
            board_list.append(row)
        self.__board = board_list
        self.__empty_cells = self.cell_list() #list of tuples
        self.__cells_with_cars = [] # list of tuples
        self.__cars_on_board = [] # list of Cars

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        board_list = self.__board
        print_str = ""
        for i in range(len(board_list)):
            print_str = print_str + str(board_list[i]) + "\n"
        return print_str

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        cell_list = []
        for i in range(7):
            if i == 3:
                for j in range(8):
                    cell_list.append((i, j))
            else:
                for j in range(7):
                    cell_list.append((i, j))
        return cell_list

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        result = []
        for car in self.__cars_on_board:
            moves = car.possible_moves()
            for direction, description in moves.items():
                result.append([car.get_name(), direction, description])
        return result

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return (3, 7)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name of the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        row, col = coordinate
        if self.__board[row][col] == 0:
            return
        else:
            for car in self.__cars_on_board:
                if coordinate in car.car_coordinates():
                    return car.get_name()

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        if car in self.__cars_on_board:
            return False
        coordinates = car.car_coordinates()
        for coordinate in coordinates:
            if coordinate in self.__cells_with_cars:
                return False
            else:
                row, col = coordinate
                self.__board[row][col] = car.get_name()
                self.__cells_with_cars.append(coordinate)
        self.__cars_on_board.append(car)
        return True

    def remove_car_from_board(self, car):
        self.__cars_on_board.remove(car)
        car_coordinates = car.car_coordinates()
        for coordinate in car_coordinates:
            row, col = coordinate
            self.__board[row][col] = 0

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        for car in self.__cars_on_board:
            if car.get_name() == name:
                car_to_move = car
            else:
                return False
        move_requirements = car_to_move.movement_requirements(movekey)
        if move_requirements[0] in self.__empty_cells:
            self.remove_car_from_board(car_to_move)
            car_to_move.move(movekey)
            self.add_car(car_to_move)
            return True
        else:
            return False

