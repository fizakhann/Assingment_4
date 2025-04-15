def get_last_element(lst):
   
    print(lst[-1])

def get_lst():
   
    lst = []
    elem = input("Enter an element to end to the list.")
    while elem != "":
        lst.append(elem)
        elem = input("Enter an element to the end to yhe list.")
    return lst

def main():
    lst = get_lst()
    get_last_element(lst)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
