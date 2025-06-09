import re


def resolve(data: str) -> int:
    return sum(
        list(
            map(
                lambda x: int(x[0]) * int(x[1]),
                re.findall(
                    r"mul\((\d+),(\d+)\)",
                    " ".join(
                        re.findall(
                            r"do\(\)(.*?)don't\(\)",
                            "do()" + data.replace("\n", "") + "don't()",
                        )
                    ),
                ),
            )
        )
    )


def main() -> None:
    with open("./input/3.2/test.txt") as file:
        data = file.read().strip()

    assert resolve(data) == 48

    with open("./input/3.2/input.txt") as file:
        data = file.read().strip()

    print(resolve(data))


if __name__ == "__main__":
    main()
