from pathlib import Path
from typing import NamedTuple


class Sale(NamedTuple):
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


def total(sales: list[Sale], discount: float = 0):
    total_sum: float = 0

    for sale in sales:
        total_sum = total_sum + sale.unit_price * sale.quantity
    if discount:
        total_sum = total_sum - total_sum * discount / 100

    return total_sum


def find_big(ds, t):
    out = []  # rows that are big enough
    for i in ds:  # each row
        x = i["a"] * i["q"]  # row money
        if x >= t:  # compare with threshold
            out.append(i)  # save row
    return out  # done


def by_category(ds):
    m = {}  # category to money
    for i in ds:  # each row
        k = i["c"]  # category name
        if k not in m:  # create if needed
            m[k] = 0  # start from zero
        m[k] += i["a"] * i["q"]  # add row amount
    return m  # return mapping


def report(ds):
    lines = []  # text lines
    lines.append("Report")  # title
    lines.append("------")  # separator

    for k, v in by_category(ds).items():  # category and amount
        lines.append(f"{k}: {v}")  # make line

    lines.append("------")  # separator again
    lines.append(f"Total: {total(ds)}")  # total sum

    return "\n".join(lines)  # merge lines


def write_report(path, txt):
    # TODO better errors
    with open(path, "w", encoding="utf-8") as f:  # open file for writing
        f.write(txt)  # write text
