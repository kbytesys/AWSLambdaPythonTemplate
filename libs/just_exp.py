from libs.nice_utils import magic_calculation, MagicCalculationResult


def business_demo(name: str) -> MagicCalculationResult | None:
    calculation = magic_calculation(name, 1)

    if calculation and calculation.result > 1:
        return calculation
