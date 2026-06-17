"""
My Solution:
2. Create a dictionary
3. Scan the input txt file
4. if a new word is encounted, add to dict as a key initialize as 0
5. if word already existed in the dict, add the corresponding word's value by 1
6. Find the Top 5 words with biggest values.
"""

import os
import string
from collections import Counter

# this make sure the file name isn't relative to the working directory
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'sample.txt')
    
try:
    words = {}

    with open(file_path, 'r') as f:
        for line in f:
            for word in line.split():   # split the line strings to word list.
                word = word.lower()

                # Prevent punctiuation stand along 
                word = ''.join(
                    c for c in word if c not in string.punctuation 
                    )
                
                 
                if word:
                    # if the current word exists in the dir
                    # Increament
                    if word in words:
                        words[word] += 1
                    else:
                        # if not store the key and initialize with 1
                        words[word] = 1

    word_counts = Counter(words)

    top_5 = word_counts.most_common(5)

    print("Top 5 most common words:")
    for word, count in top_5:
        print(f"{word}: {count}")
    
except FileNotFoundError:
    print("Input file not found in main.py")

