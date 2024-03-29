from pathlib import Path


def parse(raw_input):
    parsed_input = []
    for line in raw_input.splitlines():
        all_numbers = line.split(":")[1]
        winning_unparsed, my_numbers_unprased = all_numbers.split("|")
        winning = set(winning_unparsed.split())
        my_numbers = set(my_numbers_unprased.split())
        parsed_input.append((winning, my_numbers))

    return parsed_input


def task1(parsed_input):
    total_points = 0
    for winning, my_numbers in parsed_input:
        win_numbers_quantity = len(winning.intersection(my_numbers))
        if win_numbers_quantity == 0:
            continue
        points = 2 ** (win_numbers_quantity - 1)
        total_points += points
    return total_points


def task2(parsed_input):
    sum_ = 0
    def _handle_card(_card_id):
        nonlocal sum_
        sum_ += 1
        for i in range(1, number_of_wins_per_card[_card_id] + 1):
            _handle_card(_card_id + i)

    number_of_wins_per_card = [len(winning.intersection(my_numbers)) for winning, my_numbers in parsed_input]
    for card_id in range(len(number_of_wins_per_card)):
        _handle_card(card_id)
    return sum_

if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().strip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
