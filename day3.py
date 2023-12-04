from functools import reduce


def read_input_file():
    with open("assets/input3.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines


def get_part_number(cline: str, pline: str, nline: str) -> tuple:
    is_part_number = False
    number = ""
    i = 0
    if not cline[0].isdigit():
        if pline:
            if not pline[0].isdigit() and pline[0] != ".":
                is_part_number = True
        if nline:
            if not nline[0].isdigit() and nline[0] != ".":
                is_part_number = True
        if cline[0] != ".":
            is_part_number = True

        i += 1

    while i < len(cline) and cline[i].isdigit():
        if pline:
            if not pline[i].isdigit() and pline[i] != ".":
                is_part_number = True
        if nline:
            if not nline[i].isdigit() and nline[i] != ".":
                is_part_number = True
        number += cline[i]
        i += 1

    if i < len(cline):
        if not cline[i].isdigit() and cline[i] != ".":
            is_part_number = True
        if pline:
            if not pline[i].isdigit() and pline[i] != ".":
                is_part_number = True
        if nline:
            if not nline[i].isdigit() and nline[i] != ".":
                is_part_number = True
    return int(number) if is_part_number else -1, i


def main(lines: list) -> int:
    i = j = 0
    total_sum = 0

    while i < len(lines):
        j = 0
        while j < len(lines[i]):
            if lines[i][j].isdigit():
                start_idx = j - 1 if j else 0
                past_line = [] if i == 0 else lines[i - 1][start_idx:]
                next_line = [] if i == len(lines) - 1 else lines[i + 1][start_idx:]
                number, delta_j = get_part_number(
                    lines[i][start_idx:], past_line, next_line
                )
                if number != -1:
                    total_sum += number

                j += delta_j
            else:
                j += 1
        i += 1

    return total_sum


def get_gear_number(cline: str, pline: str, nline: str) -> tuple:
    is_gear_number = False
    number = ""
    i = 0
    rel_coord = (-1, -1)
    temp_x = 0
    if not cline[0].isdigit():
        if pline:
            if pline[0] == "*":
                is_gear_number = True
                rel_coord = (0, -1)
        if nline:
            if nline[0] == "*":
                is_gear_number = True
                rel_coord = (0, 1)
        if cline[0] == "*":
            is_gear_number = True
            rel_coord = (0, 0)

        i += 1
        temp_x += 1

    while i < len(cline) and cline[i].isdigit():
        if pline:
            if pline[i] == "*":
                is_gear_number = True
                rel_coord = (i, -1)
        if nline:
            if nline[i] == "*":
                is_gear_number = True
                rel_coord = (i, 1)
        number += cline[i]
        i += 1

    if i < len(cline):
        if cline[i] == "*":
            is_gear_number = True
            rel_coord = (i, 0)
        if pline:
            if pline[i] == "*":
                is_gear_number = True
                rel_coord = (i, -1)
        if nline:
            if nline[i] == "*":
                is_gear_number = True
                rel_coord = (i, 1)
    return (
        int(number) if is_gear_number else -1,
        i,
        (rel_coord[0] - temp_x, rel_coord[1]),
    )


def get_total_sum_gear_ratios(lines: list) -> int:
    i = j = 0
    gears = []
    total_sum = 0

    while i < len(lines):
        j = 0
        while j < len(lines[i]):
            if lines[i][j].isdigit():
                start_idx = j - 1 if j else 0
                past_line = [] if i == 0 else lines[i - 1][start_idx:]
                next_line = [] if i == len(lines) - 1 else lines[i + 1][start_idx:]
                number, delta_j, rel_coord = get_gear_number(
                    lines[i][start_idx:], past_line, next_line
                )
                if number != -1:
                    is_agg = False
                    for g in gears:
                        if g["coord"] == (j + rel_coord[0], i + rel_coord[1]):
                            g["numbers"].append(number)
                            is_agg = True
                            break
                    if not is_agg:
                        gears.append(
                            {
                                "numbers": [number],
                                "coord": (j + rel_coord[0], i + rel_coord[1]),
                            }
                        )
                j += delta_j
            else:
                j += 1
        elemments_to_remove = []
        for idx, g in enumerate(gears):
            if i == len(lines) - 1:
                if len(g["numbers"]) == 2:
                    total_sum += reduce(lambda x, y: x * y, g["numbers"])
            elif (i - g["coord"][1]) > 0:
                if len(g["numbers"]) == 2:
                    total_sum += reduce(lambda x, y: x * y, g["numbers"])
                elemments_to_remove.append(idx)
        for idx in sorted(elemments_to_remove, reverse=True):
            gears.pop(idx)
        i += 1
    return total_sum


if __name__ == "__main__":
    lines = read_input_file()

    # part 1
    total_sum = main(lines.copy())
    print(f"{total_sum=}")

    # part 2
    total_sum = get_total_sum_gear_ratios(lines)
    print(f"{total_sum=}")
