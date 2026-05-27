import sys



def print_usage() -> None:
    print(
        "No scores provided. Usage: "
        "python3 ft_score_analytics.py <score1> <score2> ..."
    )

    
def get_scores(args: list[str]) -> list[int]:
    scores: list[int] = []

    for arg in args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores
    

def print_analytics(scores: list[int]) -> None:
    total: int = sum(scores)
    average: float = total / len(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score Range: {max(scores) - min(scores)}")



def main() -> None:
    print("=== Player Score Analytics ===")

    scores: list[int] = get_scores(sys.argv[1:])

    if len(scores) == 0:
        print_usage()
        return
    
    print_analytics(scores)

if __name__ == "__main__":
    main()