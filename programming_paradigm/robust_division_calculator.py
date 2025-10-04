def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with error handling for:
    - Division by zero
    - Non-numeric input
    """
    try:
        num = float(numerator)
        denom = float(denominator)

        result = num / denom
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
