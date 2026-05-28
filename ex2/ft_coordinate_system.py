import math



def get_Player_pos() -> tuple[float, float, float]:
    while True:
        user_input: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        try:
            x_str, y_str, z_str = user_input.split(",")
            x: float = float(x_str)
            y: float = float(y_str)
            z: float = float(z_str)
            return(x,y,z)
        except ValueError as error:
            if "," not in user_input:
                print("Invalid syntax")
            else:
                print(f"Error on parameter: {error}")



def distance_from_center(pos: tuple[float, float, float]) -> float:
    x: float = pos[0]
    y: float = pos[1]
    z: float = pos[2]


    return math.sqrt(x ** 2 + y ** 2 + z ** 2)



def distance_between_points(
    first: tuple[float, float, float],
    second: tuple[float, float, float],
) -> float:
    x_diff: float = second[0] - first[0]
    y_diff: float = second[1] - first[1]
    z_diff: float = second[2] - first[2]


    return math.sqrt(x_diff ** 2 + y_diff ** 2 + z_diff ** 2)



def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get first set of coordinates")
    first_Pos: tuple[float, float,float] = get_Player_pos()

    print(f"Got a first tuple: {first_Pos}")
    print(
        f"It includes: X={first_Pos[0]},"
        f"Y={first_Pos[1]}",
        f"Z={first_Pos[2]}"
    )


    center_distance: float = distance_from_center(first_Pos)
    print(f"Distance to center: {round(center_distance, 4)}")


    print("Get a second set of coordinates")
    second_pos: tuple[float, float,float] = get_Player_pos()

    distance: float = distance_between_points(first_Pos, second_pos)
    print(
        "Distance between the sets of coordinates:"
        f"{round(distance, 4)}"
    )



if __name__ == "__main__":
    main()
