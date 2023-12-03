def read_input_file():
    with open("assets/input1.txt", "r") as f:
        return f.readlines()


def get_calibration_value(inp: str) -> int:
    calibration_value = []
    for l in inp:
        if l.isdigit() and len(calibration_value) < 2:
            calibration_value.append(l)
        elif l.isdigit():
            calibration_value[-1] = l
    if len(calibration_value) == 1:
        calibration_value.append(calibration_value[0])
    return int("".join(calibration_value))


def get_calibration_values(inps: list) -> list:
    return [get_calibration_value(inp) for inp in inps]


if __name__ == "__main__":
    input = read_input_file()
    calibrations_values = get_calibration_values(input)
    print(f"{sum(calibrations_values)=}")


"""
challange : do this task in one line of programming
"""
