def is_even(n: object) -> bool:
    """Return True if number is an even integer; otherwise, return Fasle"""
    if type(n) is not int:
        return False

    return n % 2 == 0

def main():
    """Demostrate the is_even function."""
    input_num = 5
    
    if (is_even(input_num)):
        print(f"{input_num} is an even number.")
    else:
        print(f"{input_num} is an odd number.")

if __name__ == "__main__":
    main() 