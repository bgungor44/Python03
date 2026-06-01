import random



def main() -> None:
    print("=== Game Data Alchemist ===")

    players: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]


    capitalized_players: list[str] = [name.capitalize() for name in players]
    already_capitalized: list[str] = [
        name for name in players if name[0].isupper()
    ]


    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized_players}")
    print(f"New list of capitalized names only: {already_capitalized}")


    scores: dict[str, int] = {
        name: random.randint(0, 1000) for name in capitalized_players
    }

    average: float = round(sum(scores.values()) / len(scores), 2)

    high_scores: dict[str, int] = {
        name: score for name, score in scores.items() if score > average
    }

    print(f"Score dict: {scores}")
    print(f"Score average is {average}")
    print(f"High scores: {high_scores}")

if __name__ == "__main__":
    main()