# LLM-Check

A collection of simple, well-tested utility programs in Python and Java.

## Programs

### 1. Addition Program (Python)

A simple Python script that adds two numbers, runnable as a module or from the command line.

**Usage:**

```bash
python addition.py <num1> <num2>
```

**Example:**

```bash
python addition.py 5 3
# Output: Result: 8.0
```

### 2. Calculator (Java)

A console-based calculator supporting addition, subtraction, multiplication, and division, with graceful error handling for invalid input and division by zero.

**Usage:**

```bash
javac Calculator.java
java Calculator
```

Follow the interactive prompts to enter two numbers and an operator (`+`, `-`, `*`, `/`).

**Example:**

```
Enter first number: 5
Enter operator (+, -, *, /): +
Enter second number: 3
Result: 5.0 + 3.0 = 8.0
```

## Testing

### Python

The addition program includes unit tests built with `unittest`:

```bash
python test_addition.py
```

Expected output:

```
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

The tests cover:
- Positive numbers
- Negative numbers
- Mixed positive and negative numbers
- Floating-point numbers

## Requirements

- Python 3.x
- Java Development Kit (JDK) 8 or later

## Project Structure

```
llm-check/
├── addition.py        # Python addition program (module + CLI)
├── test_addition.py   # Unit tests for addition.py
├── Calculator.java    # Java console calculator
└── README.md          # This file
```

## License

This project is for demonstration and educational purposes.
