import functools


def resolve(data: str) -> int:
    N = [int(n) for n in data.strip().split()]

    return functools.reduce(
        lambda x, y: x + y,
        map(
            lambda x: abs(x[0] - x[1]),
            zip(
                sorted(N[::2]),
                sorted(N[1::2]),
            ),
        ),
        0,
    )


def main() -> None:
    with open("./input/1/test.txt") as file:
        data = file.read().strip()

    assert resolve(data) == 11

    with open("./input/1/input.txt") as file:
        data = file.read().strip()

    print(resolve(data))


if __name__ == "__main__":
    main()
