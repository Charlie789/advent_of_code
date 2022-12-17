from pathlib import Path
import pytest

import advent_of_code.aoc_2022.aoc_2022_14.aoc_2022_14 as aoc


@pytest.fixture
def example():
    data = (Path(__file__).parent / "example.txt").read_text().rstrip()
    return aoc.parse(data)

@pytest.fixture
def example2():
    data = (Path(__file__).parent / "example.txt").read_text().rstrip()
    return aoc.parse2(data)


def test_task1(example):
    assert aoc.task1(example) == 24


def test_task2(example2):
    assert aoc.task2(example2) == 93
