import re


def resolve(data: str) -> int:
    return sum(
        list(
            map(
                lambda x: int(x[0]) * int(x[1]),
                re.findall(
                    r"mul\((\d+),(\d+)\)",
                    data,
                ),
            )
        )
    )


def main() -> None:
    with open("./input/3.1/test.txt") as file:
        data = file.read().strip()

    assert resolve(data) == 161

    with open("./input/3.1/input.txt") as file:
        data = file.read().strip()

    print(resolve(data))


if __name__ == "__main__":
    main()
