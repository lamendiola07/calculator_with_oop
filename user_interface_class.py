#Creating two <class> for "user interface" and "computations"

from simple_colors import *

#Created class for User Interface:
class UserInterface:
    def __init__(self, unit = ""):
        self.unit = unit

    #created function to ask user for number inputs
    def user_input_one(self):
        #ask the user to input for their first digit
        digit_one = float(input("Please enter your first digit: "))
        return digit_one
    
    def user_input_two(self):
        #ask the user to input for their second digit
        digit_two = float(input("Please enter your second digit: "))
        return digit_two
    
    def display_summation(self, summation):
        #displays addition calculation
        print (summation)

    def display_difference(self, difference):
        #displays subtraction calculation
        print (difference)

    def display_product(self, product):
        #display multiplication calculation
        print (product)
    
    def display_quotient(self, quotient):
        #display quotient calculation
        print (quotient)
    
    def CalculatorUnit(self):
        self.unit = input("What is your Calculator Unit? ")
        self.unit = (magenta(self.unit))
        return self.unit
    
    def display_square_root(self, sqrt_result):
        #display square root calculation
        print (sqrt_result)