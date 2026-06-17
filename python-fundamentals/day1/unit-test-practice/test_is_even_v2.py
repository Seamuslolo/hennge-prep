import pytest
from main import is_even

@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (2, True),
        (1, False),
        (0, True),
        (-1, False),
        (-2, True),
    ],
)
def test_is_even_with_integers(number, expected):
    """Test is_even with valid inputs"""
    assert is_even(number) is expected 

@pytest.mark.parametrize(
    "invalid_input",
    [
        "str",
        2.2,
        True,
        {"dict": 0},
        [1, 2],
        (2, 0),
        {2, 3},
    ],
)
def test_is_even_returns_false_for_non_integer(invalid_input):
    """Test is_even return False for non-integer input."""
    assert is_even(invalid_input) is False 