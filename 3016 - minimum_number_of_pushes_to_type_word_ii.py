# This is a problem given by Leetcode.com
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description

from unittest import TestCase, main
from collections import Counter


class Solution:
    """ You are given a string word containing lowercase English letters. Telephone keypads have keys mapped with distinct collections
    of lowercase English letters, which can be used to form words by pushing them.

    For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

    It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters.
    The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key.
    You need to find the minimum number of times the keys will be pushed to type the string word.

    Return the minimum number of pushes needed to type word after remapping the keys.

    An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.
    """

    def minimum_pushes(self, word: str) -> int:
        if not word:
            raise ValueError("word must be a string with at least 1 char.")

        if len(set(word)) <= 8:
            return len(word)

        mapping = Counter(word).most_common()
        min_pushes: int = 0

        for i, letter in enumerate(mapping):
            min_pushes += letter[1]*((i // 8)+1)

        return min_pushes


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_minimum_pushes_valid_case(self) -> None:
        case_0 = "abcdefgh"
        self.assertEqual(self.solution.minimum_pushes(case_0), 8)
        case_1 = "xyzxyzxyzxyz"
        self.assertEqual(self.solution.minimum_pushes(case_1), 12)
        case_2 = "aabbccddeeffgghhiiiiii"
        self.assertEqual(self.solution.minimum_pushes(case_2), 24)
        case_3 = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(self.solution.minimum_pushes(case_3), 56)


if __name__ == "__main__":
    main()
