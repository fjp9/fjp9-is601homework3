from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
from decimal import Decimal
from typing import Callable

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(a, b, operation)
        return calculation.perform()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculation(a, b, add)
        return calculation.get_result()
    
    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a, b, subtract)  
        return calculation.get_result()
    
    @staticmethod
    def multiply (a,b):
        calculation = Calculation(a, b, multiply)  
        return calculation.get_result()
    
    @staticmethod
    def divide(a,b):
        calculation = Calculation(a, b, divide)
        return calculation.get_result()