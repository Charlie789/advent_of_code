from pathlib import Path
import pytest

import advent_of_code.aoc_2022.aoc_2022_10.aoc_2022_10 as aoc


@pytest.fixture
def example():
    data = (Path(__file__).parent / "example.txt").read_text().strip()
    return aoc.parse(data)


def test_task1(example):
    assert aoc.task1(example) == 13140

#
# @pytest.mark.skip
def test_task2(example):
    assert aoc.task2(example) == 1
