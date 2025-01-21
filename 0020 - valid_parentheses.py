# This is a problem given by Leetcode.com
# https://leetcode.com/problems/valid-parentheses/description/

from unittest import TestCase, main


class Solution:

    char_map: dict[str, str] = {'(': ')', '{': '}', '[': ']'}

    def is_valid(self, string_to_check: str) -> bool:
        """ Validates whether a given string has properly matched and nested opening and closing characters.

            Args:
                string_to_check (str): The input string to validate. It should consist of characters
                                    defined in `self.char_map` (keys) as opening characters and
                                    `self.char_map.values()` as corresponding closing characters.

            Returns:
                bool:
                    - `True` if the string is valid (i.e., all opening characters have matching
                    closing characters in the correct order and properly nested).
                    - `False` otherwise.

            Raises:
                None explicitly, but will return `False` for invalid input strings that:
                    - Are empty.
                    - Start with a character not in `self.char_map`.
                    - Contain characters that are neither in `self.char_map` nor its values.

            Example:
                Assume `self.char_map` is defined as:
                    self.char_map = {'(': ')', '{': '}', '[': ']'}

                - `is_valid("(){}[]")` -> True
                - `is_valid("(]")` -> False
                - `is_valid("([{}])")` -> True
                - `is_valid("")` -> False
                - `is_valid("abc")` -> False

            Notes:
                - This method assumes `self.char_map` is a dictionary mapping opening characters
                to their respective closing characters (e.g., {'(': ')', '{': '}', '[': ']'}).
                - The method uses a stack to ensure that opening characters are matched correctly
                with their corresponding closing characters.
        """
        if not isinstance(string_to_check, str) or not string_to_check or string_to_check[0] not in self.char_map:
            raise ValueError("The input string to check is not valid. It must be an str starting with an opening char ('(', '{', '[')")

        stack: list[str] = [string_to_check[0]]

        for char in string_to_check[1:]:
            if char in self.char_map:
                stack.append(char)
            elif char in list(self.char_map.values()):
                if not stack or not self._is_closing(stack, char):
                    return False
                stack.pop(-1)
            else:
                return False

        return stack == []

    def _is_closing(self, stack: list[str], char: str) -> bool:
        return self.char_map[stack[-1]] == char


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_is_valid_valid_case(self) -> None:
        # Case True
        case_1: str = "()"
        self.assertTrue(self.solution.is_valid(case_1))
        case_2: str = "(())"
        self.assertTrue(self.solution.is_valid(case_2))
        case_3: str = "({})"
        self.assertTrue(self.solution.is_valid(case_3))
        case_4: str = "(){}"
        self.assertTrue(self.solution.is_valid(case_4))
        case_5: str = "()[]{}"
        self.assertTrue(self.solution.is_valid(case_5))

        # Case False
        case_6: str = "(}"
        self.assertFalse(self.solution.is_valid(case_6))
        case_7: str = "(}"
        self.assertFalse(self.solution.is_valid(case_7))

    def test_is_valid_with_invalid_input(self):
        invalid_case: str = ""
        with self.assertRaises(ValueError):
            self.solution.is_valid(invalid_case)

        invalid_case = "hello"
        with self.assertRaises(ValueError):
            self.solution.is_valid(invalid_case)

        invalid_case: int = 6
        with self.assertRaises(ValueError):
            self.solution.is_valid(invalid_case)

    def test_is_closing(self) -> None:
        stack, closing = (['('], ')')
        self.assertTrue(self.solution._is_closing(stack, closing))
        stack, closing = (['(', '('], ')')
        self.assertTrue(self.solution._is_closing(stack, closing))
        stack, closing = (['{'], '}')
        self.assertTrue(self.solution._is_closing(stack, closing))
        stack, closing = (['['], ']')
        self.assertTrue(self.solution._is_closing(stack, closing))
        stack, closing = (['('], '}')
        self.assertFalse(self.solution._is_closing(stack, closing))


if __name__ == "__main__":
    main()
