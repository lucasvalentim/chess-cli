WHITE = 'w'
BLACK = 'b'

EMPTY = ''

WHITE_PAWN = 'P'
WHITE_KNIGHT = 'N'
WHITE_BISHOP = 'B'
WHITE_ROOK = 'R'
WHITE_QUEEN = 'Q'
WHITE_KING = 'K'

BLACK_PAWN = 'p'
BLACK_KNIGHT = 'n'
BLACK_BISHOP = 'b'
BLACK_ROOK = 'r'
BLACK_QUEEN = 'q'
BLACK_KING = 'k'

WHITE_PIECES = [WHITE_KING, WHITE_QUEEN, WHITE_ROOK, WHITE_BISHOP, WHITE_KNIGHT, WHITE_PAWN]
BLACK_PIECES = [BLACK_KING, BLACK_QUEEN, BLACK_ROOK, BLACK_BISHOP, BLACK_KNIGHT, BLACK_PAWN]

PIECES = WHITE_PIECES + BLACK_PIECES

RANK_1 = 7
RANK_2 = 6
RANK_3 = 5
RANK_4 = 4
RANK_5 = 3
RANK_6 = 2
RANK_7 = 1
RANK_8 = 0

FILE_A = 0
FILE_B = 1
FILE_C = 2
FILE_D = 3
FILE_E = 4
FILE_F = 5
FILE_G = 6
FILE_H = 7

RANKS = [8, 7, 6, 5, 4, 3, 2, 1]
FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

EMPTY_BOARD = [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
               [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]]

DEFAULT_POSITION = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
