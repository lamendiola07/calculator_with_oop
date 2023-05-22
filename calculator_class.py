#Creating two <class> for "user interface" and "computations"

#Created class for Calculator formulations
class Calculator:
    #created functions for operation calculations
    def addition_operation(self,digit_one,digit_two):
        #performs addition calculation
        sum_calculation = digit_one + digit_two
        return sum_calculation
    
    def subtraction_operation(self,digit_one,digit_two):
        #performs subtraction calculation
        subtraction_calculation = digit_one - digit_two
        return subtraction_calculation
    
    def multiplication_operation(self,digit_one,digit_two):
        #performs multiplication calculation
        multiplication_calculation = digit_one * digit_two
        return multiplication_calculation
    
    def division_operation(self,digit_one,digit_two):
        #performs division calculation
        division_calculation = digit_one / digit_two
        return division_calculation
