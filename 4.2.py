def is_xmas(
    lines: list[int],
    i: int,
    j: int,
) -> bool:
    return lines[i + 1][j + 1] == "A" and "".join(
        [
            lines[i][j],
            lines[i][j + 2],
            lines[i + 2][j + 2],
            lines[i + 2][j],
        ]
    ) in ["MSSM", "MMSS", "SMMS", "SSMM"]


def count(
    lines: list[int],
    height: int,
    width: int,
) -> int:
    return sum(
        list(
            map(
                lambda i: is_xmas(
                    lines,
                    i // width,
                    i % width,
                ),
                range(height * width),
            ),
        )
    )


def resolve(data: str) -> int:
    lines = data.split("\n")

    return count(
        lines,
        len(lines) - 2,
        len(lines[0]) - 2,
    )


def main() -> None:
    with open("./input/4/test.txt") as file:
        data = file.read().strip()

    assert resolve(data) == 9

    with open("./input/4/input.txt") as file:
        data = file.read().strip()

    print(resolve(data))


if __name__ == "__main__":
    main()
