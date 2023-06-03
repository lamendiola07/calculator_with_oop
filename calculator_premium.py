from calculator_class import Calculator
from math import sqrt

class CalculatorPremium(Calculator):
    def square_root_operation(self,digit_one,digit_two):
        square_root_calcu_one = sqrt(digit_one)
        square_root_calcu_two = sqrt(digit_two)
        square_root_final = "The Square Root for Digit One is: ", square_root_calcu_one, "\n The Square Root for Digit Two is: ", square_root_calcu_two
        return square_root_final