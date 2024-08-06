# This is a problem given by Leetcode.com
# https://leetcode.com/problems/roman-to-integer/description/

from unittest import TestCase, main


class Solution:

    MAPPING: dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def roman_to_int(self, roman_str: str) -> int:
        """ Convert a Roman numeral to an integer.

            This method converts a string representing a Roman numeral to its corresponding
            integer value. It uses a predefined mapping of Roman numerals to their integer
            values and processes the string from left to right, accounting for the subtractive
            notation used in Roman numerals.

            Args:
                roman_str (str): The Roman numeral string to be converted.

            Returns:
                int: The integer value of the given Roman numeral.

            Raises:
                ValueError: If the input is not a valid Roman numeral string.
        """
        if not isinstance(roman_str, str) or any([char not in self.MAPPING for char in roman_str]):
            raise ValueError('invalid roman_str given.')

        result: int = 0
        previous: int = 0

        for char in roman_str[::-1]:
            value = self.MAPPING[char]
            if previous > value:
                result -= value
            else:
                result += value
            previous = value

        return result


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_roman_to_int_valid_case(self) -> None:
        case_0: str = "III"
        self.assertEqual(self.solution.roman_to_int(case_0), 3)
        case_1: str = "IV"
        self.assertEqual(self.solution.roman_to_int(case_1), 4)
        case_2: str = "VI"
        self.assertEqual(self.solution.roman_to_int(case_2), 6)
        case_3: str = "IX"
        self.assertEqual(self.solution.roman_to_int(case_3), 9)
        case_4: str = "LVIII"
        self.assertEqual(self.solution.roman_to_int(case_4), 58)
        case_5: str = "MCMXCIV"
        self.assertEqual(self.solution.roman_to_int(case_5), 1994)

    def test_roman_to_int_raises_value_error_with_invalid_roman_str(self) -> None:
        case_0: str = "not"
        with self.assertRaises(ValueError) as captured:
            self.solution.roman_to_int(case_0)
        self.assertEqual(str(captured.exception), "invalid roman_str given.")

        case_1: int = 1
        with self.assertRaises(ValueError) as captured:
            self.solution.roman_to_int(case_1)
        self.assertEqual(str(captured.exception), "invalid roman_str given.")


if __name__ == "__main__":
    main()
