import sys
import json
from helper import *
from board import Board
from car import Car

VALID_CAR_NAMES = ["Y", "B", "O", "W", "G", "R"]
VALID_CAR_LEN = [2, 3, 4]
VALID_CAR_ORIENTATION = [0, 1]
VALID_CAR_MOVEMENTS = ["u", "d", "r", "l"]


class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.__board = board
        self.__target_status = board.cell_content(board.target_location())

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        print("look at the board now...")
        print(self.__board)
        invalid_input = True
        while invalid_input:
            user_move = input("what's your next move?")
            if user_move == "!":
                print("okay bye...")
                return False
            try:
                move_car_name, user_movekey = user_move
            except:
                print("couldnt read your input, try again")
                break
            if move_car_name not in VALID_CAR_NAMES or user_move not in VALID_CAR_MOVEMENTS:
                print("your input is invalid")
                break
            elif not self.__board.move_car(move_car_name, user_movekey):
                print("sorry cant move this car")
                break
            else:
                invalid_input = False
            print("look at the board now...")
            print(self.__board)
            return True



    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code here (and then delete the next line - 'pass')
        while self.__target_status is None:
            if not self.__single_turn():
                return
            else:
                self.__target_status = self.__board.cell_content(self.__board.target_location())
        print("good job!!!")
        return
        #     print(self.__board)
        #     user_input = input("what's your next move?")
        #     if user_input == "!":
        #         print("okay bye")
        #         break
        #     else:
        #         move_car_name, movekey = user_input
        #     try:
        #         self.__board.move_car(move_car_name, movekey)
        #         self.__target_status = self.__board.cell_content(self.__board.target_location())
        #     except:
        #         print("bad move... try again")
        # print(self.__board)
        # print("you win")


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    game_board = Board()
    json_file_name = sys.argv[1]
    cars_dict = load_json(json_file_name)
    for car_name in cars_dict:
        if car_name not in VALID_CAR_NAMES:
            continue
        car_len = cars_dict[car_name][0]
        car_row, car_col = cars_dict[car_name][1][0], cars_dict[car_name][1][1]
        car_orientation = cars_dict[car_name][2]
        if car_len in VALID_CAR_LEN and car_orientation in VALID_CAR_ORIENTATION:
            car = Car(car_name, car_len, (car_row, car_col), car_orientation)
            game_board.add_car(car)
    new_game = Game(game_board)
    new_game.play()
