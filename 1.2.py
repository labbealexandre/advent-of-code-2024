def resolve(data: str) -> int:
    N = [int(n) for n in data.strip().split()]

    return sum(
        list(
            map(
                lambda x: x[0] * x[1][0] * x[1][1],
                enumerate(
                    list(
                        zip(
                            list(map(lambda x: N[::2].count(x), range(max(N)))),
                            list(map(lambda x: N[1::2].count(x), range(max(N)))),
                        )
                    )
                ),
            )
        )
    )


def main() -> None:
    with open("./input/1/test.txt") as file:
        data = file.read().strip()

    assert resolve(data) == 31

    with open("./input/1/input.txt") as file:
        data = file.read().strip()

    print(resolve(data))


if __name__ == "__main__":
    main()
