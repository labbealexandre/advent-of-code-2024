def count(lines: list[str]) -> int:
    return sum(
        list(
            map(
                lambda y: sum(list(map(lambda x: x.count("XMAS"), y))),
                [
                    lines,
                    list(
                        map(
                            lambda x: "".join(reversed(x)),
                            lines,
                        )
                    ),
                ],
            )
        )
    )


def to_columns(lines: list[str]) -> str:
    return list(
        map(
            lambda x: "".join(x),
            list(
                zip(
                    *list(
                        map(
                            lambda x: list(x),
                            lines,
                        )
                    )
                )
            ),
        )
    )


def resolve(data: str) -> int:
    lines = data.split("\n")

    return count(
        lines
        + to_columns(lines)
        + to_columns(
            list(
                map(
                    lambda i: "_" * (len(lines) - i - 1) + lines[i] + "_" * i,
                    range(
                        len(lines),
                    ),
                )
            )
        )
        + to_columns(
            list(
                map(
                    lambda i: "_" * i + lines[i] + "_" * (len(lines) - i - 1),
                    range(
                        len(lines),
                    ),
                )
            )
        )
    )


def main() -> None:
    with open("./input/4/test.txt") as file:
        data = file.read().strip()

    assert resolve(data) == 18

    with open("./input/4/input.txt") as file:
        data = file.read().strip()

    print(resolve(data))


if __name__ == "__main__":
    main()
