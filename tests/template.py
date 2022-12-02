from pathlib import Path
import pytest

import advent_of_code.template as aoc


@pytest.fixture
def example():
    data = (Path(__file__).parent / "example.txt").read_text().strip()
    return aoc.parse(data)

@pytest.mark.skip
def test_task1(example):
    assert aoc.task1(example) == ...

@pytest.mark.skip
def test_task2(example):
    assert aoc.task2(example) == ...