#Creating two <class> for "user interface" and "computations"

#Created class for Calculator formulations
class Calculator:
    #creating function for addition calculation
    def addition_operation(self,digit_one,digit_two):
        sum_calculation = digit_one + digit_two
        return sum_calculation
    
    def subtraction_operation(self,digit_one,digit_two):
        subtraction_calculation = digit_one - digit_two
        return subtraction_calculation
    
    def multiplication_operation(self,digit_one,digit_two):
        multiplication_calculation = digit_one * digit_two
        return multiplication_calculation
    
    def division_operation(self,digit_one,digit_two):
        division_calculation = digit_one / digit_two
        return division_calculation
