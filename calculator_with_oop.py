from user_interface_class import UserInterface
from calculator_class import Calculator
from calculator_premium import CalculatorPremium

import pyfiglet
from simple_colors import *
from pyfiglet import figlet_format

userinterface = UserInterface()
calculator = Calculator()
calcu_premium = CalculatorPremium()

print(blue("\n\nLOGIE A. MENDIOLA | BSCPE 1 - 5 | OBJECT ORIENTED PROGRAMMING - ASSIGNMENT #7 "))
print(blue("INSTRUCTIONS: Re-create Calculator Program with Object Oriented Methods\n\n"))

#Pseudocode
def calculator_program():

    #Asking the user for their Calculator Unit
    print(userinterface.CalculatorUnit(),"is starting to run . . . . . .\n\n")

    #Displays Calculator Operations
    print(yellow("C A L C U L A T O R    O P E R A T I O N S",['bold']))
    print(yellow("\n1 - A D D I T I O N \n2 - S U B T R A C T I O N \n3 - M U L T I P L I C A T I O N \n4 - D I V I S I O N \n5 - S Q U A R E  R O O T" ,['bold']))

    #Ask the user to choose an operation to be used
    ChooseOperation = int(input("\n\nPlease Choose an Operation to Use: "))


    #Performs Addition Operation if user chose "1"
    if ChooseOperation == 1:
        try:
            #Ask the user for their 1st digit
            digit_one = userinterface.user_input_one()

            #Ask the user for their 2nd digit
            digit_two = userinterface.user_input_two()

            #Performing Addition Calculation
            summation = calculator.addition_operation(digit_one, digit_two)

            # Print Summation Result
            userinterface.display_summation(summation)

        except:
            print(red("Error Detected!"))
        else:
            print("No Error detected")
        finally:
            print(green("Sequence Complete"))



    #Performs Subtraction Operation if user chose "2"
    elif ChooseOperation == 2:
        try:
            #Ask the user for their 1st digit
            digit_one = userinterface.user_input_one()

            #Ask the user for their 2nd digit
            digit_two = userinterface.user_input_two()

            #Performing Subtraction Calculation
            difference = calculator.subtraction_operation(digit_one, digit_two)

            # Print Difference Result
            userinterface.display_difference(difference)

        except:
            print(red("Error Detected!"))
        else:
            print("No Error detected")
        finally:
            print(green("Sequence Complete"))



    #Performs Multiplication Operation if user chose "3"
    elif ChooseOperation == 3:
        try:
            #Ask the user for their 1st digit
            digit_one = userinterface.user_input_one()

            #Ask the user for their 2nd digit
            digit_two = userinterface.user_input_two()

            #Performing Multiplication Calculation
            product = calculator.multiplication_operation(digit_one, digit_two)

            # Print Product Result
            userinterface.display_product(product)

        except:
            print(red("Error Detected!"))
        else:
            print("No Error detected")
        finally:
            print(green("Sequence Complete"))



    #Performs Divison Operation if user chose "4"
    elif ChooseOperation == 4:
        try:
            #Ask the user for their 1st digit
            digit_one = userinterface.user_input_one()

            #Ask the user for their 2nd digit
            digit_two = userinterface.user_input_two()

            #Performing Division Calculation
            quotient = calculator.division_operation(digit_one, digit_two)

            # Print Quotient Result
            userinterface.display_quotient(quotient)
        
        except:
            print(red("Error Detected!"))
        else:
            print("No Error detected")
        finally:
            print(green("Sequence Complete"))
    
    #Performs Square Root Operation if user chose "5"
    elif ChooseOperation == 5:
        try:
            #Ask the user for their 1st digit
            digit_one = userinterface.user_input_one()

            #Ask the user for their 2nd digit
            digit_two = userinterface.user_input_two()

            #Performing Square Root Calculation
            sqrt_result = calcu_premium.square_root_operation(digit_one, digit_two)

            # Print Square Root Results
            userinterface.display_square_root(sqrt_result)

        except:
            print(red("Error Detected!"))
        else:
            print("No Error detected")
        finally:
            print(green("Sequence Complete"))

calculator_program()

while True:
    AskRepeat = int(input("\nRepeat Sequence? Please type '1' to Repeat Sequence or type '2' if not: "))

    if AskRepeat == 1:
        print(magenta("\nRepeating Sequence . . .\n"))
        calculator_program()
    
    else:
        print(blue("\nSequence Completed"))
        break


