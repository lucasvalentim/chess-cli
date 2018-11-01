from chess.constants import *


class Piece(object):

    def __init__(self, piece_value):
        if piece_value in PIECES:
            self.__value = piece_value

            if piece_value in WHITE_PIECES:
                self.__color = WHITE

            else:
                self.__color = BLACK

    @property
    def value(self):
        return self.__value

    @property
    def color(self):
        return self.__color

    def squares_available(self, board, coordinate):
        squares_available = []

        if self.value == WHITE_PAWN:
            if coordinate.rank != RANK_8:
                if board.get(board.neighboring_squares_upper(coordinate)[0]) == EMPTY:
                    squares_available.append(board.neighboring_squares_upper(coordinate)[0])

                    if coordinate.rank == RANK_2 and board.get(board.neighboring_squares_upper(coordinate)[1]) == EMPTY:
                        squares_available.append(board.neighboring_squares_upper(coordinate)[1])

                if coordinate.file != FILE_A and board.get(
                        board.neighboring_squares_upper_left(coordinate)[0]) in BLACK_PIECES:
                    squares_available.append(board.neighboring_squares_upper_left(coordinate)[0])

                if coordinate.file != FILE_H and board.get(
                        board.neighboring_squares_upper_right(coordinate)[0]) in BLACK_PIECES:
                    squares_available.append(board.neighboring_squares_upper_right(coordinate)[0])

        elif self.value == BLACK_PAWN:
            if coordinate.rank != RANK_1:
                if board.get(board.neighboring_squares_lower(coordinate)[0]) == EMPTY:
                    squares_available.append(board.neighboring_squares_lower(coordinate)[0])

                    if coordinate.rank == RANK_7 and board.get(board.neighboring_squares_lower(coordinate)[1]) == EMPTY:
                        squares_available.append(board.neighboring_squares_lower(coordinate)[1])

                if coordinate.file != FILE_A and board.get(
                        board.neighboring_squares_lower_left(coordinate)[0]) in WHITE_PIECES:
                    squares_available.append(board.neighboring_squares_lower_left(coordinate)[0])

                if coordinate.file != FILE_H and board.get(
                        board.neighboring_squares_lower_right(coordinate)[0]) in WHITE_PIECES:
                    squares_available.append(board.neighboring_squares_lower_right(coordinate)[0])

        elif self.value == WHITE_KNIGHT:
            for square_coordinate in board.neighboring_squares_knight_radius(coordinate):
                if board.get(square_coordinate) in [EMPTY] + BLACK_PIECES:
                    squares_available.append(square_coordinate)

        elif self.value == BLACK_KNIGHT:
            for square_coordinate in board.neighboring_squares_knight_radius(coordinate):
                if board.get(square_coordinate) in [EMPTY] + WHITE_PIECES:
                    squares_available.append(square_coordinate)

        elif self.value == WHITE_BISHOP:
            for squares_coordinates in [board.neighboring_squares_upper_left(coordinate),
                                        board.neighboring_squares_lower_right(coordinate),
                                        board.neighboring_squares_upper_right(coordinate),
                                        board.neighboring_squares_lower_left(coordinate)]:
                for square_coordinate in squares_coordinates:
                    if board.get(square_coordinate) == EMPTY:
                        squares_available.append(square_coordinate)

                    elif board.get(square_coordinate) in BLACK_PIECES:
                        squares_available.append(square_coordinate)
                        break

                    else:
                        break

        elif self.value == BLACK_BISHOP:
            for squares_coordinates in [board.neighboring_squares_upper_left(coordinate),
                                        board.neighboring_squares_lower_right(coordinate),
                                        board.neighboring_squares_upper_right(coordinate),
                                        board.neighboring_squares_lower_left(coordinate)]:
                for square_coordinate in squares_coordinates:
                    if board.get(square_coordinate) == EMPTY:
                        squares_available.append(square_coordinate)

                    elif board.get(square_coordinate) in WHITE_PIECES:
                        squares_available.append(square_coordinate)
                        break

                    else:
                        break

        elif self.value == WHITE_ROOK:
            for squares_coordinates in [board.neighboring_squares_upper(coordinate),
                                        board.neighboring_squares_lower(coordinate),
                                        board.neighboring_squares_left(coordinate),
                                        board.neighboring_squares_right(coordinate)]:
                for square_coordinate in squares_coordinates:
                    if board.get(square_coordinate) == EMPTY:
                        squares_available.append(square_coordinate)

                    elif board.get(square_coordinate) in BLACK_PIECES:
                        squares_available.append(square_coordinate)
                        break

                    else:
                        break

        elif self.value == BLACK_ROOK:
            for squares_coordinates in [board.neighboring_squares_upper(coordinate),
                                        board.neighboring_squares_lower(coordinate),
                                        board.neighboring_squares_left(coordinate),
                                        board.neighboring_squares_right(coordinate)]:
                for square_coordinate in squares_coordinates:
                    if board.get(square_coordinate) == EMPTY:
                        squares_available.append(square_coordinate)

                    elif board.get(square_coordinate) in WHITE_PIECES:
                        squares_available.append(square_coordinate)
                        break

                    else:
                        break

        elif self.value == WHITE_QUEEN:
            for squares_coordinates in [board.neighboring_squares_upper(coordinate),
                                        board.neighboring_squares_lower(coordinate),
                                        board.neighboring_squares_left(coordinate),
                                        board.neighboring_squares_right(coordinate),
                                        board.neighboring_squares_upper_left(coordinate),
                                        board.neighboring_squares_lower_right(coordinate),
                                        board.neighboring_squares_upper_right(coordinate),
                                        board.neighboring_squares_lower_left(coordinate)]:
                for square_coordinate in squares_coordinates:
                    if board.get(square_coordinate) == EMPTY:
                        squares_available.append(square_coordinate)

                    elif board.get(square_coordinate) in BLACK_PIECES:
                        squares_available.append(square_coordinate)
                        break

                    else:
                        break

        elif self.value == BLACK_QUEEN:
            for squares_coordinates in [board.neighboring_squares_upper(coordinate),
                                        board.neighboring_squares_lower(coordinate),
                                        board.neighboring_squares_left(coordinate),
                                        board.neighboring_squares_right(coordinate),
                                        board.neighboring_squares_upper_left(coordinate),
                                        board.neighboring_squares_lower_right(coordinate),
                                        board.neighboring_squares_upper_right(coordinate),
                                        board.neighboring_squares_lower_left(coordinate)]:
                for square_coordinate in squares_coordinates:
                    if board.get(square_coordinate) == EMPTY:
                        squares_available.append(square_coordinate)

                    elif board.get(square_coordinate) in WHITE_PIECES:
                        squares_available.append(square_coordinate)
                        break

                    else:
                        break

        elif self.value == WHITE_KING:
            if coordinate.rank != RANK_8:
                if board.get(board.neighboring_squares_upper(coordinate)[0]) in [EMPTY] + BLACK_PIECES:
                    squares_available.append(board.neighboring_squares_upper(coordinate)[0])

                if coordinate.file != FILE_A and board.get(
                        board.neighboring_squares_upper_left(coordinate)[0]) in [EMPTY] + BLACK_PIECES:
                    squares_available.append(board.neighboring_squares_upper_left(coordinate)[0])

                if coordinate.file != FILE_H and board.get(
                        board.neighboring_squares_upper_right(coordinate)[0]) in [EMPTY] + BLACK_PIECES:
                    squares_available.append(board.neighboring_squares_upper_right(coordinate)[0])

            if coordinate.rank != RANK_1:
                if board.get(board.neighboring_squares_lower(coordinate)[0]) in [EMPTY] + BLACK_PIECES:
                    squares_available.append(board.neighboring_squares_lower(coordinate)[0])

                if coordinate.file != FILE_A and board.get(
                        board.neighboring_squares_lower_left(coordinate)[0]) in [EMPTY] + BLACK_PIECES:
                    squares_available.append(board.neighboring_squares_lower_left(coordinate)[0])

                if coordinate.file != FILE_H and board.get(
                        board.neighboring_squares_lower_right(coordinate)[0]) in [EMPTY] + BLACK_PIECES:
                    squares_available.append(board.neighboring_squares_lower_right(coordinate)[0])

            if coordinate.file != FILE_A and board.get(
                    board.neighboring_squares_left(coordinate)[0]) in [EMPTY] + BLACK_PIECES:
                squares_available.append(board.neighboring_squares_left(coordinate)[0])

            if coordinate.file != FILE_H and board.get(
                    board.neighboring_squares_right(coordinate)[0]) in [EMPTY] + BLACK_PIECES:
                squares_available.append(board.neighboring_squares_right(coordinate)[0])

        elif self.value == BLACK_KING:
            if coordinate.rank != RANK_8:
                if board.get(board.neighboring_squares_upper(coordinate)[0]) in [EMPTY] + WHITE_PIECES:
                    squares_available.append(board.neighboring_squares_upper(coordinate)[0])

                if coordinate.file != FILE_A and board.get(
                        board.neighboring_squares_upper_left(coordinate)[0]) in [EMPTY] + WHITE_PIECES:
                    squares_available.append(board.neighboring_squares_upper_left(coordinate)[0])

                if coordinate.file != FILE_H and board.get(
                        board.neighboring_squares_upper_right(coordinate)[0]) in [EMPTY] + WHITE_PIECES:
                    squares_available.append(board.neighboring_squares_upper_right(coordinate)[0])

            if coordinate.rank != RANK_1:
                if board.get(board.neighboring_squares_lower(coordinate)[0]) in [EMPTY] + WHITE_PIECES:
                    squares_available.append(board.neighboring_squares_lower(coordinate)[0])

                if coordinate.file != FILE_A and board.get(
                        board.neighboring_squares_lower_left(coordinate)[0]) in [EMPTY] + WHITE_PIECES:
                    squares_available.append(board.neighboring_squares_lower_left(coordinate)[0])

                if coordinate.file != FILE_H and board.get(
                        board.neighboring_squares_lower_right(coordinate)[0]) in [EMPTY] + WHITE_PIECES:
                    squares_available.append(board.neighboring_squares_lower_right(coordinate)[0])

            if coordinate.file != FILE_A and board.get(
                    board.neighboring_squares_left(coordinate)[0]) in [EMPTY] + WHITE_PIECES:
                squares_available.append(board.neighboring_squares_left(coordinate)[0])

            if coordinate.file != FILE_H and board.get(
                    board.neighboring_squares_right(coordinate)[0]) in [EMPTY] + WHITE_PIECES:
                squares_available.append(board.neighboring_squares_right(coordinate)[0])

        return squares_available
