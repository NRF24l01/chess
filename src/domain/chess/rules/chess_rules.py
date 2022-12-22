from typing import List

from domain.board import Board
from domain.common import Point, Color
from domain.rules import FigureRule


class RookRule(FigureRule):
    @staticmethod
    def can_move(points: List[Point], turn: Color, board: Board) -> bool:
        start, end = points
        if start[0] == end[0]:
            print("17")
            if start[1] > end[1]:
                print("21")
                for i in range(end[1] + 1, start[1]):
                    if board.get((start[0], i)) is not None:
                        print("11")
                        return False
            elif start[1] < end[1]:
                print("16")
                for i in range(start[1] + 1, end[1]):
                    if board.get((start[0], i)) is not None:
                        print("12")
                        return False
            return True
        elif start[1] == end[1]:
            print("22")
            if start[0] > end[0]:
                print("23")
                for i in range(end[0] + 1, start[0]):
                    if board.get((i, start[1])) is not None:
                        print("14", (start[1], i))
                        return False
            elif start[0] < end[0]:
                print("26")
                for i in range(end[0], start[0]):
                    if board.get((i, start[1])) is not None:
                        print("13")
                        return False
            return True
        return False
