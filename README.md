# Simple Python Calculator

## 📝 Overview
This is a **command-line calculator** written in Python that performs basic arithmetic operations: addition, subtraction, multiplication, and division. It features error handling for invalid inputs and division by zero.

## ✨ Features
- **Basic Operations**: Supports `+`, `-`, `*`, `/`
- **Error Handling**: 
  - Validates numeric inputs
  - Prevents division by zero
- **User-Friendly**: Clear prompts and formatted output
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed

### Installation
1. Clone the repository or download `calculator.py`
   ```bash
   git clone https://github.com/your-username/python-calculator.git
   ```
2. Navigate to the project directory
   ```bash
   cd python-calculator
   ```

### Usage
Run the calculator:
```bash
python calculator.py
```

Example session:
```
Simple Python Calculator
Operations: + (Addition), - (Subtraction), * (Multiplication), / (Division)
Enter first number: 10
Enter operation (+, -, *, /): *
Enter second number: 5
10.0 * 5.0 = 50.0
```

## 🛠️ Code Structure
```python
def calculator():
    # Display welcome message and instructions
    # Get user input for numbers and operation
    # Perform calculation based on operation
    # Handle errors (non-numeric input, division by zero)
    # Print formatted result

if __name__ == "__main__":
    calculator()  # Run the calculator when executed directly
```

## 🔍 Error Handling
The calculator gracefully handles:
- Non-numeric inputs (e.g., entering "ten" instead of 10)
- Division by zero attempts
- Invalid operation symbols

## 📚 Learning Points
This project demonstrates:
- Basic Python I/O operations
- Conditional statements
- Exception handling
- Function definition
- Floating-point arithmetic

## 🤝 Contributions
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## 📜 License
MIT License - see [LICENSE](LICENSE) file for details

## 🎯 Future Enhancements
- [ ] Add exponentiation operation
- [ ] Implement memory functions (M+, M-, MR)
- [ ] Add command history
- [ ] Create GUI version

## 📞 Support
For questions or issues, please open an issue in the repository.

---

### Example Calculations
| Operation | Example Input | Output |
|-----------|---------------|--------|
| Addition | 5 + 3 | 8.0 |
| Subtraction | 10 - 4 | 6.0 |
| Multiplication | 6 * 7 | 42.0 |
| Division | 20 / 5 | 4.0 |
| Division by Zero | 5 / 0 | Error message |

Enjoy calculating! 🧮
