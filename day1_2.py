SPELLED_NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def read_input_file():
    with open("assets/input1.txt", "r") as f:
        return f.readlines()


def is_str_an_number(str_pn: str, sn: dict) -> tuple:
    new_sn = {}
    for spell_number, number in sn.items():
        if str_pn == spell_number:
            return True, new_sn
        elif spell_number.startswith(str_pn):
            new_sn[spell_number] = number
    return False, new_sn


def remaining_str_pn(str_pn: str) -> str:
    while len(str_pn) > 1:
        for spell_number, _ in SPELLED_NUMBERS.items():
            if spell_number.startswith(str_pn):
                return str_pn
        str_pn = str_pn[1:]
    return str_pn


def get_calibration_value(inp: str) -> int:
    sn = SPELLED_NUMBERS.copy()
    str_pn = ""
    calibration_value = []
    for l in inp:
        str_pn += l
        out, new_sn = is_str_an_number(str_pn, sn)
        if out:
            number = SPELLED_NUMBERS[str_pn]
            l = str(number)
            str_pn = str_pn[-1]
            sn = SPELLED_NUMBERS.copy()
        else:
            if not new_sn:
                if len(str_pn) > 2:
                    str_pn = remaining_str_pn(str_pn[1:])
                else:
                    str_pn = str_pn[-1]
                sn = SPELLED_NUMBERS.copy()
            else:
                sn = new_sn

        if l.isdigit() and len(calibration_value) < 2:
            calibration_value.append(l)
        elif l.isdigit():
            calibration_value[-1] = l
    if len(calibration_value) == 1:
        calibration_value.append(calibration_value[0])
    return int("".join(calibration_value))


def get_calibration_values(inps: list) -> list:
    return [get_calibration_value(inp.split("\n")[0]) for inp in inps]


if __name__ == "__main__":
    input = read_input_file()
    calibration_values = get_calibration_values(input)
    print(f"{sum(calibration_values)=}")
