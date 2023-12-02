def main():
    cube_outcomes = open("input.txt")
    print(calculate_total_possible_games(cube_outcomes))
    print(calculate_minimum_possible_games(cube_outcomes))


def calculate_total_possible_games(cube_outcomes):
    cube_outcomes.seek(0)
    no_cubes = {"red": 12, "green": 13, "blue": 14}
    total_game_ids = 0

    for cube_outcome in cube_outcomes:
        possible = True
        game_id, game_outcomes = cube_outcome.split(":")
        game_outcomes = game_outcomes.split(";")
        for game_outcome in game_outcomes:
            for color_cubes in  game_outcome.split(","):
                number = int("".join(filter(str.isdigit, color_cubes.strip())))
                color = "".join(filter(str.isalpha, color_cubes.strip()))
                possible = False if no_cubes[color] < number else possible
        total_game_ids = total_game_ids + int("".join(filter(str.isdigit, game_id))) if possible else total_game_ids

    return total_game_ids


def calculate_minimum_possible_games(cube_outcomes):
    cube_outcomes.seek(0)
    total_power = 0

    for cube_outcome in cube_outcomes:
        min_colors = {"red": 0, "green": 0, "blue": 0}
        game_outcomes = cube_outcome.split(":")[1].split(";")
        for game_outcome in game_outcomes:
            for color_cubes in game_outcome.split(","):
                number = int("".join(filter(str.isdigit, color_cubes.strip())))
                color = "".join(filter(str.isalpha, color_cubes.strip()))
                min_colors[color] = number if min_colors[color] < number else min_colors[color]
        total_power = total_power + min_colors["red"] * min_colors["green"] * min_colors["blue"]

    return total_power


if __name__ == "__main__":
    main()
