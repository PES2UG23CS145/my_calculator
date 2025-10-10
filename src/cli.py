"""
Command Line Interface for Calculator
Example:
    python src/cli.py add 5 3
    python -m src.cli subtract 10 4
"""

import sys
import click
from src.calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI supporting basic operations."""
    try:
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation in ["sqrt", "square_root"]:
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Format result nicely
        if isinstance(result, (int, float)):
            if result == int(result):
                click.echo(int(result))
            else:
                click.echo(f"{result:.2f}")
        else:
            click.echo(result)

    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        # Broad exception handler for unexpected runtime issues
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()  # pylint: disable=no-value-for-parameter
