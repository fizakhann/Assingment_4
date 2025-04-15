def add_three_copies(lst, data):
    # Add three copies of data to the list (in-place modification)
    for _ in range(3):
        lst.append(data)

def main():
   
    message = input("Enter a message to copy: ")

    messages = []

    # Show list before modification
    print("List before:", messages)

    add_three_copies(messages, message)

    # Show list after modification
    print("List after:", messages)


if __name__ == '__main__':
    main()
