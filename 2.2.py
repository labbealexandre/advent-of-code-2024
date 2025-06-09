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


def loose_safe(N: list[int]):
    return any(
        list(
            map(
                lambda M: is_safe(
                    list(
                        map(
                            lambda i: M[i] - M[i + 1],
                            range(len(M) - 1),
                        )
                    )
                ),
                list(
                    map(
                        lambda i: N[:i] + N[i + 1 :],
                        range(len(N)),
                    )
                ),
            )
        )
    )


def resolve(data: str) -> int:
    R = [[int(n) for n in line.split()] for line in data.strip().split("\n")]

    return sum((list(map(lambda N: loose_safe(N), R))))


def main() -> None:
    with open("./input/2/test.txt") as file:
        data = file.read().strip()

    assert resolve(data) == 4

    with open("./input/2/input.txt") as file:
        data = file.read().strip()

    print(resolve(data))


if __name__ == "__main__":
    main()
