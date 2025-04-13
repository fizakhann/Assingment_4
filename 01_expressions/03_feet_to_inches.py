Inch: int = 12

def foot():
    feet: int = int(input("Enter feet and it will convert into inches: "))
    print(f'There are {Inch * feet} inches in {feet} feet.')

if __name__ == "__main__":
    foot()
