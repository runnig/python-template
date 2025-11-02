from example_cli import calc


def test_ans() -> None:
    assert calc.calc("+", 3, 2) == 5
