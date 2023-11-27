import math


def main():
    fuel_requirements = open("input.txt")

    total_fuel_requirement = 0
    for fuel_requirement in fuel_requirements:
        total_fuel_requirement = total_fuel_requirement + convert_snafu_2_decimal(fuel_requirement[:-1])

    print(convert_decimal_2_snafu(total_fuel_requirement))


def convert_decimal_2_snafu(decimal):
    snafu = []
    while decimal > 0:
        if decimal % 5 > 2:
            snafu.append(str(decimal-(math.floor(decimal // 5) + 1) * 5))
            decimal = math.floor(decimal // 5) + 1
        else:
            snafu.append(str(decimal % 5))
            decimal = math.floor(decimal // 5)

    snafu = [digit.replace("-1", "-") for digit in snafu]
    snafu = [digit.replace("-2", "=") for digit in snafu][::-1]

    return "".join(snafu)


def convert_snafu_2_decimal(snafu):
    digits = [str(x) for x in str(snafu)]
    digits = [digit.replace("-", "-1") for digit in digits]
    digits = [digit.replace("=", "-2") for digit in digits][::-1]

    position = 0
    decimal = 0

    for digit in digits:
        decimal = decimal + int(digit) * (5**position)
        position = position + 1

    return decimal


if __name__ == "__main__":
    main()
