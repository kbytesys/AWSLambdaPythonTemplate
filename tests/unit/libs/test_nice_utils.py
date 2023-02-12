from unittest import mock

from libs.nice_utils import magic_calculation, MagicCalculationResult


@mock.patch('time.time', mock.MagicMock(return_value=12345))
def test_magic_calculation_valid():
    result = magic_calculation("test", 1)
    assert result == MagicCalculationResult("test", 2)


def test_magic_calculation_invalid():
    result = magic_calculation("test", 0)
    assert result is None
