CUBES_CONFIG = {"red": 12, "green": 13, "blue": 14}


def read_input_file():
    with open("assets/input2.txt", "r") as f:
        return f.readlines()


def get_id_and_sets(inp: str) -> tuple:
    first_half, second_half = inp.split(": ")
    return int(first_half.split(" ")[1]), second_half


def is_possible_game(sets: str) -> bool:
    subsets = sets.split("; ")
    for subset in subsets:
        subset_config = subset.split(", ")
        for c in subset_config:
            n, color = c.split(" ")
            if int(n) > CUBES_CONFIG[color]:
                return False
    return True


def get_possibles_games(inps: list) -> list:
    id_possibles_games = []
    for game in inps:
        id_game, sets = get_id_and_sets(game.split("\n")[0])
        if is_possible_game(sets):
            id_possibles_games.append(id_game)
    return id_possibles_games


def get_fewest_number_cubes(inps: list) -> list:
    fewest_number_cubes = []
    for game in inps:
        min_current_game_config = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        _, sets = get_id_and_sets(game.split("\n")[0])
        subsets = sets.split("; ")
        for subset in subsets:
            subset_config = subset.split(", ")
            for c in subset_config:
                n, color = c.split(" ")
                if int(n) > min_current_game_config[color]:
                    min_current_game_config[color] = int(n)
        fewest_number_cubes.append(min_current_game_config)
    return fewest_number_cubes


def get_powers(number_cubes_games: list):
    return [
        cubes["red"] * cubes["green"] * cubes["blue"] for cubes in number_cubes_games
    ]


if __name__ == "__main__":
    inps = read_input_file()

    # part 1
    id_possibles_games = get_possibles_games(inps)
    print(f"The sum of the possible games is: {sum(id_possibles_games)}")

    # part 2
    fewest_number_cubes = get_fewest_number_cubes(inps)
    powers = get_powers(fewest_number_cubes)
    print(f"The sum of the powers is: {sum(powers)}")
