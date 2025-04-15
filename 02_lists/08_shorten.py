max_length: int = 3  # Set the maximum allowed length of the list

def shorten(lst):
    # Remove and print elements until the list is down to MAX_LENGTH
    while len(lst) > max_length:
        last_elem = lst.pop()
        print(last_elem)

def get_lst():
    
    lst = []
    elem = input("Enter an element add to the list")
    while elem != "":
        lst.append(elem)
        elem = input("Enter an element add to the list")
    return lst

def main():
    lst = get_lst()
    shorten(lst)

# This provided line is required to run the program
if __name__ == '__main__':
    main()
