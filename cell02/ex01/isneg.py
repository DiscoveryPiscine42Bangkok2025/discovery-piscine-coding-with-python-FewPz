def is_negative(n: str) -> int:
    """
    Check if the input string represents a negative integer.
    
    Returns:
        1 if the number is negative,
        0 if the number is zero,
        -1 if the number is positive.
        -99 if the input is not a valid integer.
    """
    try:
        num = int(n)
        if num < 0:
            return 1
        elif num == 0:
            return 0
        else:
            return -1
    except (ValueError, TypeError):
        return -99

result = is_negative(input())
if result == 1:
    print("This number is negative.")
elif result == 0:
    print("This number is both positive and negative.")
elif result == -1:
    print("This number is positive.")
