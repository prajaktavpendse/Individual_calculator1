import unittest
import scalculator


class Unit_Test(unittest.TestCase):
    def test_add(self):
        test_cases = Unit_Test.get_test_cases_from_file("UnitTestAddition.csv")

        for test in test_cases:
            print("Running addition test case: {}".format(test))
            self.assertEqual(test[2], scalculator.Calculator.addition([test[0], test[1]]))

    def test_sub(self):
        test_cases = Unit_Test.get_test_cases_from_file("UnitTestSubtraction.csv")

        for test in test_cases:
            print("Running subtraction test case: {}".format(test))
            self.assertEqual(test[2], scalculator.Calculator.subtraction(test[0], test[1]))



    @staticmethod
    def get_test_cases_from_file(file_name):
        results_list = []
        with open(file_name, "r") as file:
            header = file.readline()

            new_line = file.readline()

            while new_line:
                tokens = new_line.split(",")
                num1 = float(tokens[0])
                num2 = float(tokens[1])
                expected_result = float(tokens[2])
                results_list.append([num1, num2, expected_result])

                new_line = file.readline()
        return results_list


if __name__== "__main__":
    unittest.main()


