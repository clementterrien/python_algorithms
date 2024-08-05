# This is a problem given by Leetcode.com
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from unittest import TestCase, main


class Solution:
    
    def length_of_longest_substring(self, string: str) -> int:
        """ Returns the length of the longest substring without repeating characters.

            This method uses a sliding window technique to find the longest substring
            without repeating characters in a given input string. It maintains a set
            to keep track of characters in the current window and adjusts the window
            size dynamically to ensure no characters are repeated within the window.

            Args:
                string (str): The input string to analyze.

            Returns:
                int: The length of the longest substring without repeating characters.
        """
        if not string:
            return 0
        
        char_set: set = set()
        left: int = 0
        max_length: int = 0

        for right in range(len(string)):
            while string[right] in char_set:
                char_set.remove(string[left])
                left += 1
            char_set.add(string[right])
            max_length = max(max_length, right - left + 1)

        return max_length


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_length_of_longest_substring_valid_case(self) -> None:
        case_0: str = ""
        self.assertEqual(self.solution.length_of_longest_substring(case_0), 0)
        
        case_1: str = "a"
        self.assertEqual(self.solution.length_of_longest_substring(case_1), 1)
        
        case_2: str = "abcabcbb"
        self.assertEqual(self.solution.length_of_longest_substring(case_2), 3)

        case_3: str = "bbbbb"
        self.assertEqual(self.solution.length_of_longest_substring(case_3), 1)
        
        case_4: str = "pwwkew"
        self.assertEqual(self.solution.length_of_longest_substring(case_4), 3)

        case_5: str = "abcdefgh"
        self.assertEqual(self.solution.length_of_longest_substring(case_5), 8)

if __name__ == "__main__":
    main()
