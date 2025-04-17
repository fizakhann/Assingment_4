MAX_FIB_VALUE = 10000

def print_fibonacci_sequence():
    a, b = 0, 1
    while a < MAX_FIB_VALUE:
        print(a, end=" ")
        a, b = b, a + b

if __name__ == "__main__":
    print_fibonacci_sequence()
