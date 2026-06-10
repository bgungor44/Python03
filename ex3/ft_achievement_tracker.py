import random



def gen_player_achievements() -> set[str]:
    all_achievements: list[str] = [
        "First Steps",
        "Boss Slayer",
        "Treasure Hunter",
        "Speed Runner",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "World Savior",
        "Crafting Genius",
        "Strategist",
        "Survivor",
        "Sharp Mind",
        "Hidden Path Finder",
    ]

    count: int = random.randint(4, 8)
    return set(random.sample(all_achievements, count))


def print_player_achievements(players: dict[str, set[str]]) -> None:
    for name in players:
        print(f"Player {name}: {players[name]}")


def get_all_achievements(players: dict[str, set[str]]) -> set[str]:
    all_achievements: set[str] = set()

    for name in players:
        all_achievements = all_achievements.union(players[name])
    return all_achievements


def get_common_achievemenets(players: dict[str, set[str]]) -> set[str]:
    first: bool = True
    common: set[str] = players[name]

    for name in players:
        if first:
            common = players[name]
            first = False
        else:
            common = common.intersection(players[name])
    return common


def print_unique_achievements(players: dict[str, set[str]]) -> None:
    for name in players:
        others: set[str] = set()
        for other_name in players:
            if other_name != name:
                others = others.union(players[other_name])
        print(f"Only {name} has: {players[name].difference(others)}")# A.difference(b) = a da olanlardan b de olanları çıkar.


def print_missing_achievements(
    players: dict[str, set[str]],
    all_achievements: set[str],
) -> None:
    for name in players:
        missing: set[str] = all_achievements.difference(players[name])
        print(f"{name} is missing: {missing}")



def main() -> None:
    print("=== Achievement Tracker System ===")


    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    print_player_achievements(players)

    print()

    all_achievements: set[str] = get_all_achievements(players)
    common_achievements: set[str] = get_common_achievemenets(players)

    print(f"All distinct achievements: {all_achievements}")

    print()

    print(f"Common achievements: {common_achievements}")

    print()

    print_unique_achievements(players)
    print()
    print_missing_achievements(players, all_achievements)


if __name__ == "__main__":
    main()