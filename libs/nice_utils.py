import time


class MagicCalculationResult:
    name: str
    result: int
    calculation_timestamp: float

    def __init__(self, name, calculation):
        self.name = name
        self.result = calculation
        self.calculation_timestamp = time.time()

    # We need to implement the eq method also if we don't really need it,
    # because it's required to simplify the unit tests
    def __eq__(self, other):
        return self.name == other.name and self.result == other.result and \
            self.calculation_timestamp == other.calculation_timestamp


def magic_calculation(name: str, counter: int) -> MagicCalculationResult:
    if counter > 0:
        return MagicCalculationResult(name, counter + 1)
