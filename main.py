from src.calculator import Calculator
from src.utils import get_python_info

def main():
    # Display Python environment info
    get_python_info()
    
    # Demo calculator
    calc = Calculator()
    result = calc.add(5, 3)
    print(f"\nDemo calculation: 5 + 3 = {result}")