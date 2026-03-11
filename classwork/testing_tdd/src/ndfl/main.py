def calculate_ndfl_tax(income: float) -> float:
    result = 0.0

    if income >= 5_000_000:
        result += (income - 5_000_000) * 0.18
        income = 5_000_000

    if income >= 2_400_000:
        result += (income - 2_400_000) * 0.15
        income = 2_400_000

    if income:
        result += income * 0.13

    return result
