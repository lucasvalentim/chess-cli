from chess.constants import *


class Coordinate(object):

    def __init__(self, rank=None, file=None, notation=None):
        if notation is not None:
            self.__rank = RANKS.index(int(notation[1]))
            self.__file = FILES.index(notation[0])

        else:
            self.__rank = rank
            self.__file = file

    @property
    def rank(self):
        return self.__rank

    @property
    def file(self):
        return self.__file

    @property
    def coordinate(self):
        return self.__rank, self.__file
