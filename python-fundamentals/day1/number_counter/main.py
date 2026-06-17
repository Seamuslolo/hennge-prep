"""
Python: read a file of numbers (one per line) 
and print the sum, average, and largest.
"""

import os

def main():
    print("Number Calculator")

    try:
        folder_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(folder_path, "sample.txt")

        count = 0
        sum = 0
        largest = 0

        with open(file_path, 'r') as file:
            for str_num in file:
                num = int(str_num)

                if count == 0:
                    # Set the first integer as largest
                    largest = num
                elif num > largest:
                    # Compare current number with largest number
                    largest = num

                sum += num # add current number to the sum
                count += 1 # Increament count 
        
        print(f"  Sum: {sum}")
        print(f"  Average: {sum/count}")
        print(f"  Largest: {largest}\n")

    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()