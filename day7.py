import bisect

CARDS_STREGTH = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
}


def read_input_file():
    with open("assets/input7.txt") as file:
        hands = {}
        for line in file:
            hand, bid = line.split(" ")
            hands[hand] = int(bid)
    return hands


def initialize_hand() -> dict:
    return {
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "T": 0,
        "J": 0,
        "Q": 0,
        "K": 0,
        "A": 0,
    }


def classify_hand(hand: str, joker_option: bool = False) -> str:
    placeholder = initialize_hand()
    for card in hand:
        placeholder[card] += 1
    if joker_option:
        n_j_cards = placeholder["J"]
        del placeholder["J"]
        most_rep_card = max(placeholder, key=placeholder.get)
        placeholder[most_rep_card] += n_j_cards

    if 5 in placeholder.values():
        return "five_kind"
    elif 4 in placeholder.values():
        return "four_kind"
    elif 3 in placeholder.values() and 2 in placeholder.values():
        return "full_house"
    elif 3 in placeholder.values():
        return "three_kind"
    elif list(placeholder.values()).count(2) == 2:
        return "two_pair"
    elif 2 in placeholder.values():
        return "one_pair"
    else:
        return "high_card"


def get_insert_pos(hands: list[tuple], chand: str, joker_option: bool = False) -> int:
    cards_stregth = CARDS_STREGTH.copy()
    if joker_option:
        cards_stregth["J"] = 0

    if not hands:
        return 0
    else:
        for pos, (hand, _) in enumerate(hands):
            for c, cc in zip(hand, chand):
                if cards_stregth[c] > cards_stregth[cc]:
                    return pos
                elif cards_stregth[c] < cards_stregth[cc]:
                    break
        return len(hands)


def main(hands_bid: dict, joker_option: bool = False) -> int:
    hands_types = {
        "high_card": [],
        "one_pair": [],
        "two_pair": [],
        "three_kind": [],
        "full_house": [],
        "four_kind": [],
        "five_kind": [],
    }
    for hand, bid in hands_bid.items():
        hand_type = classify_hand(hand, joker_option)
        pos = get_insert_pos(hands_types[hand_type], hand, joker_option)
        hands_types[hand_type].insert(pos, (hand, bid))

    rank = 1
    result = 0
    for _, hands in hands_types.items():
        for _, bid in hands:
            result += bid * rank
            rank += 1
    return result


if __name__ == "__main__":
    hands_bid = read_input_file()
    print(main(hands_bid))

    # part 2
    print(main(hands_bid, True))
