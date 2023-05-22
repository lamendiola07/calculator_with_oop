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