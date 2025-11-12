def even_or_odd(n: int) -> str:
    """Return 'odd' or 'even' for the given integer n."""
    return "odd" if n % 2 else "even"
if __name__ == "__main__":
    try:
        n = int(input("Enter an integer: "))
        print(f"Number is {even_or_odd(n)}")
    except ValueError:
        print("Please enter a valid integer.")