
def temp():
   fahrenheit_degree = float(input("Enter your Fahrenheit degree: "))  # Assigning input to fahrenheit_degree
   celsius_degree = (fahrenheit_degree - 32) * 5.0 / 9.0  #  formula to convert Fahrenheit to Celsius
   print(f"Temperature {fahrenheit_degree}F = {celsius_degree}C")  

if __name__ == "__main__": 
    temp()