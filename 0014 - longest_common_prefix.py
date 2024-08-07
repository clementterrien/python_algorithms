# This is a problem given by Leetcode.com
# https://leetcode.com/problems/longest-common-prefix/description/

from unittest import TestCase, main


class Solution:

    def longest_common_prefix(self, strs: list[str]) -> str:
        """ Find the longest common prefix string amongst an array of strings.

        This method takes a list of strings and returns the longest common prefix
        that is shared among all the strings. If there is no common prefix, an
        empty string is returned.

        Args:
            strs (list[str]): A list of strings to be analyzed.

        Returns:
            str: The longest common prefix shared by all the strings in the list.

        Raises:
            ValueError: If the input list is empty or not containing only strings.
        """
        if not strs or any([not isinstance(x, str) for x in strs]):
            raise ValueError("strs must be a list of strings.")

        strs.sort(key=len)

        longest: str = ""

        for i, char in enumerate(strs[0]):

            if all([x[i] == char for x in strs[1:]]):
                longest += char
            else:
                break

        return longest


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_longest_common_prefix_valid_case(self) -> None:
        case_1: list[str] = ["flower", "flow", "flight"]
        self.assertEqual(self.solution.longest_common_prefix(case_1), 'fl')
        case_2: list[str] = ["cir", "car"]
        self.assertEqual(self.solution.longest_common_prefix(case_2), 'c')

    def test_longest_common_prefix_invalid_case(self) -> None:
        case_1: list[str | int] = ["flower", "flow", 1]
        with self.assertRaises(ValueError) as captured:
            self.solution.longest_common_prefix(case_1)  # type: ignore

        self.assertEqual(str(captured.exception), "strs must be a list of strings.")

        case_2: list = []
        with self.assertRaises(ValueError) as captured:
            self.solution.longest_common_prefix(case_2)  # type: ignore

        self.assertEqual(str(captured.exception), "strs must be a list of strings.")


if __name__ == "__main__":
    main()
