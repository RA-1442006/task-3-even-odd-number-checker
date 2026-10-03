# Even and Odd Number Checker

A clean, beginner-friendly Python command-line utility that determines whether a given integer is **Even** or **Odd**. The application demonstrates essential programming foundations, including conditional control flow (`if` / `elif` / `else`), the modulus operator (`%`), error handling (`try` / `except`), and unit testing.

---

## 🎯 Learning Objective

The primary objective of this project is to master:
1. **The Modulus Operator (`%`)**: Understanding how remainder-based division is used to identify divisibility and number parity.
2. **Conditional Branching (`if` / `elif` / `else`)**: Directing program execution based on boolean truth values.
3. **Robust Input Validation**: Using exception handling (`try` / `except ValueError`) to gracefully manage unexpected user input (e.g., text strings or floating-point decimals) without crashing.
4. **Interactive CLI Design**: Structuring an interactive `while` loop that cleanly terminates when the user chooses to exit.

---

## 🛠️ Tools Used

- **Language**: Python 3 (Standard Library only)
- **Testing Framework**: `unittest` (built-in Python standard library)
- **Version Control**: Git & GitHub-ready structure

*No external dependencies or third-party packages are required.*

---

## 🚀 How to Run the Program and Tests

### 1. Prerequisites
Ensure Python 3.8+ is installed on your system. You can verify your installation by running:
```bash
python --version
```

### 2. Running the Program
Run the main script from your terminal:
```bash
python main.py
```
Follow the interactive prompt:
- Enter any whole number (e.g., `42`, `-7`, `0`).
- Type `q` or `Q` to quit the program.

### 3. Running the Unit Tests
Execute the test suite using Python's built-in `unittest` runner:
```bash
python -m unittest test_main.py -v
```

All test cases (covering positive numbers, negative numbers, zero, and large integers) will execute with verbose feedback.

---

## 💻 Sample Input / Output Examples

### Example 1: Even & Odd Numbers
```text
Enter a number (or 'q' to quit): 14
Result: 14 is Even.

Enter a number (or 'q' to quit): 27
Result: 27 is Odd.
```

### Example 2: Negative Numbers & Zero
```text
Enter a number (or 'q' to quit): -8
Result: -8 is Even.

Enter a number (or 'q' to quit): -13
Result: -13 is Odd.

Enter a number (or 'q' to quit): 0
Result: 0 is Even.
```

### Example 3: Input Validation & Recovery
```text
Enter a number (or 'q' to quit): apple
Invalid input! Please enter a valid whole number (integers only, no decimals or text).

Enter a number (or 'q' to quit): 12.34
Invalid input! Please enter a valid whole number (integers only, no decimals or text).

Enter a number (or 'q' to quit): 50
Result: 50 is Even.

Enter a number (or 'q' to quit): q

Thank you for using Even and Odd Number Checker. Goodbye!
```

---

## 🔍 How the Modulus (`%`) Operator Works

The modulus operator (`%`) computes the **remainder** left over after dividing one integer by another.

$$\text{Dividend} = (\text{Divisor} \times \text{Quotient}) + \text{Remainder}$$

When checking whether an integer $n$ is even or odd:
- We divide $n$ by $2$: `n % 2`.
- Any integer that is divisible by $2$ leaves a remainder of `0` ($n \pmod 2 = 0$). Hence, `n % 2 == 0` evaluates to `True` for all **even** numbers.
- Any integer that is not divisible by $2$ leaves a remainder of `1` ($n \pmod 2 = 1$). Hence, `n % 2 == 0` evaluates to `False` for all **odd** numbers.

### Behavior in Python:
- **Positive numbers**: `10 % 2 == 0` (Even), `11 % 2 == 1` (Odd).
- **Negative numbers**: Python uses floor division; `-4 % 2 == 0` (Even), `-7 % 2 == 1` (Odd).
- **Zero**: `0 % 2 == 0` (Zero is an even number because it is an integer multiple of 2: $0 = 2 \times 0$).

---

## 💡 Interview Questions & Answers

### a) How do you check whether a number is even in Python?
You check whether a number is even by applying the modulus operator `%` with `2` and checking if the remainder is `0`:
```python
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```
Alternatively, in bitwise operations, you can check `(number & 1) == 0`.

---

### b) What is the purpose of the `%` operator?
The `%` (modulus) operator returns the remainder of the division between two numbers. In addition to testing for even/odd parity and general divisibility (e.g., checking leap years or prime numbers), it is widely used for:
- Keeping values constrained within a fixed cyclical range (such as clock arithmetic: `hour % 12`).
- Wrapping circular array indices.
- Formatting alternating rows or periodic batch triggers in loops.

---

### c) What is the difference between `if`, `elif`, and `else`?
- **`if`**: The initial condition evaluated. If its expression evaluates to `True`, Python executes its code block and skips the rest of the chain.
- **`elif`** (short for *else if*): An optional intermediate condition evaluated only if all preceding `if` and `elif` checks were `False`. You can have multiple `elif` blocks to check mutually exclusive conditions in sequence.
- **`else`**: The final fallback branch. It takes no condition and executes only if every preceding `if` and `elif` evaluated to `False`.

---

## 👤 Author

**M. Rohithanjan**
