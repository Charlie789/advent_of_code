from pathlib import Path
from collections import namedtuple
from typing import List
from copy import deepcopy


class DynamicAccessNestedDict:
    """Dynamically get/set nested dictionary keys of 'data' dict"""

    def __init__(self, data: dict):
        self.data = data

    def getval(self, keys: List):
        data = self.data
        for k in keys:
            data = data[k]
        return data

    def setval(self, keys: List, val) -> None:
        data = self.data
        lastkey = keys[-1]
        for k in keys[:-1]:
            data = data[k]
        data[lastkey] = val


cd_command = namedtuple("cd_command", "dir")
ls_command = namedtuple("ls_command", "")
file_entry = namedtuple("file_entry", "size file_name")
dir_entry = namedtuple("dir_entry", "dir_name")


def parse(raw_input):
    parsed_input = []
    for line in raw_input.splitlines():
        words = line.split(" ")
        if words[0] == "$":
            if words[1] == "ls":
                parsed_input.append(ls_command())
            else:
                parsed_input.append(cd_command(words[-1]))
        elif words[0] == "dir":
            parsed_input.append(dir_entry(words[-1]))
        else:
            parsed_input.append(file_entry(words[0], words[-1]))

    parsed_input.reverse()
    return parsed_input


omg = 0


def task1(parsed_input):
    def get_sum(d):
        global omg
        current_dir_sum = 0
        for k, v in d.items():
            if isinstance(v, dict):
                current_dir_sum += get_sum(v)
            else:
                sub_sum = sum([int(x.size) for x in set(v)])
                current_dir_sum += sub_sum
        if current_dir_sum < 100000:
            omg += current_dir_sum

        return current_dir_sum

    structure = DynamicAccessNestedDict({})
    current_dir = ""
    while parsed_input:
        entry = parsed_input.pop()
        if isinstance(entry, cd_command):
            if entry.dir == "/":
                current_dir = "root_dir"
            elif entry.dir == "..":
                temp_dir = current_dir.split("/")
                current_dir = "/".join(temp_dir[:-1])
            else:
                current_dir += f"/{entry.dir}"
        elif isinstance(entry, ls_command):
            pass
        elif isinstance(entry, dir_entry):
            path = current_dir.split("/")
            try:
                structure.getval(path)
            except KeyError:
                structure.setval(path, {"files": []})
        elif isinstance(entry, file_entry):
            path = current_dir.split("/")
            try:
                structure.getval(path)
            except KeyError:
                structure.setval(path, {"files": []})
            path.extend(["files"])
            files = structure.getval(path)
            files.append(entry)
            structure.setval(path, files)

    get_sum(structure.data["root_dir"])

    return omg


def task2(parsed_input):
    sizes = []

    def get_sum(d):
        current_dir_sum = 0
        for k, v in d.items():
            if isinstance(v, dict):
                current_dir_sum += get_sum(v)
            else:
                sub_sum = sum([int(x.size) for x in set(v)])
                current_dir_sum += sub_sum
        sizes.append(current_dir_sum)

        return current_dir_sum

    structure = DynamicAccessNestedDict({})
    current_dir = ""
    while parsed_input:
        entry = parsed_input.pop()
        if isinstance(entry, cd_command):
            if entry.dir == "/":
                current_dir = "root_dir"
            elif entry.dir == "..":
                temp_dir = current_dir.split("/")
                current_dir = "/".join(temp_dir[:-1])
            else:
                current_dir += f"/{entry.dir}"
        elif isinstance(entry, ls_command):
            pass
        elif isinstance(entry, dir_entry):
            path = current_dir.split("/")
            try:
                structure.getval(path)
            except KeyError:
                structure.setval(path, {"files": []})
        elif isinstance(entry, file_entry):
            path = current_dir.split("/")
            try:
                structure.getval(path)
            except KeyError:
                structure.setval(path, {"files": []})
            path.extend(["files"])
            files = structure.getval(path)
            files.append(entry)
            structure.setval(path, files)

    get_sum(structure.data["root_dir"])

    available_space = 70000000 - max(sizes)
    needed_space = 30000000 - available_space
    minimal_size_to_remove = min(filter(lambda size: size >= needed_space, sizes))

    return minimal_size_to_remove


if __name__ == "__main__":
    data = (Path(__file__).parent / "input.txt").read_text().strip()
    parsed_data = parse(data)
    solution1 = task1(deepcopy(parsed_data))
    solution2 = task2(parsed_data)
    print(f"Solution 1: {solution1}\nSolution 2: {solution2}")
