def main():
    calorie_inputs = open("input.txt", "r")

    print(find_max_calories(calorie_inputs, 1))
    print(find_max_calories(calorie_inputs, 3))


def find_max_calories(calorie_inputs, no_elves):
    calorie_inputs.seek(0)

    max_calories = [0]*no_elves
    calories = 0

    for calorie_input in calorie_inputs:
        if calorie_input == "\n":
            if calories > min(max_calories):
                max_calories = max_calories[:no_elves-1] + [calories]
                max_calories.sort(reverse=True)
            calories = 0
        else:
            calories = calories + int(calorie_input)

    return sum(max_calories)


if __name__ == "__main__":
    main()
