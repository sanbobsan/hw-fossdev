from pathlib import Path
from typing import TypedDict


class Sale(TypedDict):
    product_name: str
    category: str
    unit_price: float
    quantity: int


def _parse_record(line: str) -> Sale | None:
    sale: list[str] = line.strip().split(",")
    if len(sale) != 4:  # according to spec, there should be 4 fields
        return None
    try:
        product_name: str = sale[0]
        category: str = sale[1]
        unit_price: float = float(sale[2])
        quantity: int = int(sale[3])
    except ValueError:
        return None

    return {
        "product_name": product_name,
        "category": category,
        "unit_price": unit_price,
        "quantity": quantity,
    }


def read_data(path: str | Path) -> list[Sale]:
    result: list[Sale] = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            record: Sale | None = _parse_record(line)
            if record is not None:
                result.append(record)
    return result


def get_total_sum(sales: list[Sale], discount: float = 0) -> float:
    total_sum: float = 0
    for sale in sales:
        total_sum += sale["unit_price"] * sale["quantity"]
    if discount:
        total_sum = total_sum - total_sum * discount / 100
    return total_sum


def filter_by_threshold(sales: list[Sale], threshold: float) -> list[Sale]:
    """Finds sales that bigger than threshold"""
    result = []
    for sale in sales:
        sum = sale["unit_price"] * sale["quantity"]
        if sum >= threshold:
            result.append(sale)
    return result


def get_sum_by_category(sales: list[Sale]) -> dict[str, float]:
    """Returns sum by categories"""
    categories: dict[str, float] = {}
    for sale in sales:
        category: str = sale["category"]
        if category not in categories:
            categories[category] = 0
        categories[category] += sale["unit_price"] * sale["quantity"]
    return categories


def report(sales: list[Sale]) -> str:
    category_lines = [
        f"{category}: {sum}" for category, sum in get_sum_by_category(sales).items()
    ]
    result: str = (
        "Report\n"
        + "------\n"
        + "\n".join(category_lines)
        + "------\n"
        + f"Total: {get_total_sum(sales)}\n"
    )

    return result


def write_report(path: Path | str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
