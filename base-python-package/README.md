# python-package

A simple Python package for basic mathematical operations.

## Features

- **Addition**: Add two numbers.
- **Subtraction**: Subtract one number from another.
- **Multiplication**: Multiply two numbers.
- **Division**: Divide one number by another, with error handling for division by zero.

## Installation

Clone the repository and install the package locally using `pip`:

```bash
git clone https://github.com/amaldonadomat/module-1-example.git
cd module-1-example
pip install .

```

Or install directly from the source:

```bash
pip install git+https://github.com/amaldonadomat/module-1-example.git
```

## Usage

Import the functions and use them in your Python code:


```
from my_package import add, subtract, multiply, divide
```


Example usage
```
print(add(5, 3))         # Output: 8
print(subtract(10, 7))   # Output: 3
print(multiply(4, 6))    # Output: 24

try:
    print(divide(9, 3))  # Output: 3.0
    print(divide(1, 0))  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
```
## Project Structure
```
my_project/
├── python-package/
│   ├── __init__.py          # Package initialization
│   ├── module.py            # Core mathematical operations
├── setup.py                 # Packaging and installation configuration
├── README.md                # Project documentation
├── LICENSE                  # License information
```

## Testing

To test the package, create a virtual environment and run the module directly:

```
python my_package/module.py
```

Or write additional test scripts that import the package.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.