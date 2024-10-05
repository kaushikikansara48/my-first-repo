# test_scratch.py

from scratch_4 import is_even  # Import the function from the file

def test_is_even():
    assert is_even(4) == True  # Test for an even number
    assert is_even(5) == False  # Test for an odd number
