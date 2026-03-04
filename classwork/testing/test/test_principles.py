
from app.math_demo import add

def test_addition() -> None:
    assert add(2, 2) == 4
    print("Test succed")

def main() -> None:
    test_addition()

if __name__ == "__main__":
    main()