# This is a problem given by Leetcode.com
# https://leetcode.com/problems/two-sum/description/

from unittest import TestCase, main


class Solution:

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """ Find two numbers in a list that add up to a specific target.

            This method takes a list of integers and a target integer.
            It searches fortwo distinct indices in the list such that
            the numbers at those indices add up to the target.
            If such a pair is found, it returns the indices as a list.
            If no such pair exists, it raises a ValueError.

            Args:
                nums (list[int]): A list of integers to search within.
                target (int): The target sum we are looking for.

            Returns:
                list[int]: A list containing the two indices of the numbers
                that add up to the target. The first index is smaller than
                the second index.

            Raises:
                ValueError: If no two numbers add up to the target.

            Example:
                >>> solution = Solution()
                >>> solution.two_sum([2, 7, 11, 15], 9)
                [0, 1]
            """
        n_nums: int = len(nums)

        for i in range(n_nums):
            y = i + 1
            for a in list(range(n_nums))[y:n_nums]:
                if nums[i] + nums[a] == target:
                    return [i, a]

        raise ValueError('Given nums have no solutions.')


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_two_sums_case_1(self) -> None:
        case_1: list[int] = [2, 7, 11, 15]
        target: int = 9
        self.assertEqual(self.solution.two_sum(nums=case_1, target=target), [0, 1])

    def test_two_sums_case_2(self) -> None:
        case_2: list[int] = [3, 2, 4]
        target: int = 6
        self.assertEqual(self.solution.two_sum(nums=case_2, target=target), [1, 2])

    def test_two_sums_case_3(self) -> None:
        case_3: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 48, 56]
        target: int = 104
        self.assertEqual(self.solution.two_sum(nums=case_3, target=target), [15, 16])

    def test_two_sums_raises_error_with_no_solution(self) -> None:
        invalid_case: list[int] = [1, 2, 3, 4, 42]
        target: int = 104
        with self.assertRaises(ValueError):
            self.solution.two_sum(nums=invalid_case, target=target)


if __name__ == "__main__":
    main()
