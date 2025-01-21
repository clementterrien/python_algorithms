# This is a problem given by Leetcode.com
# https://leetcode.com/problems/merge-two-sorted-lists/description/

from unittest import TestCase, main

from utils.list_node import ListNode


ListNode.min_val = -100
ListNode.max_val = 100


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
