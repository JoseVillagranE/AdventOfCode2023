import numpy as np

# destination source range


def read_input_file():
    seeds = []
    maps = {
        "seed_to_soil_map": [],
        "soil_to_fertilizer_map": [],
        "fertilizer_to_water_map": [],
        "water_to_light_map": [],
        "light_to_temperature_map": [],
        "temperature_to_humidity_map": [],
        "humidity_to_location_map": [],
    }
    cmap = "seed_to_soil_map"
    with open("assets/input5.txt") as file:
        for line in file:
            if line.startswith("seeds"):
                seeds = [int(x) for x in line.rstrip().split(": ")[1].split(" ")]
            elif line.startswith("seed-to-soil map"):
                cmap = "seed_to_soil_map"
            elif line.startswith("soil-to-fertilizer map"):
                cmap = "soil_to_fertilizer_map"
            elif line.startswith("fertilizer-to-water map"):
                cmap = "fertilizer_to_water_map"
            elif line.startswith("water-to-light map"):
                cmap = "water_to_light_map"
            elif line.startswith("light-to-temperature map"):
                cmap = "light_to_temperature_map"
            elif line.startswith("temperature-to-humidity map"):
                cmap = "temperature_to_humidity_map"
            elif line.startswith("humidity-to-location map"):
                cmap = "humidity_to_location_map"
            elif line != "\n":
                maps[cmap].append([int(x) for x in line.rstrip().split(" ")])

    return (seeds, maps)


def main(seeds: list, maps: dict) -> int:
    for i in range(len(seeds)):
        for k, m in maps.items():
            for r in m:
                if seeds[i] >= r[1] and seeds[i] <= r[1] + r[2] - 1:
                    seeds[i] = r[0] + (seeds[i] - r[1])
                    break
    return min(seeds)


def local_minima_serach(
    seed_high: int, seed_low: int, location_high: int, location_low: int, maps: dict
) -> int:
    mid = seed_low + (seed_high - seed_low) // 2

    if mid == seed_low:
        print(f"{location_low=}")
        return location_low

    mid_location = seed_to_location(mid, maps)
    mid_location_m1 = seed_to_location(mid - 1, maps)
    mid_location_p1 = seed_to_location(mid + 1, maps)

    if mid_location > mid_location_m1:
        return local_minima_serach(
            mid - 1, seed_low, mid_location_m1, location_low, maps
        )

    return local_minima_serach(seed_high, mid + 1, location_high, mid_location_p1, maps)


def iterative_local_minima_serach(seed_high: int, seed_low: int, maps: dict) -> int:
    while True:
        mid = seed_low + (seed_high - seed_low) // 2
        mid_location = seed_to_location(mid, maps)
        mid_location_m1 = seed_to_location(mid - 1, maps)
        mid_location_p1 = seed_to_location(mid + 1, maps)

        if mid_location > mid_location_m1:
            seed_high = mid - 1
        elif mid_location > mid_location_p1:
            seed_low = mid + 1
        else:
            return mid_location


def seed_to_location(seed: int, maps: dict) -> int:
    location = 0
    for _, m in maps.items():
        for r in m:
            if seed >= r[1] and seed <= r[1] + r[2] - 1:
                location = r[0] + (seed - r[1])
                break
    return location if location > 0 else seed


def main2(seeds: list, maps: dict) -> int:
    i = 0
    min_location = np.inf
    while i < len(seeds):
        print(i)
        low_seed = seeds[i]
        high_seed = seeds[i + 1]
        low_location = seed_to_location(low_seed, maps)
        high_location = seed_to_location(high_seed, maps)
        if low_location < high_location:
            min_location = min(
                min_location,
                iterative_local_minima_serach(high_seed, low_seed, maps),
            )
        else:
            min_location = min(
                min_location,
                iterative_local_minima_serach(low_seed, high_seed, maps),
            )
        i += 2
    return min_location


if __name__ == "__main__":
    seeds, maps = read_input_file()
    print(main2(seeds, maps))
