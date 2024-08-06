# This is a problem given by Leetcode.com
# https://leetcode.com/problems/palindrome-number/description/

from unittest import TestCase, main


class Solution:
    """Given an integer x, return true if x is a palindrome, and false otherwise."""

    def is_palindrome(self, x: int) -> bool:
        """ Determine whether an integer is a palindrome.

            A palindrome is a number that reads the same backward as forward. This method
            checks if the given integer is a palindrome by converting it to a string and 
            comparing the string to its reversed version.

            Args:
                x (int): The integer to be checked.

            Returns:
                bool: True if the integer is a palindrome, False otherwise.
        """
        if x < 0:
            return False
        if x < 10:
            return True

        return str(x) == str(x)[::-1]


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_is_palindrome_valid_case(self) -> None:
        case_0: int = 0
        self.assertTrue(self.solution.is_palindrome(case_0))
        case_1: int = 1
        self.assertTrue(self.solution.is_palindrome(case_1))
        case_2: int = -1
        self.assertFalse(self.solution.is_palindrome(case_2))
        case_3: int = 11
        self.assertTrue(self.solution.is_palindrome(case_3))
        case_4: int = -11
        self.assertFalse(self.solution.is_palindrome(case_4))
        case_5: int = 101
        self.assertTrue(self.solution.is_palindrome(case_5))
        case_6: int = 11011
        self.assertTrue(self.solution.is_palindrome(case_6))
        case_7: int = 235606532
        self.assertTrue(self.solution.is_palindrome(case_7))


if __name__ == "__main__":
    main()
