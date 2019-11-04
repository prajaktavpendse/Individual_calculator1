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

        # Applies the given operation for each line of the file
        def load_from_file_and_compute(self, file_name, separator, operation_str, is_header_available=False):
            operation = Calculator.get_operation(operation_str)
            if operation is Calculator.Operation.UNKNOWN:
                print("Invalid operation")
                exit(-1)

            for values_list in Calculator.open_file_and_iterate_per_line(file_name, separator, is_header_available):
                if not values_list:
                    continue

                values_list = [self.parse_number(str(v), False) for v in values_list]

                if any([math.isnan(x) for x in values_list]):
                    print("Invalid inputs detected, skipping this line")
                    continue

                self.result = values_list[0]

                for num in range(1, len(values_list)):
                    actual_num = values_list[num]
                    self.result = Calculator.dispatch_and_compute_result(self.result, actual_num)

                # Print the value
                print("Numbers: {}, result: {}".format(values_list, self.result))

        def parse_number(self, numberStr, allow_res=True):
            if numberStr == "res" and allow_res:
                return self.result
            else:
                try:
                    if "." in numberStr:
                        return float(numberStr)
                    else:
                        return int(numberStr)
                except:
                    return float("nan")

        def parse_interactive_mode_input(self, inputStr, get_oper_function):
            tokens = inputStr.split()
            if len(tokens) < 2:
                return []
            else:
                operationn = get_oper_function(tokens[-1])
                nums = [self.parse_number(n) for n in tokens[:-1]]

            for num in nums:
                if math.isnan(num):
                    return []

            return [operationn, nums]
