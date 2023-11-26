def main():
    rps_inputs = open("input.txt")
    print(calculate_rps_score_1(rps_inputs))
    print(calculate_rps_score_2(rps_inputs))


def calculate_rps_score_1(rps_inputs):
    outcome_dict = {"A": ["Z", "X", "Y"],
                    "B": ["X", "Y", "Z"],
                    "C": ["Y", "Z", "X"]}
    shape_scores = ["X", "Y", "Z"]

    rps_inputs.seek(0)
    total_score = 0
    for rps_input in rps_inputs:
        outcome_score = outcome_dict[rps_input[0]].index(rps_input[2]) * 3
        shape_score = shape_scores.index(rps_input[2]) + 1
        total_score = total_score + shape_score + outcome_score
    return total_score


def calculate_rps_score_2(rps_inputs):
    outcome_scores = ["X", "Y", "Z"]
    shape_scores = {"A": ["Y", "Z", "X"],
                    "B": ["X", "Y", "Z"],
                    "C": ["Z", "X", "Y"]}
    rps_inputs.seek(0)
    total_score = 0
    for rps_input in rps_inputs:
        outcome_score = outcome_scores.index(rps_input[2]) * 3
        shape_score = shape_scores[rps_input[0]].index(rps_input[2]) + 1
        total_score = total_score + shape_score + outcome_score
    return total_score


if __name__ == "__main__":
    main()
