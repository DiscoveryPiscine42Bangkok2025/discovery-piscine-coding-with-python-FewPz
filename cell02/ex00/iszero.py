def is_zero(n: str) -> bool:
    """Check if the input string represents the integer zero."""
    try:
        return int(n) == 0
    except (ValueError, TypeError):
        return False

print(is_zero(input()))