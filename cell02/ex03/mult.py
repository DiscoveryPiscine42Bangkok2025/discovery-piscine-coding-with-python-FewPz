first_number = input("Enter the first number:\n")
second_number = input("Enter the second number:\n")

try:
    first_number = int(first_number)
    second_number = int(second_number)
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")
    if result < 0:
        print("The result is negative.")
    elif result == 0:
        print("The result is positive and negative.")
    elif result > 0:
        print("The result is positive.")
except (ValueError, TypeError):
    pass