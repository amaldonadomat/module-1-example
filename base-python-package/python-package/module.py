def add(a, b):
    """Suma dos números."""
    return a + b

def subtract(a, b):
    """Resta el segundo número del primero."""
    return a - b

def multiply(a, b):
    """Multiplica dos números."""
    return a * b

def divide(a, b):
    """Divide el primer número por el segundo.

    Levanta una excepción si el divisor es cero.
    """
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b

if __name__ == "__main__":
    print("Módulo cargado correctamente. Usa las funciones en tu proyecto.")