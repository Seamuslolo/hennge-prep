from main import is_palindrome
import pytest

@pytest.mark.parametrize(
    ("s", "expected"), 
    [
        ("bananana", False),    # Not palindrome 
        ("dad", True),          # palindrome
        ("Dad", True),          # Uppercase and lowercase are treated the same
        ("Dad  ", True),        # Ingore extra spaces
        (123, False),           #  Not palindrome number
        (121, True),            # palindrome number
    ],
)
def test_is_palindrome_with_valid_string(s, expected):
    assert is_palindrome(s) is expected


@pytest.mark.parametrize(
    "invalid_input", 
    [
        1.2,          # raitonal number
        {1, 2},       # set
        (1, ),        # tuple
        [1, 2],       # list
        {"key1": 1, },# dict
        True          # bool
    ]
)
def test_is_palindrome_return_false_for_invalid_input(invalid_input):
    assert is_palindrome(invalid_input) is False