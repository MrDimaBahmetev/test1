import pytest
from main import calculate_avarage, multiply

def test_calculate_avarage():
    assert calculate_avarage([10,20,30]) == 20.0
    assert calculate_avarage([]) == 0.0
    assert calculate_avarage([5]) == 5.0 

def test_multilpy():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5