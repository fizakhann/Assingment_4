import random

def roll_dice():
    # Simulate rolling two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    # Calculation
    total = die1 + die2

    # Print results
    print(f"You rolled a {die1} and a {die2}.")
    print(f"The total is {total}.")

if __name__ == "__main__":
    roll_dice()
