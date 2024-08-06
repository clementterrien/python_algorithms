from unittest import TestCase, main
from collections import Counter


class Solution:

    def frequency_sort(self, nums: list[int]) -> list[int]:
        """ Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
            If multiple values have the same frequency, sort them in decreasing order.

            Return the sorted array.

            Args:
                nums (list[int]): The array of integers to sort by increasing frequency where:
                        - 1 <= nums.length <= 100
                        -100 <= nums[i] <= 100

            Returns:
                list[int]: The sorted by increasing frequency array.
        """
        if not all([isinstance(x, int) for x in nums]):
            raise ValueError("nums must be an array of integers.")

        counts = Counter(nums)
        nums.sort(key=lambda x: (counts[x], -x))
        return nums


class TestSolution(TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_frequency_sort_valid_case(self) -> None:
        valid_case: list[int] = [1, 1, 2, 2, 2, 3]
        self.assertEqual(self.solution.frequency_sort(valid_case), [3, 1, 1, 2, 2, 2])

        valid_case = [2, 3, 1, 3, 2]
        self.assertEqual(self.solution.frequency_sort(valid_case), [1, 3, 3, 2, 2])

        valid_case = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
        self.assertEqual(self.solution.frequency_sort(valid_case), [5, -1, 4, 4, -6, -6, 1, 1, 1])

    def test_frequency_raises_error_with_invalid_value(self) -> None:
        invalid_case_1: list[str] = ["str", "str"]

        with self.assertRaises(ValueError) as captured:
            self.solution.frequency_sort(nums=invalid_case_1)  # type: ignore
        self.assertEqual(str(captured.exception), "nums must be an array of integers.")


if __name__ == "__main__":
    main()
