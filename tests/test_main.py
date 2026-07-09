import pytest
from main import calculate_avarage

def test_calculate_avarage():
    assert calculate_avarage([10,20,30]) == 20.0
    assert calculate_avarage([]) == 0.0
    assert calculate_avarage([5]) == 5.0 