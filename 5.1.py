def resolve(data: str) -> int:
    return sum(
        list(
            map(
                lambda l: l[len(l) // 2],
                list(
                    filter(
                        lambda y: all(
                            list(
                                map(
                                    lambda i: all(
                                        list(
                                            map(
                                                lambda x: y[i] != x[0]
                                                or x[1] not in y[:i],
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
                ),
            )
        )
    )


def main() -> None:
    with open("./input/5/test.txt") as file:
        data = file.read().strip()

    assert resolve(data) == 143

    with open("./input/5/input.txt") as file:
        data = file.read().strip()

    print(resolve(data))


if __name__ == "__main__":
    main()
