
def divide_numbers():
   
    num1 = int(input("Enter an integer to be divided: "))
    
    num2 = int(input("Enter an integer to divide by: "))
    
    # Perform integer division and find the remainder
    quotient = num1 // num2
    remainder = num1 % num2
    
    # Print the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    divide_numbers()



    