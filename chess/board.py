import re
from chess.constants import *
from chess.coordinate import Coordinate


class Board(object):

    def __init__(self, position=None):
        self.__squares = EMPTY_BOARD

        if position is not None:
            self.set_position(position)

        else:
            self.set_position(DEFAULT_POSITION)

    @property
    def squares(self):
        return self.__squares

    def get(self, coordinate):
        return self.__squares[coordinate.rank][coordinate.file]

    def put(self, coordinate, value):
        self.__squares[coordinate.rank][coordinate.file] = value

    def remove(self, coordinate):
        self.__squares[coordinate.rank][coordinate.file] = EMPTY

    def safe_square(self, coordinate, color):
        if coordinate.rank != RANK_8:
            if (color == WHITE and self.get(self.neighboring_squares_upper(coordinate)[0]) == BLACK_KING) or \
               (color == BLACK and self.get(self.neighboring_squares_upper(coordinate)[0]) == WHITE_KING):
                return False

            if coordinate.file != FILE_A:
                if (color == WHITE and self.get(self.neighboring_squares_upper_left(coordinate)[0]) == BLACK_KING) or \
                   (color == BLACK and self.get(self.neighboring_squares_upper_left(coordinate)[0]) == WHITE_KING):
                    return False

                if color == WHITE and self.get(self.neighboring_squares_upper_left(coordinate)[0]) == BLACK_PAWN:
                    return False

            if coordinate.file != FILE_H:
                if (color == WHITE and self.get(self.neighboring_squares_upper_right(coordinate)[0]) == BLACK_KING) or \
                   (color == BLACK and self.get(self.neighboring_squares_upper_right(coordinate)[0]) == WHITE_KING):
                    return False

                if color == WHITE and self.get(self.neighboring_squares_upper_right(coordinate)[0]) == BLACK_PAWN:
                    return False

        if coordinate.rank != RANK_1:
            if (color == WHITE and self.get(self.neighboring_squares_lower(coordinate)[0]) == BLACK_KING) or \
               (color == BLACK and self.get(self.neighboring_squares_lower(coordinate)[0]) == WHITE_KING):
                return False

            if coordinate.file != FILE_A:
                if (color == WHITE and self.get(self.neighboring_squares_lower_left(coordinate)[0]) == BLACK_KING) or \
                   (color == BLACK and self.get(self.neighboring_squares_lower_left(coordinate)[0]) == WHITE_KING):
                    return False

                if color == BLACK and self.get(self.neighboring_squares_lower_left(coordinate)[0]) == WHITE_PAWN:
                    return False

            if coordinate.file != FILE_H:
                if (color == WHITE and self.get(self.neighboring_squares_lower_right(coordinate)[0]) == BLACK_KING) or \
                   (color == BLACK and self.get(self.neighboring_squares_lower_right(coordinate)[0]) == WHITE_KING):
                    return False

                if color == BLACK and self.get(self.neighboring_squares_lower_right(coordinate)[0]) == WHITE_PAWN:
                    return False

        if coordinate.file != FILE_A:
            if (color == WHITE and self.get(self.neighboring_squares_left(coordinate)[0]) == BLACK_KING) or \
               (color == BLACK and self.get(self.neighboring_squares_left(coordinate)[0]) == WHITE_KING):
                return False

        if coordinate.file != FILE_H:
            if (color == WHITE and self.get(self.neighboring_squares_right(coordinate)[0]) == BLACK_KING) or \
               (color == BLACK and self.get(self.neighboring_squares_right(coordinate)[0]) == WHITE_KING):
                return False

        for square_coordinate in self.neighboring_squares_knight_radius(coordinate):
            if (color == WHITE and self.get(square_coordinate) == BLACK_KNIGHT) or \
               (color == BLACK and self.get(square_coordinate) == WHITE_KNIGHT):
                return False

        for squares_coordinates in [self.neighboring_squares_upper(coordinate),
                                    self.neighboring_squares_lower(coordinate),
                                    self.neighboring_squares_left(coordinate),
                                    self.neighboring_squares_right(coordinate)]:
            for square_coordinate in squares_coordinates:
                if color == WHITE:
                    if self.get(square_coordinate) in WHITE_PIECES:
                        break

                    elif self.get(square_coordinate) in [BLACK_ROOK, BLACK_QUEEN]:
                        return False

                else:
                    if self.get(square_coordinate) in BLACK_PIECES:
                        break

                    elif self.get(square_coordinate) in [WHITE_ROOK, WHITE_QUEEN]:
                        return False

        for squares_coordinates in [self.neighboring_squares_upper_left(coordinate),
                                    self.neighboring_squares_lower_right(coordinate),
                                    self.neighboring_squares_upper_right(coordinate),
                                    self.neighboring_squares_lower_left(coordinate)]:
            for square_coordinate in squares_coordinates:
                if color == WHITE:
                    if self.get(square_coordinate) in WHITE_PIECES:
                        break

                    elif self.get(square_coordinate) in [BLACK_BISHOP, BLACK_QUEEN]:
                        return False

                else:
                    if self.get(square_coordinate) in BLACK_PIECES:
                        break

                    elif self.get(square_coordinate) in [WHITE_BISHOP, WHITE_QUEEN]:
                        return False

        return True

    def set_position(self, position):
        position_strings = re.findall('\w{1,8}', position)

        for rank in range(len(position_strings)):
            file = 0

            for ch in position_strings[rank]:
                if re.match('[1-8]', ch):
                    self.put(Coordinate(rank, file), EMPTY)
                    file += int(ch)

                elif re.match('[kqrnbpKQRNBP]', ch):
                    self.put(Coordinate(rank, file), ch)
                    file += 1

    def get_position(self):
        position = []

        for square in self.squares:
            string = ''

            for value in square:
                if value == EMPTY:
                    if string == '' or re.match('[^1-8]', string[-1]):
                        string += '1'

                    else:
                        string = string.rsplit(string[-1], 1)[0] + str(int(string[-1]) + 1)

                else:
                    string += value

            position.append(string)

        return '/'.join(position)

    @staticmethod
    def coordinates():
        return [Coordinate(rank, file) for rank in range(8) for file in range(8)]

    @staticmethod
    def neighboring_squares(coordinate):
        return Board.neighboring_squares_upper(coordinate) + \
               Board.neighboring_squares_lower(coordinate) + \
               Board.neighboring_squares_left(coordinate) + \
               Board.neighboring_squares_right(coordinate) + \
               Board.neighboring_squares_upper_left(coordinate) + \
               Board.neighboring_squares_upper_right(coordinate) + \
               Board.neighboring_squares_lower_left(coordinate) + \
               Board.neighboring_squares_lower_right(coordinate) + \
               Board.neighboring_squares_knight_radius(coordinate)

    @staticmethod
    def neighboring_squares_upper(coordinate):
        return [Coordinate(rank, coordinate.file) for rank in reversed(range(coordinate.rank))]

    @staticmethod
    def neighboring_squares_lower(coordinate):
        return [Coordinate(rank, coordinate.file) for rank in range(coordinate.rank + 1, 8)]

    @staticmethod
    def neighboring_squares_left(coordinate):
        return [Coordinate(coordinate.rank, file) for file in reversed(range(coordinate.file))]

    @staticmethod
    def neighboring_squares_right(coordinate):
        return [Coordinate(coordinate.rank, file) for file in range(coordinate.file + 1, 8)]

    @staticmethod
    def neighboring_squares_upper_left(coordinate):
        return [Coordinate(coordinate.rank - x, coordinate.file - x)
                for x in range(1, 8) if coordinate.rank - x >= 0 <= coordinate.file - x]

    @staticmethod
    def neighboring_squares_upper_right(coordinate):
        return [Coordinate(coordinate.rank - x, coordinate.file + x)
                for x in range(1, 8) if coordinate.rank - x >= 0 and coordinate.file + x <= 7]

    @staticmethod
    def neighboring_squares_lower_left(coordinate):
        return [Coordinate(coordinate.rank + x, coordinate.file - x)
                for x in range(1, 8) if coordinate.rank + x <= 7 and coordinate.file - x >= 0]

    @staticmethod
    def neighboring_squares_lower_right(coordinate):
        return [Coordinate(coordinate.rank + x, coordinate.file + x)
                for x in range(1, 8) if coordinate.rank + x <= 7 >= coordinate.file + x]

    @staticmethod
    def neighboring_squares_knight_radius(coordinate):
        coordinates = []

        if coordinate.rank > RANK_7 and coordinate.file > FILE_A:
            coordinates.append(Coordinate(coordinate.rank - 2, coordinate.file - 1))

        if coordinate.rank > RANK_7 and coordinate.file < FILE_H:
            coordinates.append(Coordinate(coordinate.rank - 2, coordinate.file + 1))

        if coordinate.rank > RANK_8 and coordinate.file > FILE_B:
            coordinates.append(Coordinate(coordinate.rank - 1, coordinate.file - 2))

        if coordinate.rank > RANK_8 and coordinate.file < FILE_G:
            coordinates.append(Coordinate(coordinate.rank - 1, coordinate.file + 2))

        if coordinate.rank < RANK_1 and coordinate.file > FILE_B:
            coordinates.append(Coordinate(coordinate.rank + 1, coordinate.file - 2))

        if coordinate.rank < RANK_1 and coordinate.file < FILE_G:
            coordinates.append(Coordinate(coordinate.rank + 1, coordinate.file + 2))

        if coordinate.rank < RANK_2 and coordinate.file > FILE_A:
            coordinates.append(Coordinate(coordinate.rank + 2, coordinate.file - 1))

        if coordinate.rank < RANK_2 and coordinate.file < FILE_H:
            coordinates.append(Coordinate(coordinate.rank + 2, coordinate.file + 1))

        return coordinates
