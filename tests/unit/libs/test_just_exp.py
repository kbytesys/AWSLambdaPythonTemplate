import time
from unittest.mock import patch, MagicMock

from libs.just_exp import business_demo
from libs.nice_utils import MagicCalculationResult, magic_calculation


@patch('time.time', MagicMock(return_value=12345))
def test_exp_valid():
    expected_calculation = MagicCalculationResult("test", 6)

    with patch("libs.just_exp.magic_calculation") as mocked_magic_calculation:
        mocked_magic_calculation.return_value = expected_calculation
        result = business_demo("test")
        assert mocked_magic_calculation.called_with("test", 1)
        assert result == expected_calculation


@patch('time.time', MagicMock(return_value=12345))
def test_exp_invalid():
    with patch("libs.just_exp.magic_calculation") as mocked_magic_calculation:
        mocked_magic_calculation.return_value = None
        result = business_demo("test")
        assert mocked_magic_calculation.called_with("test", 1)
        assert result is None
