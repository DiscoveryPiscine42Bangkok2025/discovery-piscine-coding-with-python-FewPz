def is_zero(n: str) -> bool:
    """Check if the input string represents the integer zero."""
    try:
        return float(n) == 0
    except (ValueError, TypeError):
        return False

result = is_zero(input())
if result:
    print("This number is equal to zero.")
else:
    print("This number is different from zero.")