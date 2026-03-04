from app.math_demo import add
from app.math_demo import calculate_tax


def test_addition() -> None:
    assert add(2, 2) == 4
    assert add(-10, 16) == 6
    assert add(-500, 250) == -250
    print("Test ADDITION PASSED")


def test_addition_commutative() -> None:
    assert add(-5, 12) == add(12, -5)
    assert add(100, -200) == add(-200, 100)
    print("Test ADDITION COMMUTATIVE PASSED")


def test_tax_calculation():
    assert calculate_tax(1000) == 150.0
    assert calculate_tax(100) == 15.0
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(-200) == -30
    assert calculate_tax(0) == 0
    print("Test TAX CALCULATION PASSED")


def main() -> None:
    test_addition()
    test_addition_commutative()
    test_tax_calculation()


if __name__ == "__main__":
    main()
