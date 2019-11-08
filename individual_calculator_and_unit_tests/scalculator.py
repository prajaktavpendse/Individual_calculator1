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

    def process_input_data(self, input_str, parse_operation_func=None):
        if not parse_operation_func:
            parse_operation_func = Calculator.get_operation
        input_data = self.parse_interactive_mode_input(input_str, parse_operation_func)
        if not input_data:
            raise ValueError("You entered invalid data!")
        return input_data

    def start_interactive_calculator(self):
        print("Welcome to the interactive mode\n "
              "Example usage:\n"
              "(1) num1 num2 ... numN ADD\n"
              "(2) num1 num2 SUBTRACT\n"
              "(3) num1 num2 ... numN MULTIPLY\n"
              "(4) num1 num2 DIVISION\n"
              "(5) num1 SQUARE\n"
              "(6) num1 SQRT\n"
              "(7) Use res to use results of computations till now\n"
              "Example: res ADD 5\n"
              "Hit Enter to display result and exit")

        input_str = input("Enter input: ")
        while input_str:
            input_data = self.process_input_data(input_str)
            self.result = Calculator.dispatch_and_compute_result(input_data[0], input_data[1])
            input_str = input("Enter input: ")
        print("Result: {}".format(self.result))

    @staticmethod
    def addition(nums):
        return sum(nums)

    @staticmethod
    def subtraction(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplication(nums):
        product = 1
        for num in nums:
            product = product * num
        return product

    @staticmethod
    def division(num1, num2):
        return num1 / num2

    @staticmethod
    def square(num1):
        return pow(num1, 2)

    @staticmethod
    def square_root(num1):
        if num1 < 0:
            raise ValueError("Invalid number")
        return math.sqrt(num1)

    @staticmethod
    def get_operation(operation):
        if not isinstance(operation, str):
            print("Supported operations are: Add, Subtract, Multiply, Divide, Square, Square root")

        operation = operation.upper()

        if "ADD" in operation:
            return Calculator.Operation.ADD
        elif "SUB" in operation:
            return Calculator.Operation.SUBTRACT
        elif "MUL" in operation:
            return Calculator.Operation.MULTIPLY
        elif "DIV" in operation:
            return Calculator.Operation.DIVIDE
        elif "SQUARE" in operation:
            return Calculator.Operation.SQUARE
        elif "SQRT" in operation:
            return Calculator.Operation.SQUARE_ROOT

        else:
            return Calculator.Operation.UNKNOWN


if __name__ == '__main__':
    calculator = Calculator()
    calculator.start_interactive_calculator()