import math
from pathlib import Path
from collections import namedtuple
from typing import Set, Tuple


Move = namedtuple("Move", "direction quantity")


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_diag_up_left(self):
        self.move_up()
        self.move_left()

    def move_diag_up_right(self):
        self.move_up()
        self.move_right()

    def move_diag_down_left(self):
        self.move_down()
        self.move_left()

    def move_diag_down_right(self):
        self.move_down()
        self.move_right()

    @staticmethod
    def distance(p1: "Position", p2: "Position"):
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

class Rope:
    def __init__(self):
        self.head_position = Position(0, 0)
        self.tail_position = Position(0, 0)
        self.visited_positions: Set[Tuple[int, int]] = {(0, 0)}

    def save_position(self):
        self.visited_positions.add((self.tail_position.x, self.tail_position.y))

    def distance(self):
        return Position.distance(self.tail_position, self.head_position)

    def distance_x(self):
        return self.head_position.x - self.tail_position.x

    def distance_y(self):
        return self.head_position.y - self.tail_position.y

    def perform_move(self, move: Move):
        if move.direction == "L":
            for _ in range(int(move.quantity)):
                self.move_left()
        elif move.direction == "R":
            for _ in range(int(move.quantity)):
                self.move_right()
        elif move.direction == "U":
            for _ in range(int(move.quantity)):
                self.move_up()
        elif move.direction == "D":
            for _ in range(int(move.quantity)):
                self.move_down()

    def move_left(self):
        self.head_position.move_left()
        if self.distance() < 2:
            return
        if self.distance() == 2:
            self.tail_position.move_left()
        else:
            if self.distance_y() == 1:
                self.tail_position.move_diag_up_left()
            if self.distance_y() == -1:
                self.tail_position.move_diag_down_left()
        self.save_position()

    def move_right(self):
        self.head_position.move_right()
        if self.distance() < 2:
            return
        if self.distance() == 2:
            self.tail_position.move_right()
        else:
            if self.distance_y() == 1:
                self.tail_position.move_diag_up_right()
            if self.distance_y() == -1:
                self.tail_position.move_diag_down_right()
        self.save_position()

    def move_up(self):
        self.head_position.move_up()
        if self.distance() < 2:
            return
        if self.distance() == 2:
            self.tail_position.move_up()
        else:
            if self.distance_x() == 1:
                self.tail_position.move_diag_up_right()
            if self.distance_x() == -1:
                self.tail_position.move_diag_up_left()
        self.save_position()

    def move_down(self):
        self.head_position.move_down()
        if self.distance() < 2:
            return
        if self.distance() == 2:
            self.tail_position.move_down()
        else:
            if self.distance_x() == 1:
                self.tail_position.move_diag_down_right()
            if self.distance_x() == -1:
                self.tail_position.move_diag_down_left()
        self.save_position()


def parse(raw_input):
    parsed_input = [Move(*line.split(" ")) for line in raw_input.splitlines()]

    return parsed_input


def task1(parsed_input):
    rope = Rope()
    for move in parsed_input:
        rope.perform_move(move)
    return len(rope.visited_positions)


def task2(parsed_input):
    return parsed_input


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().rstrip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
