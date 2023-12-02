from pathlib import Path
import pytest

import advent_of_code.aoc_2023.aoc_2023_01.aoc_2023_01 as aoc


@pytest.fixture
def example():
    data = (Path(__file__).parent / "example.txt").read_text().strip()
    return aoc.parse(data)

@pytest.fixture
def example2():
    data = (Path(__file__).parent / "example2.txt").read_text().strip()
    return aoc.parse(data)

def test_task1(example):
    assert aoc.task1(example) == 142


def test_task2(example2):
    assert aoc.task2(example2) == 281