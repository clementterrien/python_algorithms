# This is a problem given by Leetcode.com
# https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Any, Generator
from unittest import TestCase, main


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, list):
            return super().__eq__(value)
        else:
            return list(self) == value

    def __iter__(self) -> Generator[int, Any, None]:
        current = self
        while current:
            yield current.val
            current = current.next

    def __repr__(self) -> str:
        return str(self.val)

    def generate_list_node_from_int_list(self, nums: list[int]) -> "ListNode":
        """ Generates a linked list from a given list of integers, using the current `ListNode` as the head.

            Args:
                nums (list[int]): A list of integers to populate the linked list. The first integer
                                will be assigned to the current node (`self`), and subsequent integers
                                will form the rest of the linked list.

            Returns:
                ListNode: The head of the constructed linked list (i.e., the current node `self`).

            Example:
                If `nums = [1, 2, 3]` and the current `ListNode` is the head:

                Initial state:
                    self = ListNode(val=0)

                After calling `generate_list_node_from_int_list(nums)`:
                    self = ListNode(val=1) -> ListNode(val=2) -> ListNode(val=3)

            Notes:
                - The method modifies the `self` node and appends new nodes to it.
                - Assumes that `nums` is not empty. If `nums` is empty, it will raise an `IndexError`
                when trying to access `nums[0]`.
                - The resulting linked list will follow the order of integers in `nums`.

            Raises:
                ValueError: If given nums is empty or contains non integer elements.
        """
        if not isinstance(nums, list) and not all([isinstance(x, int) for x in nums]):
            raise ValueError("nums must be a list of integers.")
        if not nums:
            raise ValueError("nums can't be empty.")

        current = self
        self.val = nums[0]

        for num in nums[1:]:
            current.next = ListNode(val=num)
            current = current.next

        return self


class Solution:

    def merge_two_lists(self, list_node_1: ListNode, list_node_2: ListNode) -> ListNode:

        first: ListNode = ListNode(0)
        current: ListNode = first

        current_1: ListNode = list_node_1
        current_2: ListNode = list_node_2

        while current_1 and current_2:

            if current_1.val < current_2.val:
                current.next = current_1
                current_1 = current_1.next

            else:
                current.next = current_2
                current_2 = current_2.next

            current = current.next

        if current_1:
            current.next = current_1
        if current_2:
            current.next = current_2

        return first.next


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.list_node = ListNode()

    def test_merge_two_lists_valid_case(self) -> None:
        list_1: ListNode = ListNode().generate_list_node_from_int_list([1, 2, 4])
        list_2: ListNode = ListNode().generate_list_node_from_int_list([1, 3, 4])

        self.assertEqual(self.solution.merge_two_lists(list_1, list_2), [1, 1, 2, 3, 4, 4])

        list_1 = ListNode().generate_list_node_from_int_list([0, 2, 4, 6, 8])
        list_2 = ListNode().generate_list_node_from_int_list([1, 3, 5, 7, 9])

        self.assertEqual(self.solution.merge_two_lists(list_1, list_2), list(range(10)))


if __name__ == "__main__":
    main()
