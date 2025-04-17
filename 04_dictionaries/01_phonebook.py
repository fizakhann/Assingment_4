
def read_phone_numbers(phonebook):
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")

    if name in phonebook:
        print(f"{name} already exists in the phonebook.")
    else:
        phonebook[name] = number
        print(f"{name} added to the phonebook.")

def search_contact(phonebook):
    name = input("Enter the name to search: ")
    if name in phonebook:
        print(f"{name}'s number is {phonebook[name]}")
    else:
        print(f"{name} not found in the phonebook.")

def display_contact(phonebook):
    if phonebook:
        print("\nPhonebook contact list:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty.")
def delete_contact(phonebook):
    name = input("Enter the contact name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"{name} has been deleted from the phonebook.")
    else:
        print(f"{name} was not found in the phonebook.")

if __name__ == "__main__":
    phonebook = {}
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            read_phone_numbers(phonebook)
        elif choice == "2":
            search_contact(phonebook)
        elif choice == "3":
            display_contact(phonebook)
        elif choice == "4":
            delete_contact(phonebook)
        elif choice == "5":
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")