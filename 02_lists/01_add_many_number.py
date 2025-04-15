def add(nums) -> int:
    total = 0
    for n in nums:
        total += n
    return total

# There is no need to edit code beyond this point

def main():
    nums: list[int] = [1, 2, 3, 4, 5]  # Make a list of numbers
    result: int = add(nums)  # Find the sum of the list
    print(result)  # Print out the sum above

if __name__ == "__main__":
    main()

