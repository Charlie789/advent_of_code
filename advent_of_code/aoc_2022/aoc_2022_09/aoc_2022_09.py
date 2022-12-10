import math
from pathlib import Path
from collections import namedtuple
from typing import Set, Tuple


Move = namedtuple("Move", "direction quantity")


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.on_moved = None
        self.to_follow = None

    def move_up(self):
        self.y += 1
        if self.on_moved:
            self.on_moved()

    def move_down(self):
        self.y -= 1
        if self.on_moved:
            self.on_moved()

    def move_left(self):
        self.x -= 1
        if self.on_moved:
            self.on_moved()

    def move_right(self):
        self.x += 1
        if self.on_moved:
            self.on_moved()

    def move_diag_up_left(self):
        self.y += 1
        self.x -= 1
        if self.on_moved:
            self.on_moved()

    def move_diag_up_right(self):
        self.y += 1
        self.x += 1
        if self.on_moved:
            self.on_moved()

    def move_diag_down_left(self):
        self.y -= 1
        self.x -= 1
        if self.on_moved:
            self.on_moved()

    def move_diag_down_right(self):
        self.y -= 1
        self.x += 1
        if self.on_moved:
            self.on_moved()

    def follow_to(self):
        p = self.to_follow

        distance = Position.distance(self, p)

        if distance < 2:
            return
        elif distance == 2:
            if self.x - p.x == 2:
                self.move_left()
            elif self.x - p.x == -2:
                self.move_right()
            elif self.y - p.y == 2:
                self.move_down()
            elif self.y - p.y == -2:
                self.move_up()
        else:
            if self.x - p.x > 0 and self.y - p.y > 0:
                self.move_diag_down_left()
            elif self.x - p.x > 0 and self.y - p.y < 0:
                self.move_diag_up_left()
            elif self.x - p.x < 0 and self.y - p.y > 0:
                self.move_diag_down_right()
            elif self.x - p.x < 0 and self.y - p.y < 0:
                self.move_diag_up_right()

    @staticmethod
    def distance(p1: "Position", p2: "Position"):
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

class Rope:
    def __init__(self, points):
        self.points = [Position(0, 0) for _ in range(points)]

        for i in range(1, points):
            self.points[i - 1].on_moved = self.points[i].follow_to
            self.points[i].to_follow = self.points[i - 1]


        self.head_position = self.points[0]
        self.tail_position = self.points[-1]
        self.tail_position.on_moved = self.save_position
        self.visited_positions: Set[Tuple[int, int]] = {(0, 0)}

    def save_position(self):
        self.visited_positions.add((self.tail_position.x, self.tail_position.y))

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

    def move_right(self):
        self.head_position.move_right()

    def move_up(self):
        self.head_position.move_up()

    def move_down(self):
        self.head_position.move_down()


def parse(raw_input):
    parsed_input = [Move(*line.split(" ")) for line in raw_input.splitlines()]

    return parsed_input


def task1(parsed_input):
    rope = Rope(2)
    for move in parsed_input:
        rope.perform_move(move)
    return len(rope.visited_positions)


def task2(parsed_input):
    rope = Rope(10)
    for move in parsed_input:
        rope.perform_move(move)
    return len(rope.visited_positions)


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().rstrip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
