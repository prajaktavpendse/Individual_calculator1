import unittest
import scalculator
import math

class Unit_Test(unittest.TestCase):
    def test_add(self):
        test_cases = Unit_Test.get_test_cases_from_file("../csv_files/UnitTestAddition.csv")

        for test in test_cases:
            print("Running addition test case: {}".format(test))
            self.assertEqual(test[2], scalculator.Calculator.addition([test[0], test[1]]))

    def test_subtraction(self):
        test_cases = Unit_Test.get_test_cases_from_file("../csv_files/UnitTestSubtraction.csv")

        for test in test_cases:
            print("Running subtraction test case: {}".format(test))
            self.assertEqual(test[2], scalculator.Calculator.subtraction(test[1], test[0]))

    def test_division(self):
        test_cases = Unit_Test.get_test_cases_from_file("../csv_files/UnitTestDivision.csv")

        for test in test_cases:
            print("Running division test case: {}".format(test))
            self.assertTrue(math.fabs(test[2] - scalculator.Calculator.division(test[1], test[0])) <= 0.001)

    def test_multiplication(self):
        test_cases = Unit_Test.get_test_cases_from_file("../csv_files/UnitTestMultiplication.csv")

        for test in test_cases:
            print("Running multiplication test case: {}".format(test))
            self.assertEqual(test[2], scalculator.Calculator.multiplication([test[1], test[0]]))

    def test_square(self):
        test_cases = Unit_Test.get_test_cases_from_file("../csv_files/UnitTestSquare.csv")

        for test in test_cases:
            print("Running square test case: {}".format(test))
            self.assertEqual(test[1], scalculator.Calculator.square(test[0]))

    def test_square_root(self):
        test_cases = Unit_Test.get_test_cases_from_file("../csv_files/UnitTestSquareRoot.csv")

        for test in test_cases:
            print("Running square root test case: {}".format(test))
            self.assertTrue(math.fabs(test[1] - scalculator.Calculator.square_root(test[0])) <= 0.001)

    def test_process_input_data(self):
        calculator = scalculator.Calculator()
        self.assertTrue(math.isnan(calculator.result))

        result_list = calculator.process_input_data("1 2 3 4 5 ADD")
        self.assertEqual(result_list, [scalculator.Calculator.Operation.ADD, [1, 2, 3, 4, 5]])

        result_list = calculator.process_input_data("1 2 DIVISION")
        self.assertEqual(result_list, [scalculator.Calculator.Operation.DIVIDE, [1, 2]])

    def test_dispatch_and_compute_result(self):
        result = scalculator.Calculator.dispatch_and_compute_result(scalculator.Calculator.Operation.ADD, [1,2,3])
        self.assertEqual(result, 6)

        # Should ignore the remaining numbers after the first two
        result = scalculator.Calculator.dispatch_and_compute_result(scalculator.Calculator.Operation.SUBTRACT, [2, 1, 3, 4, 5])
        self.assertEqual(result, 1)

    @staticmethod
    def get_test_cases_from_file(file_name):
        results_list = []
        with open(file_name, "r") as file:
            # Do this to ignore the header
            header = file.readline()

            new_line = file.readline()

            while new_line:
                tokens = new_line.split(",")
                results_list.append([float(t) for t in tokens[:-1]])

                new_line = file.readline()
        return results_list


if __name__== "__main__":
    unittest.main()


