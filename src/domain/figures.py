import abc
from typing import Tuple
from domain.common import Color
from board import Board


class Figure:
    def __init__(self, color: Color):
        self.color = color

    @abc.abstractmethod
    def can_move(self, start, end, board: Board):
        raise NotImplementedError

    def moved(self, start, end, board: Board):
        pass

    @abc.abstractmethod
    def __repr__(self):
        raise NotImplementedError

    def _colorise(self, s):
        if self.color == Color.WHITE:
            return s.upper()
        return s

    def _direction(self, board: Board):
        if self.color == board.color:
            return -1
        else:
            return 1


class Pawn(Figure):
    def __init__(self, color: Color):
        super().__init__(color)
        self.__is_moved = False

    def can_move(self, start, end, board: Board):
        direction = self._direction(board)

        # прямой ход
        if start[0] == end[0]:
            if end[1] == start[1] + direction and board.get(end) is None:
                return True
            if end[1] == start[1] + 2 * direction and board.get(end) is None and board.get(
                    (start[0], start[1] + direction)) is None and not self.__is_moved:
                return True
        # косой ход
        if abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 1:
            if board.get(end) is not None and board.get(end).color != self.color:
                return True

        return False

    def moved(self, start, end, board: Board):
        self.__is_moved = True

    def __repr__(self):
        return self._colorise("p")  # Пешка, вообще говоря, не записывается в нотации)


class Rook(Figure):
    # Ладья
    def __init__(self, color: Color):
        super().__init__(color)

    def __repr__(self):
        return self._colorise("r")

    def moved(self, start, end, board):
        pass

    def can_move(self, start, end, board: Board):
        if start[0] == end[0]:
            if start[1] > end[1]:
                for i in range(end[1] + 1, start[1]):
                    if board.get((start[0], i)) != None:
                        return False
            elif start[1] < end[1]:
                for i in range(start[1], end[1] - 1):
                    if board.get((start[0], i)) != None:
                        return False
            return True
        elif start[1] == end[1]:
            if start[0] > end[0]:
                for i in range(end[0] + 1, start[0]):
                    if board.get((start[1], i)) != None:
                        return False
            elif start[0] < end[0]:
                for i in range(start[0], end[0] - 1):
                    if board.get((start[1], i)) != None:
                        return False
            return True
        return False


class Bishop(Figure):
    # Слон
    def __init__(self, color: Color):
        super().__init__(color)

    def __repr__(self):
        return self._colorise("b")

    def moved(self, start, end, board: Board):
        pass

    def can_move(self, start, end, board: Board):
        pass


class Knight(Figure):
    # Конь
    def __init__(self, color: Color):
        super().__init__(color)

    def __repr__(self):
        return self._colorise("n")  # В шахматной нотации Конь это не "Horse", а N, от kNight

    def moved(self, start, end, board: Board):
        pass

    def can_move(self, start, end, board: Board):
        pass


class Queen(Figure):
    def __init__(self, color: Color):
        super().__init__(color)

    def __repr__(self):
        return self._colorise("q")

    def moved(self, start, end, board: Board):
        pass

    def can_move(self, start, end, board: Board):
        pass


class King(Figure):
    def __init__(self, color: Color):
        super().__init__(color)

    def __repr__(self):
        return self._colorise("k")

    def moved(self, start, end, board: Board):
        pass

    def can_move(self, start, end, board: Board):
        pass
