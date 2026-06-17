# Word counter

## Problem & assumptions
- Uppercase and lowercase forms are treated as the same word (fish == Fish) 
- Punctuation is ignored and removed from words (end. == end)

## v1 — naive approahc
- Store each word as a dictionary key and map it to its frequency
- Scan the input text file one line at a time
- If a word has not been encountered before, add it to the dictionary with an initial count of 1
- If the word already exists in the dictionary, increament its count by 1 
The if/else counting logic was somwhat clumsy. Python's Counter class makes this logic unnecessary. 

## v2 — idiomatic
 


## What I learned / would do differently
- How to create and run test file in python
- How to use Python's Counter class 
- Create a list of every wrod before counting for a huge file takes up lot of memory, updating a counter as I read each line would be more a memory effienct approach.
- create ve and ve file that contain the set up so each project can use the exact package versions it needs without causing conflicts with other projects
- if __name__ == "__main__": ensures the program runs only when the file is executed directly, preventing it from running automatically when the file is imported into another file. so the unit testing can be run without running the main function.

cd ~abs_project_folder
python3 -m venv .venv
source .venv/bin/activate
pip install pytest 
