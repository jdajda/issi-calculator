"""Calculator module"""

class Calculator:
    """Calculator."""
    def __init__(self, op1: float, op2: float):
        self.__op1 = op1
        self.__op2 = op2

    def add(self):
        """Zwraca sumę dwóch liczb."""
        return self.__op1 + self.__op2

    def subtract(self):
        """Zwraca różnicę dwóch liczb."""
        return self.__op1 - self.__op2

    def multiply(self):
        """Zwraca iloczyn dwóch liczb."""
        return self.__op1 * self.__op2

    def divide(self):
        """Zwraca iloraz dwóch liczb, z obsługą dzielenia przez zero."""
        if self.__op2 == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero!")
        return self.__op1 / self.__op2

def main():
    """Demo """
    calc = Calculator(10, 5)

    print("Test klasy Calculator:\n")
    print(f"Dodawanie: 10 + 5 = {calc.add()}")
    print(f"Odejmowanie: 10 - 5  = {calc.subtract()}")
    print(f"Mnożenie: 10 * 5  = {calc.multiply()}")
    print(f"Dzielenie: 10 / 5  = {calc.divide()}")


if __name__ == "__main__":
    main()
