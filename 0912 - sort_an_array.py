# This is a problem given by Leetcode.com
# https://leetcode.com/problems/sort-an-array/description

from unittest import TestCase, main


class Solution:
    """ Given an array of integers nums, sort the array in ascending order and return it.

        You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
    """

    def sort_array(self, nums: list[int], is_first_call: bool = True) -> list[int]:
        """ Sorts an array of integers in ascending order using the merge sort algorithm.

        Args:
            nums (list[int]): The list of integers to be sorted.
            is_first_call (bool): Indicates if this is the first call to the method.

        Returns:
            list[int]: The sorted list of integers in ascending order.

        Raises:
            ValueError: If nums is not an array of integers with at least two integers.

        Example:
            >>> sol = Solution()
            >>> sol.sort_array([5, 2, 3, 1])
            [1, 2, 3, 5]
        """
        if is_first_call and (len(nums) < 2 or not all(isinstance(x, int) for x in nums)):
            raise ValueError("nums must be an array of integers with at least two integers.")

        if len(nums) <= 1:
            return nums

        divider: int = len(nums) // 2
        left_part: list[int] = nums[:divider]
        right_part: list[int] = nums[divider:]

        self.sort_array(left_part, is_first_call=False)
        self.sort_array(right_part, is_first_call=False)

        l: int = 0
        r: int = 0
        i: int = 0

        while l < len(left_part) and r < len(right_part):
            if left_part[l] < right_part[r]:
                nums[i] = left_part[l]
                l += 1
            else:
                nums[i] = right_part[r]
                r += 1
            i += 1

        while l < len(left_part):
            nums[i] = left_part[l]
            l += 1
            i += 1

        while r < len(right_part):
            nums[i] = right_part[r]
            r += 1
            i += 1

        return nums


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_sort_array_valid_cases(self) -> None:
        case: list[int] = [1, 2, 3]
        self.assertEqual(self.solution.sort_array(case), [1, 2, 3])

        case = [10, 20, 30]
        self.assertEqual(self.solution.sort_array(case), [10, 20, 30])

        case = [8, 5, 9, 4, 6, 8, 1, 0, 3, 2, 1, 5, 4]
        self.assertEqual(self.solution.sort_array(case), [0, 1, 1, 2, 3, 4, 4, 5, 5, 6, 8, 8, 9])

    def test_sort_array_raises_error_with_invalid_nums(self) -> None:
        invalid_case_1 = [0]
        with self.assertRaises(ValueError) as captured:
            self.solution.sort_array(invalid_case_1)  # type: ignore
        self.assertEqual(str(captured.exception), "nums must be an array of integers with at least two integers.")

        invalid_case_2 = ['str', 'str']
        with self.assertRaises(ValueError) as captured:
            self.solution.sort_array(invalid_case_2)  # type: ignore
        self.assertEqual(str(captured.exception), "nums must be an array of integers with at least two integers.")


if __name__ == "__main__":
    main()
