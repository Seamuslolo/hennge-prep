def is_palindrome(s: object) -> bool:
    """
    If the reversed string is same as the orginal string, return True;
    otherwise return False
    """
    if ((type(s) is not str) and (type(s) is not int)):
        return False

    if (type(s) is str): # Uppercase and lowercase are treated the same
        s = s.lower() 

    if (type(s) is int): # Convert integer to string if needed
        s = str(s)
    
    s = s.strip() # remove leading and trailing spaces

    return s[::-1] == s # Reverse the string using slicing
        
def main():
    s = "cadac"

    if is_palindrome(s):
        print(f"{s} is a palindrome.")
    else:
        print(f"{s} is not a palindrome.")

if __name__ == "__main__":
    main() 