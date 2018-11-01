import os
import re
from termcolor import colored
from chess.constants import *
from chess.coordinate import Coordinate
from chess.board import Board
from chess.piece import Piece

class Chess(object):
    def __init__(self, position=None):
        self.__board = Board(position)
        self.__turn = WHITE
        self.__movements = []

    @property
    def turn(self):
        return self.__turn

    def change_turn(self):
        if self.turn == WHITE:
            self.__turn = BLACK
        else:
            self.__turn = WHITE

    def king_coordinate(self, color):
        for square_coordinate in self.__board.coordinates():
            if (color == WHITE and self.__board.get(square_coordinate) == WHITE_KING) or \
               (color == BLACK and self.__board.get(square_coordinate) == BLACK_KING):
                    return square_coordinate

    def pieces_coordinates(self, color):
        pieces_coordinates = []

        for square_coordinate in self.__board.coordinates():
            if (color == WHITE and self.__board.get(square_coordinate) in WHITE_PIECES) or \
               (color == BLACK and self.__board.get(square_coordinate) in BLACK_PIECES):
                    pieces_coordinates.append(square_coordinate)

        return pieces_coordinates

    def in_check(self):
        if not self.__board.safe_square(self.king_coordinate(WHITE), WHITE):
            return True

        if not self.__board.safe_square(self.king_coordinate(BLACK), BLACK):
            return True

        return False

    def in_checkmate(self):
        if self.in_check() and not self.moves_leave_check():
            return True

        return False

    def moves_leave_check(self):
        moves_leave_check = []

        for piece_coordinate in self.pieces_coordinates(self.__turn):
            piece_ = Piece(self.__board.get(piece_coordinate))

            for to_square_coordinate in piece_.squares_available(self.__board, piece_coordinate):
                if piece_.value in [WHITE_KING, BLACK_KING] and not self.__board.safe_square(
                        to_square_coordinate, self.__turn):
                    continue

                self.hypothetical_move(piece_coordinate, to_square_coordinate)

                if not self.in_check():
                    moves_leave_check.append((piece_coordinate.coordinate, to_square_coordinate.coordinate))

                self.undo()

        return moves_leave_check

    def hypothetical_move(self, from_square_coordinate, to_square_coordinate):
        from_square_value = self.__board.get(from_square_coordinate)
        to_square_value = self.__board.get(to_square_coordinate)

        self.__board.remove(from_square_coordinate)
        self.__board.put(to_square_coordinate, from_square_value)

        self.change_turn()

        self.__movements.append({
            'from_square_coordinate': from_square_coordinate,
            'to_square_coordinate': to_square_coordinate,
            'from_square_value': from_square_value,
            'to_square_value': to_square_value
        })

    def move(self, movement):
        if self.in_checkmate():
            return False

        if not re.match('^[a-h][1-8]-[a-h][1-8]$', movement):
            return False

        from_square_coordinate = Coordinate(notation=movement.split('-')[0])
        to_square_coordinate = Coordinate(notation=movement.split('-')[1])

        from_square_value = self.__board.get(from_square_coordinate)
        to_square_value = self.__board.get(to_square_coordinate)

        if (self.__turn == WHITE and from_square_value not in WHITE_PIECES) or \
           (self.__turn == BLACK and from_square_value not in BLACK_PIECES):
            return False

        from_square_piece = Piece(from_square_value)

        if to_square_coordinate.coordinate not in [square.coordinate for square in from_square_piece.squares_available(
                self.__board, from_square_coordinate)]:
            return False

        if from_square_value in [WHITE_KING, BLACK_KING] and not self.__board.safe_square(
                to_square_coordinate, self.__turn):
            return False

        if self.in_check() and (from_square_coordinate.coordinate,
                                to_square_coordinate.coordinate) not in self.moves_leave_check():
            return False

        self.__board.remove(from_square_coordinate)
        self.__board.put(to_square_coordinate, from_square_value)

        self.change_turn()

        self.__movements.append({
            'from_square_coordinate': from_square_coordinate,
            'to_square_coordinate': to_square_coordinate,
            'from_square_value': from_square_value,
            'to_square_value': to_square_value
        })

        return True

    def undo(self):
        last_movement = self.__movements[-1]

        self.__board.put(last_movement['from_square_coordinate'], last_movement['from_square_value'])
        self.__board.put(last_movement['to_square_coordinate'], last_movement['to_square_value'])

        self.change_turn()

        del self.__movements[-1]

    def draw_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print('     a b c d e f g h     ')
        print('   +—————————————————+   ')

        for rank in range(len(self.__board.squares)):
            rank_string = ' ' + str(RANKS[rank]) + ' |'

            for square_value in self.__board.squares[rank]:
                if square_value == EMPTY:
                    rank_string = rank_string + ' •'

                else:
                    if square_value in WHITE_PIECES:
                        rank_string = rank_string + ' ' + colored(square_value, 'yellow')

                    else:
                        rank_string = rank_string + ' ' + colored(square_value, 'cyan')

            rank_string = rank_string + ' | ' + str(RANKS[rank]) + ''

            print(rank_string)

        print('   +—————————————————+   ')
        print('     a b c d e f g h     ')
