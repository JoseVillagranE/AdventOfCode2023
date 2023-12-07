def read_input_file():
    with open("assets/input4.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines


def get_points(a):
    if not a:
        return 0
    else:
        return 2 ** (a - 1)


def main(cards: list) -> int:
    total_points = 0
    for card in cards:
        winning_numbers, numbers = card.replace("  ", " ").split(": ")[1].split(" | ")
        winning_numbers = sorted([int(n) for n in winning_numbers.split(" ")])
        numbers = sorted([int(n) for n in numbers.split(" ")])
        i = j = 0
        n_matches = 0
        while i < len(numbers) and j < len(winning_numbers):
            if winning_numbers[j] == numbers[i]:
                n_matches += 1
                j += 1
                i += 1
            elif winning_numbers[j] > numbers[i]:
                i += 1
            else:
                j += 1
        total_points += get_points(n_matches)
    return total_points


def main2(cards: list) -> int:
    copies = {k: 1 for k in range(len(cards))}
    for card_index, card in enumerate(cards):
        winning_numbers, numbers = card.replace("  ", " ").split(": ")[1].split(" | ")
        winning_numbers = sorted([int(n) for n in winning_numbers.split(" ")])
        numbers = sorted([int(n) for n in numbers.split(" ")])
        i = j = 0
        n_matches = 0
        while i < len(numbers) and j < len(winning_numbers):
            if winning_numbers[j] == numbers[i]:
                n_matches += 1
                j += 1
                i += 1
            elif winning_numbers[j] > numbers[i]:
                i += 1
            else:
                j += 1
        for _ in range(copies[card_index]):
            for n in range(n_matches):
                copies[n + card_index + 1] += 1
    return sum(copies.values())


if __name__ == "__main__":
    cards = read_input_file()
    print(main2(cards))
