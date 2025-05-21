# This is a problem given by Leetcode.com
# https://leetcode.com/problems/sort-the-jumbled-numbers/description

from unittest import TestCase, main

MAPPING_LEN: int = 10
NUM_LIMIT: int = 10 ** 9  # 0 <= nums[i] < 109
MAX_NNUMS: int = 3 * 104


class Solution:
    """ You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system.
        mapping[i] = j means digit i should be mapped to digit j in this system.

        The mapped value of an integer is the new integer obtained by replacing each occurrence of
        digit i in the integer with mapping[i] for all 0 <= i <= 9.

        You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements.

        Notes:

        Elements with the same mapped values should appear in the same relative order as in the input.
        The elements of nums should only be sorted based on their mapped values and not be replaced by them.
        Constraints:

        - mapping.length == 10
        - 0 <= mapping[i] <= 9
        - All the values of mapping[i] are unique.
        - 1 <= nums.length <= 3 * 104
        - 0 <= nums[i] < 109
    """

    def sort_jumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        """ Sorts a list of integers based on a custom digit mapping.

            This method takes a list of integers and sorts them according to a provided
            digit mapping. Each digit of the integers in `nums` is mapped to a new digit
            as specified in the `mapping` list, and the integers are sorted based on their
            mapped values.

            Args:
                mapping (list[int]): A list of 10 integers where each integer is between 0 and 9, inclusive.
                                    This list represents the mapping of digits 0 through 9 to new values.
                                    For example, if mapping[2] = 5, then the digit '2' will be considered as '5'.
                nums (list[int]): A list of integers to be sorted. Each integer must be within a predefined limit.

            Returns:
                list[int]: The sorted list of integers based on the custom digit mapping.

            Raises:
                ValueError: If `mapping` does not contain exactly 10 integers between 0 and 9 inclusive.
                ValueError: If `nums` contains elements that are not integers or are out of the allowed range.

            Example:
                >>> mapping = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                >>> nums = [123, 456, 789]
                >>> sorted_nums = sort_jumbled(mapping, nums)
                >>> print(sorted_nums)
                [123, 456, 789]  # The result will vary based on the provided mapping.
        """
        if len(mapping) != 10 or not all([isinstance(x, int) and x in range(10) for x in mapping]) or len(nums) != len(set(nums)):
            raise ValueError("mapping is invalid. mapping must contain 10 unique values between 0 and 9 included.")
        if not all([isinstance(num, int) and num in range(NUM_LIMIT) for num in nums]):
            raise ValueError('nums must be a list of integers.')
        if not 1 <= len(nums) <= MAX_NNUMS:
            raise ValueError(f"nums exceeds the max limit of values of: {MAX_NNUMS}")

        nums.sort(key=lambda x: self._map_value(mapping, x))

        return nums

    def _map_value(self, mapping: list[int], value: int | str) -> int:
        """ Returns the mapped value of a given integer or string representation of an integer.

            This method takes an integer or a string representation of an integer and maps each
            of its digits to new values based on the provided `mapping` list. The mapped digits
            are then combined to form a new integer, which is returned.

            Args:
                mapping (list[int]): A list of 10 integers where each integer is between 0 and 9, inclusive.
                                    This list represents the mapping of digits 0 through 9 to new values.
                                    For example, if mapping[2] = 5, then the digit '2' will be considered as '5'.
                value (int | str): An integer or a string representation of an integer whose digits are to be mapped.

            Returns:
                int: The new integer formed by mapping each digit of the input value according to the provided mapping.

            Example:
                >>> mapping = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
                >>> value = 123
                >>> mapped_value = self._map_value(mapping, value)
                >>> print(mapped_value)
                876  # Digits 1, 2, 3 are mapped to 8, 7, 6 respectively.
        """
        new_value: str = ""
        str_number: str = str(value) if isinstance(value, int) else value

        for digit in str_number:
            new_value += str(mapping[int(digit)])

        return int(new_value)


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_case_1(self) -> None:
        mapping: list[int] = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
        nums: list[int] = [991, 338, 38]
        self.assertEqual(self.solution.sort_jumbled(mapping=mapping, nums=nums), [338, 38, 991])

    def test_case_2(self) -> None:
        mapping: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        nums: list[int] = [789, 456, 123]
        self.assertEqual(self.solution.sort_jumbled(mapping=mapping, nums=nums), [123, 456, 789])

    def test_map_value_case_1(self) -> None:
        mapping: list[int] = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]

        for digit in range(10):
            self.assertEqual(self.solution._map_value(mapping=mapping, value=digit), mapping[digit])

    def test_map_value_case_2(self) -> None:
        mapping: list[int] = [2, 9, 0, 5, 6, 3, 7, 4, 1, 8]

        for digit in range(10):
            # try sending str as value
            self.assertEqual(self.solution._map_value(mapping=mapping, value=str(digit)), mapping[digit])


if __name__ == "__main__":
    main()
