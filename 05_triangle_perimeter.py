    
def triangle_sides():
    print("This code is about the sum of triangle sides")

    # Side 1 ka length 
    side1 = float(input("What is the length of side 1? "))

    # Side 2 ka length 
    side2 = float(input("What is the length of side 2? "))

    # Side 3 ka length 
    side3 = float(input("What is the length of side 3? "))

    # Perimeter calculate
    total = side1 + side2 + side3

    # Result
    print(f'The perimeter of {side1}, {side2}, and {side3} is {total}')

# Make sure this code runs only when it's the main file
if __name__ == "__main__":
    triangle_sides()
