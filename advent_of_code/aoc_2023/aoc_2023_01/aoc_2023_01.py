from pathlib import Path
from string import ascii_lowercase

word_to_digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def parse(raw_input):
    parsed_input = raw_input.split("\n")
    return parsed_input


def task1(parsed_input):
    def find_first_last_number(line_):
        new_line = line_.strip(ascii_lowercase)
        digits = int(f'{new_line[0]}{new_line[-1]}')
        return digits

    sum = 0
    for line in parsed_input:
        sum += find_first_last_number(line)

    return sum

def task2(parsed_input):
    sum_ = 0
    for line in parsed_input:
        parsed_line = ""
        char_index = 0
        while char_index < len(line):
            if line[char_index].isdigit():
                parsed_line += line[char_index]
            else:
                for digit in word_to_digit_map:
                    if line.startswith(digit, char_index):
                        parsed_line += word_to_digit_map[digit]
                        break
            char_index += 1
        digits = int(f'{parsed_line[0]}{parsed_line[-1]}')
        sum_ += digits
    return sum_


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().strip()
    parsed_data = parse(data)
    solution1 = task1(parsed_data)
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
