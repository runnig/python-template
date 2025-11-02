import arithm


def calc(op: str, a: int, b: int) -> int:
    match op:
        case "+":
            return arithm.add(a, b)
        case _:
            raise ValueError(f"Unsupported operation: {op}")
