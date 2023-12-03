import pytest
from day1_2 import get_calibration_value


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("treb7uchet", 77),
        ("trebsevenuchet", 77),
        ("honemkmbfbnlhtbq19twonekbp", 11),
        ("3nqqgfone", 31),
    ],
)
def test_get_calibration_value(test_input, expected):
    assert get_calibration_value(test_input) == expected
