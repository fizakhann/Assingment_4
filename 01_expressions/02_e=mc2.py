def energy():
    c: float = 299792458
    m: float = float(input("Enter the kilo mass: "))
    print("e = m * c^2")
    print("mass = " + str(m) + " kg")
    print("c = " + str(c) + " m/s")
    print("e = " + str(m * c ** 2) + " joules")

if __name__ == "__main__":
    energy()

