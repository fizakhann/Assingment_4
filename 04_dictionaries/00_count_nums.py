
def count_number():
    count_dic = {}
    while True:
        user_input = input("Enter a number (or 'exit' to quit): ")

        if user_input.lower() == "exit":
            break

        if user_input.isdigit():
            num = int(user_input)
            count_dic[num] = count_dic.get(num, 0) + 1
        else:
            print("Invalid input. Please enter a number or 'exit'.")

    return count_dic


def display_counts(count_dict):
    print("\nNumber count:")
    for key, value in count_dict.items():
        print(f'{key} appears {value} time{"s" if value != 1 else ""}.')


# Entry point
if __name__ == '__main__':
    counts = count_number()
    display_counts(counts)



