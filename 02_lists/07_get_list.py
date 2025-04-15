def main():
    lst = []  # empty list

    val = input("Enter a value: ")  
    while val:  # Keep looping until the user enters nothing
        lst.append(val)  # Add the value to the list
        val = input("Enter a value: ")  # Prompt again

    print("Here's the list:", lst)

if __name__ == '__main__':
    main()
