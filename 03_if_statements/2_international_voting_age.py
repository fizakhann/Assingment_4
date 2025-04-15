def main():
    
    age = int(input("How old are you? "))

    # Define the voting ages
    peturksbouipo_age = 16
    stanlau_age = 25
    mayengua_age = 48

    # Check voting eligibility for each country
    if age >= peturksbouipo_age:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")

    if age >= stanlau_age:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")

    if age >= mayengua_age:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")


if __name__ == '__main__':
    main()
