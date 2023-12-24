def str_to_int(a: list):
    return [int(n) for n in a]


def read_input_file(convert_to_int: bool = True):
    with open("assets/input6.txt") as file:
        time_line = " ".join(file.readline().split(":")[1].split()).split(" ")
        distance_line = " ".join(file.readline().split(":")[1].strip().split()).split(
            " "
        )

    if convert_to_int:
        time_line = str_to_int(time_line)
        distance_line = str_to_int(distance_line)
    return time_line, distance_line


def find_n_ways_to_solve(time: int, distance: int) -> int:
    n = 0
    for t in range(time + 1):
        speed = t  # [mm/ms]
        distance_traveled = speed * (time - t)  # [mm]
        if distance_traveled > distance:
            n += 1
    return n


def main(time_line: list, distance_line: list) -> int:
    result = 1
    for i in range(len(time_line)):
        result *= find_n_ways_to_solve(time_line[i], distance_line[i])
    return result


if __name__ == "__main__":
    time_line, distance_line = read_input_file()
    print(main(time_line, distance_line))

    time_line, distance_line = read_input_file(False)
    time = int("".join(time_line))
    distance = int("".join(distance_line))

    print(main([time], [distance]))
