import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players: list[str] = ["alice", "bob", "charlie", "dylan"]
    actions: list[str] = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "use",
        "release",
    ]

    while True:
        name: str = random.choice(players)
        action: str = random.choice(actions)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index: int = random.randrange(len(events))
        event: tuple[str, str] = events[index]
        del events[event]
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator: typing.Generator[tuple[str, str], None, None]
    event_generator = gen_event()

    for i in range(1000):
        event: tuple[str, str] = next(event_generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    events: list[tuple[str, str]] = []

    for _ in range(10):
        event = next(event_generator)
        events += [event]

    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()