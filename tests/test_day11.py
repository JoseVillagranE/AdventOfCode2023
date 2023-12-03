import pytest
from day1_1 import get_calibration_value


@pytest.mark.parametrize(
    "test_input,expected",
    [("1abc2", 12), ("pqr3stu8vwx", 38), ("a1b2c3d4e5f", 15), ("treb7uchet", 77)],
)
def test_get_calibration_value(test_input, expected):
    assert get_calibration_value(test_input) == expected
