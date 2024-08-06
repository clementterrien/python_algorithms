# This is a problem given by Leetcode.com
# https://leetcode.com/problems/longest-palindromic-substring/

from unittest import TestCase, main


class Solution:
    
    def longest_palindrome(self, string: str) -> str:
        if not string:
            return ""
        if string == string[::-1]:
            return string
        
        longest: str = string[0]

        for i in range(len(string)):
            for y in range(i+1, len(string)+1):
                sub = string[i:y]
                if sub == sub[::-1] and len(sub) > len(longest):
                    longest = sub
            
        return longest
    
    
class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_longest_palindrome_valid_case(self) -> None:
        case_0: str = 'kayak'
        self.assertEqual(self.solution.longest_palindrome(case_0), "kayak")
        case_1: str = 'abcneveroddorevenxyz'
        self.assertEqual(self.solution.longest_palindrome(case_1), "neveroddoreven")
        case_2: str = 'babad'
        self.assertEqual(self.solution.longest_palindrome(case_2), "bab")
        case_3: str = 'cbbd'
        self.assertEqual(self.solution.longest_palindrome(case_3), "bb")
        case_4: str = 'abb'
        self.assertEqual(self.solution.longest_palindrome(case_4), "bb")

if __name__ == "__main__":
    main()
