# This is a problem given by Leetcode.com
# https://leetcode.com/problems/add-two-numbers/description/

from unittest import TestCase, main

from utils.list_node import ListNode


ListNode.min_val = 0
ListNode.max_val = 9


class Solution:

    def add_two_numbers(self, linked_list_1: ListNode, linked_list_2: ListNode) -> ListNode:
        sum_result: int = linked_list_1.to_integer() + linked_list_2.to_integer()
        return ListNode().generate_list_node_from_int_list([int(x) for x in reversed(str(sum_result))])


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_add_two_numbers_case_1(self) -> None:
        first_list: list[int] = [2, 4, 3]
        list_node_1: ListNode = ListNode().generate_list_node_from_int_list(first_list)
        second_list: list[int] = [5, 6, 4]
        list_node_2: ListNode = ListNode().generate_list_node_from_int_list(second_list)
        self.assertEqual(self.solution.add_two_numbers(linked_list_1=list_node_1, linked_list_2=list_node_2), [7, 0, 8])

    def test_add_two_numbers_case_2(self) -> None:
        first_list: list[int] = [0]
        list_node_1 = ListNode().generate_list_node_from_int_list(first_list)
        second_list: list[int] = [0]
        list_node_2 = ListNode().generate_list_node_from_int_list(second_list)
        self.assertEqual(self.solution.add_two_numbers(linked_list_1=list_node_1, linked_list_2=list_node_2), [0])

    def test_add_two_numbers_case_3(self) -> None:
        first_list: list[int] = [9, 9, 9, 9, 9, 9, 9]
        list_node_1 = ListNode().generate_list_node_from_int_list(first_list)
        second_list: list[int] = [9, 9, 9, 9]
        list_node_2 = ListNode().generate_list_node_from_int_list(second_list)
        self.assertEqual(self.solution.add_two_numbers(linked_list_1=list_node_1, linked_list_2=list_node_2), [8, 9, 9, 9, 0, 0, 0, 1])


if __name__ == "__main__":
    main()
