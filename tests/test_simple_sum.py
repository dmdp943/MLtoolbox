# tests/test_lib.py
from MLtoolbox.simple_sum import sum_numbers

def test_sum_numbers():
    assert sum_numbers(2,1.5) == 3.5
