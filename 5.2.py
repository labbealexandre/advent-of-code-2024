def merge(a: list[int], b: list[int], rules: list[tuple[int]]) -> list[int]:
    if len(a) == 0 and len(b) == 0:
        return []

    elif len(a) == 0:
        return [b[0]]

    elif len(b) == 0:
        return [a[0]]

    if (b[0], a[0]) in rules:
        return [b[0], a[0]]

    return [a[0], b[0]]


def sort(update: list[int], rules: list[tuple[int]]) -> int:
    return merge(
        sort(update[: len(update) // 2], rules),
        sort(update[len(update) // 2 :], rules),
    )


def resolve(data: str) -> int:
    rules = list(
        map(
            lambda x: (
                int(x.split("|")[0]),
                int(x.split("|")[1]),
            ),
            data.split("\n\n")[0].split(),
        )
    )
    print(rules)

    f = list(
        filter(
            lambda y: not all(
                list(
                    map(
                        lambda i: all(
                            list(
                                map(
                                    lambda x: y[i] != x[0] or x[1] not in y[:i],
                                    list(
                                        map(
                                            lambda x: (
                                                int(x.split("|")[0]),
                                                int(x.split("|")[1]),
                                            ),
                                            data.split("\n\n")[0].split(),
                                        )
                                    ),
                                )
                            )
                        ),
                        range(len(y)),
                    )
                )
            ),
            list(
                map(
                    lambda y: list(map(lambda x: int(x), y.split(","))),
                    data.split("\n\n")[1].split(),
                )
            ),
        )
    )
    print(f)


def main() -> None:
    with open("./input/5/test.txt") as file:
        data = file.read().strip()

    assert resolve(data) == 123

    with open("./input/5/input.txt") as file:
        data = file.read().strip()

    print(resolve(data))


if __name__ == "__main__":
    main()
