"""
Refine Solution: Counter also apply for list so no need to store list
2. Create a list instead of dict
3. Scan the input txt file
4. After word validaiton, add the word into the counter object
5. Use the counter object to find the Top 5 words with biggest values.
"""

import string
import os
from collections import Counter

def count_words(text, n=5):
    """return the n most common words as a list of (word, count)."""
    words = []

    for word in text.split():
        word = word.lower()
        # Remove punctuation
        word = ''.join(
            c for c in word if c not in string.punctuation
            )

        if word:
            words.append(word)
    
    return Counter(words).most_common(n)


# Get sample.txt path
folder_abs_path = os.path.dirname(os.path.abspath(__file__)) 
input_file_path = os.path.join(folder_abs_path, "sample.txt")

def main():
    try:
        with open(input_file_path, 'r') as f:
            # the file object f is iterable
            # however we read the complete file into one string
            text = f.read()
            top_5 = count_words(text, 5)

            print("\n5 most common words with their counts:")
            for i, (word, freq) in enumerate(top_5, start=1):
                if freq == 1:
                    print(f"{i}. {word} - {freq} time")
                else:
                    print(f"{i}. {word} - {freq} times")
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()