# This is a problem given by Leetcode.com
# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

from unittest import TestCase, main

from utils.list_node import ListNode

ListNode.min_val = 0
ListNode.max_val = 1000


class Solution:
    """ You are given the head of a linked list (ListNode), which contains a series of integers separated by 0's.
        The beginning and end of the linked list will have Node.val == 0.

        For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes.
        The modified list should not contain any 0's.

        Return the head of the modified linked list.

        Constraints:

        - The number of nodes in the list is in the range [3, 2 * 10^5].
        - 0 <= Node.val <= 1000
        - There are no two consecutive nodes with Node.val == 0.
        - The beginning and end of the linked list have Node.val == 0.
    """

    def merge_nodes(self, head: ListNode) -> ListNode:
        """

        Args:
            head (ListNode): The head of a linked list

        Returns:
            list[int]: _description_
        """
        if head.val != 0:
            raise ValueError("The Head of list Node must be 0.")

        consumed = head
        current = head.next
        sum_to_add = 0
        while current:
            if current.val != 0:
                sum_to_add += current.val
            else:
                consumed.val = sum_to_add
                sum_to_add = 0
                if current.next:
                    consumed.next = current
                    consumed = current
                else:
                    consumed.next = None

            current = current.next

        return head


class TestListNode(TestCase):

    def setUp(self) -> None:
        self.list_node = ListNode()

    def test_generate_list_node_from_int_list_case_1(self) -> None:
        case_1: list[int] = [0, 3, 1, 0, 4, 5, 2, 0]
        result = self.list_node.generate_list_node_from_int_list(case_1)

        current = result
        for num in case_1:
            self.assertEqual(current.val, num)
            current = current.next

    def test_generate_list_node_from_int_list_case_2(self) -> None:
        case_1: list[int] = [0, 1, 0, 3, 0, 2, 2, 0]
        result: ListNode = self.list_node.generate_list_node_from_int_list(case_1)

        current: ListNode = result
        for num in case_1:
            self.assertEqual(current.val, num)
            current = current.next


class TestSolution(TestCase):

    def setUp(self) -> None:
        self.solution = Solution()
        self.list_node = ListNode()

    def test_case_1(self) -> None:
        case: list[int] = [0, 3, 1, 0, 4, 5, 2, 0]
        list_node: ListNode = self.list_node.generate_list_node_from_int_list(case)
        self.assertEqual(self.solution.merge_nodes(list_node), [4, 11])

    def test_case_2(self) -> None:
        case: list[int] = [0, 1, 0, 3, 0, 2, 2, 0]
        list_node: ListNode = self.list_node.generate_list_node_from_int_list(case)

        self.assertEqual(self.solution.merge_nodes(list_node), [1, 3, 4])


if __name__ == "__main__":
    main()
