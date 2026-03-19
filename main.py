
def Add(numbers: str) -> float:
    if not numbers:
        return 0
    normal = numbers.replace('\n', ',')
    if ",\n" in numbers or "\n," in numbers:
        raise ValueError("Invalid separators")

    numbers_float = [float(x) for x in normal.split(',')]
    return sum(numbers_float)

