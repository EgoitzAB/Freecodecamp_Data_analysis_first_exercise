#!/usr/bin/python3
import pytest
from mean_var_std import calculate

def test_nine_values_exception():
    with pytest.raises(ValueError) as excinfo:
        calculate([0,1,2])
    assert str(excinfo.value) == "List must contain nine numbers."

def test_nine_values_passes():
    actual = calculate([0,1,2,3,4,5,6,7,8])
    assert actual

def test_calculate():
    actual = calculate([0,1,2,3,4,5,6,7,8])
    expected = {'mean': ([3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0), 'variance': ([6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667), 'standard deviation': ([2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611), 'max': ([6, 7, 8], [2, 5, 8], 8), 'min': ([0, 1, 2], [0, 3, 6], 0), 'sum': ([9, 12, 15], [3, 12, 21], 36)}
    assert actual == expected

def test_calculate_1_not_equal():
    actual = calculate([0,1,2,3,4,5,6,7,9])
    expected = {'mean': ([3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0), 'variance': ([6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667), 'standard deviation': ([2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611), 'max': ([6, 7, 8], [2, 5, 8], 8), 'min': ([0, 1, 2], [0, 3, 6], 0), 'sum': ([9, 12, 15], [3, 12, 21], 36)}
    assert actual != expected

if __name__=='__main__':
    pytest.main(['test_module.py', '--verbose'])
