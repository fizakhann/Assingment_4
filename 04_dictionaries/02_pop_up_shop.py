def main():
    # Dictionary of fruits and their prices per unit
    fruit_prices = {
        "apple": 5.0,
        "durian": 20.0,
        "jackfruit": 15.5,
        "kiwi": 6.0,
        "rambutan": 8.0,
        "mango": 10.0
    }

    total_cost = 0.0

    # Ask the user how many of each fruit they want
    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        
        total_cost += quantity * price

    print(f"\nYour total is ${total_cost:.2f}")

if __name__ == "__main__":
    main()

