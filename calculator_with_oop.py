from user_interface_class import UserInterface
from calculator_class import Calculator

userinterface = UserInterface()
calculator = Calculator()



#Pseudocode
#Displays Calculator Operations
print("C A L C U L A T O R    O P E R A T I O N S")
print("\n1 - A D D I T I O N \n2 - S U B T R A C T I O N \n3 - M U L T I P L I C A T I O N \n4 - D I V I S I O N")

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
        print("Error Detected!")
    else:
        print("No Error detected")
    finally:
        print("Sequence Complete")



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
        print("Error Detected!")
    else:
        print("No Error detected")
    finally:
        print("Sequence Complete")



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
        print("Error Detected!")
    else:
        print("No Error detected")
    finally:
        print("Sequence Complete")



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
        print("Error Detected!")
    else:
        print("No Error detected")
    finally:
        print("Sequence Complete")



