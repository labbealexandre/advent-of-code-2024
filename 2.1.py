def is_safe(D: list[int]):
    return all(
        list(
            map(
                lambda x: 1 <= x <= 3,
                D,
            )
        )
    ) or all(
        list(
            map(
                lambda x: -3 <= x <= -1,
                D,
            )
        )
    )


def resolve(data: str) -> int:
    R = [[int(n) for n in line.split()] for line in data.strip().split("\n")]

    return sum(
        list(
            map(
                lambda N: is_safe(
                    list(
                        map(
                            lambda i: N[i] - N[i + 1],
                            range(len(N) - 1),
                        )
                    )
                ),
                R,
            )
        )
    )


def main() -> None:
    with open("./input/2/test.txt") as file:
        data = file.read().strip()

    assert resolve(data) == 2

    with open("./input/2/input.txt") as file:
        data = file.read().strip()

    print(resolve(data))


if __name__ == "__main__":
    main()
