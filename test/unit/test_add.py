from calculator_backend.add import add


def test_add() -> None:
    a = 1
    b = 2

    assert add(a, b) == a + b, "Addition failed"
