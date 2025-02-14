from calculator_backend.multiply import multiply


def test_multiply() -> None:
    a = 3
    b = 4

    assert multiply(a, b) == a * b
