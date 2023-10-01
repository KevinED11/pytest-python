


def sum(a: int, b: int) -> int:
    return a + b


def test_sum():
    assert sum(3, 2) == 5


def test_expected_return_type_in_sum_function():
    assert isinstance(sum(3, 2), int)

def main() -> None:
    sum(3, 2)


if __name__ == '__main__':
    main()