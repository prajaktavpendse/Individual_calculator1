import sys
from enum import Enum
import argparse
import math
from math import pow


class Calculator:
    class Operation(Enum):
        ADD = 1,
        SUBTRACT = 2,
        MULTIPLY = 3,
        DIVIDE = 4,
        SQUARE = 5,
        SQUARE_ROOT = 6,
        UNKNOWN = 7000

    def __init__(self):
        self.result = float("nan")

    @staticmethod
    def open_file_and_iterate_per_line(file_name, separator, skip_header=False):
        with open(file_name, "r") as file:
            line_str = file.readline()

            if not line_str:
                yield list()
                return

            if skip_header:
                line_str = file.readline()

            while line_str:
                values = line_str.split(separator)
                yield values

                line_str = file.readline()

    @staticmethod
    def dispatch_and_compute_result(operation, nums):
        if isinstance(operation, str):
            operation = Calculator.get_operation(operation)

        if operation == Calculator.Operation.ADD:
            return Calculator.addition(nums)
        elif operation == Calculator.Operation.SUBTRACT:
            return Calculator.subtraction(nums[0], nums[1])
        elif operation == Calculator.Operation.MULTIPLY:
            return Calculator.multiplication(nums)
        elif operation == Calculator.Operation.DIVIDE:
            return Calculator.division(nums[0], nums[1])
        elif operation == Calculator.Operation.SQUARE:
            return Calculator.square(nums[0])
        elif operation == Calculator.Operation.SQUARE_ROOT:
            return Calculator.square_root(nums[0])