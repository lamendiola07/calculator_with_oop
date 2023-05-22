#Creating two <class> for "user interface" and "computations"

#Created class for User Interface:
class UserInterface:
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