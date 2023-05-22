from user_interface_class import UserInterface
from calculator_class import Calculator

userinterface = UserInterface()
calculator = Calculator()



#Pseudocode

#Ask the user for their 1st digit
digit_one = userinterface.user_input_one()

#Ask the user for their 2nd digit
digit_two = userinterface.user_input_two()

#Performing Addition Calculation
summation = calculator.addition_operation(digit_one, digit_two)

# Print Summation Result
userinterface.display_summation(summation)



#Performing Subtraction Calculation
difference = calculator.subtraction_operation(digit_one, digit_two)

#Performing Multiplication Calculation
product = calculator.multiplication_operation(digit_one, digit_two)

#Performing Division Calculation
quotient = calculator.division_operation(digit_one, digit_two)

