import sys


def factorial(n):
    """Calcula el factorial de un número entero no negativo."""
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python my_script.py <número>  ")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        result = factorial(number)
        print(f"El factorial de {number} es {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
