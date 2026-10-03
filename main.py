"""Even and Odd Number Checker

A beginner-friendly Python program that determines whether an integer is
even or odd using conditional statements (if/else) and the modulus operator (%).
"""


def is_even(n: int) -> bool:
    """Check if an integer is even.

    The modulus operator (%) calculates the remainder after dividing n by 2.
    If the remainder is 0, the number is divisible by 2 with no remainder,
    meaning it is even.

    Parameters:
        n (int): The integer to check.

    Returns:
        bool: True if the integer is even, False otherwise.
    """
    # The modulus operator (%) returns the remainder of division.
    # When n is divided by 2, a remainder of 0 means the number is even.
    # In Python, this works seamlessly for positive numbers, negative numbers,
    # and zero (e.g., -4 % 2 == 0, -7 % 2 == 1, 0 % 2 == 0).
    return n % 2 == 0


def check_number(n: int) -> str:
    """Return 'Even' if the integer is even, or 'Odd' if it is odd.

    Uses an if/else conditional statement to return the result.

    Parameters:
        n (int): The integer to evaluate.

    Returns:
        str: "Even" or "Odd".
    """
    # Conditional logic:
    # if the condition evaluates to True, the 'if' block executes.
    # Otherwise, the 'else' block executes.
    if is_even(n):
        return "Even"
    else:
        return "Odd"


def main() -> None:
    """Run the interactive Command-Line Interface (CLI) loop."""
    print("=" * 45)
    print("       Even and Odd Number Checker")
    print("=" * 45)
    print("Enter any whole number to check if it is even or odd.")
    print("Type 'q' at any time to quit.\n")

    while True:
        user_input = input("Enter a number (or 'q' to quit): ").strip()

        # Check if the user wants to exit
        if user_input.lower() == "q":
            print("\nThank you for using Even and Odd Number Checker. Goodbye!")
            break

        # Input validation using try/except
        try:
            # Attempt to convert the input into an integer.
            # If the user entered text or a decimal number, a ValueError is raised.
            number = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid whole number (integers only, no decimals or text).\n")
            continue

        # Determine if the number is Even or Odd
        result = check_number(number)
        print(f"Result: {number} is {result}.\n")


if __name__ == "__main__":
    main()
