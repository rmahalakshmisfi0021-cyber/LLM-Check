def add(a, b):
    """Adds two numbers."""
    return a + b

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            print(f"Result: {add(num1, num2)}")
        except ValueError:
            print("Error: Please provide two valid numbers.")
    else:
        print("Usage: python addition.py <num1> <num2>")
