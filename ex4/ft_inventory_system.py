import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts: list[str] = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item: str = parts[0]
        quantity_text: str = parts[1]

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity: int = int(quantity_text)
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")
            continue

        inventory[item] = quantity

    return inventory


def display_inventory_stats(inventory: dict[str, int]) -> None:
    items: list[str] = list(inventory.keys())
    quantities: list[int] = list(inventory.values())
    total: int = sum(quantities)

    if len(items) == 0:
        print("Got inventory: {}")
        return

    print(f"Got inventory: {inventory}")
    print(f"Item list: {items}")
    print(f"Total quantity of the {len(items)} items: {total}")

    for item in inventory:
        percent: float = round((inventory[item] / total) * 100, 1)
        print(f"Item {item} represents {percent}%")

    most_item: str = items[0]
    least_item: str = items[0]

    for item in inventory:
        if inventory[item] > inventory[most_item]:
            most_item = item
        if inventory[item] < inventory[least_item]:
            least_item = item

    print(
        f"Item most abundant: {most_item} "
        f"with quantity {inventory[most_item]}"
    )
    print(
        f"Item least abundant: {least_item} "
        f"with quantity {inventory[least_item]}"
    )


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = parse_inventory(sys.argv[1:])


    if inventory != {}:
        display_inventory_stats(inventory)
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")
    else:
        print(f"Each parameter must follow this format:")
        print(
            f"python3 ft_inventory_system.py <item_name>:<quantity>",
            f"<item_name2>:<quantity>"
            )


if __name__ == "__main__":
    main()