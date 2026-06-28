"""
Python: read a file of numbers (one per line) 
and print the sum, average, and largest.
"""

import os

def get_file_abs_path(file_path):
    folder_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder_path, file_path)


def main():
    print("Number Calculator")

    try:
        file_path = "sample.txt"
        file_path = get_file_abs_path(file_path) 
        
        # Initialize variables
        count = 0
        temp = 0
        largest = None

        with open(file_path, 'r') as file:
            for str_num in file:
                str_num = str_num.strip()
                # Skip blank lines
                if not str_num:
                    continue

                num = int(str_num)

                if largest is None or num > largest:
                    largest = num
                
                temp += num # add current number to the sum
                count += 1 # Increament count 

        # Handle empty / no valid number
        if count == 0:
            print("file is empty or no number is detected, nothing to compute")
            return
        print(f"  Sum: {temp}")
        print(f"  Average: {temp/count:.3f}")
        print(f"  Largest: {largest}\n")

    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("File contains invalid data (non-numeric value)")


if __name__ == "__main__":
    main()