from pathlib import Path
import pytest

import advent_of_code.aoc_2022.aoc_2022_06.aoc_2022_06 as aoc


@pytest.fixture
def example():
    with open(Path(__file__).parent / "example.txt", "r") as f:
        data = f.readlines()
    return aoc.parse(data)


def test_task1(example):
    assert aoc.task1(example) == 7


def test_task2(example):
    assert aoc.task2(example) == 19