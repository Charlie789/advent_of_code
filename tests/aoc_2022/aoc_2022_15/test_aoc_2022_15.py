from pathlib import Path
import pytest

import advent_of_code.aoc_2022.aoc_2022_15.aoc_2022_15 as aoc

from advent_of_code.aoc_2022.aoc_2022_15.aoc_2022_15 import Position

@pytest.fixture
def example():
    data = (Path(__file__).parent / "example.txt").read_text().rstrip()
    return aoc.parse(data)


def test_task1(example):
    assert aoc.task1(example, 10) == 26


def test_task2(example):
    assert aoc.task2(example, 20) == 56000011
